<script setup>
import { decode } from "html-entities";

const { t, locale } = useI18n();

const base = locale._value == "en" ? ".." : "../..";

const data = await getCMS("start");
const release_data = await getCMS("release");

useHead({
  title: data._value.title,
  meta: [
    {
      name: "parameters",
      content: "sidebars: 0|1",
    },
  ],
  script: [
    {
      // this is here so it will run very early if the client supports js
      src: `${base}/js/startpage.js`,
      body: true,
    },
  ],
});

// number of headlines to display
const count_headlines = 9;
const count_headlines_narrow = 6;

// number of common issues to display
const count_common = 6;
const current_release = release_data._value.ga.releasever;

// number of solved issues to display
const count_solved = 4;

// number of commblog posts to display
const count_commblog = 4;

// user documentation
const user_documentation = data._value.sections[0];

// communication channels
const comm_channels = data._value.sections[1];

// latest council video
const latest_council_video = data._value.sections[2];

// query string parameters
const { sidebars = "1" } = useRoute().query;

// fedora reminders (weekly)
const reminder_data = await getCMS("reminders");

const fr_headlines = async () => {
  let reminders = reminder_data._value.links;

  let i = reminders.length - 1;
  let headlines = [];
  while (i >= 0) {
    let date = new Date(parseInt(reminders[i].reminder_date));
    let today = new Date();

    // only show reminders that are set for the current weekday
    if (date.getUTCDay() == today.getDay()) {
      headlines.push({
        timestamp: date,
        thumbnail: "public/assets/images/reminders-472x200.png",
        date: today.toLocaleDateString("en-US", {
          month: "short",
          day: "2-digit",
          year: "numeric",
        }),
        title: decode(reminders[i].text),
        link: reminders[i].url,
      });
    }

    i--;
  }

  return headlines;
};

let reminders = [];
try {
  if (process.client) {
    reminders = await fr_headlines();
  }
} catch (e) {
  console.log(e);
}

// fedora announcements
const discourse_uri = "https://discussion.fedoraproject.org";
const discourse_api = "c/news/announce-list/76";

const fa_headlines = async () => {
  let dcdata = await $fetch(`${discourse_uri}/${discourse_api}.json`);
  let topics = dcdata.topic_list.topics;

  let i = 0;
  let headlines = [];
  while (i < count_headlines + 1) {
    let title = topics[i].title;

    if (title == "About the Announce List category") {
      i++;
      continue;
    }

    let date = new Date(topics[i].created_at);

    headlines.push({
      timestamp: date,
      thumbnail: "public/assets/images/announcements-472x200.png",
      date: date.toLocaleDateString("en-US", {
        month: "short",
        day: "2-digit",
        year: "numeric",
      }),
      title: title,
      link: `${discourse_uri}/t/${topics[i].slug}`,
    });

    i++;
  }

  return headlines.slice(0, count_headlines);
};

let newsfeed = [];
try {
  newsfeed = await fa_headlines();
} catch (e) {
  console.log(e);
}

// fedora magazine
const magazine_uri = "https://fedoramagazine.org";
const magazine_api = "wp-json/fedora-ssr-endpoint";

const fm_headlines = async () => {
  let index = await $fetch(`${magazine_uri}/${magazine_api}/v1/index/1`);

  let i = 0;
  let headlines = [];
  while (i < count_headlines) {
    let date = new Date(index[i].date);

    headlines.push({
      timestamp: date,
      thumbnail: index[i].feature,
      date: date.toLocaleDateString("en-US", {
        month: "short",
        day: "2-digit",
        year: "numeric",
      }),
      title: decode(index[i].title),
      link: `${magazine_uri}/${index[i].slug}`,
      comments: index[i].comments.toString(),
    });

    i++;
  }

  return headlines;
};

let magazine = [];
try {
  magazine = await fm_headlines();
} catch (e) {
  console.log(e);
}

// fedora podcast
const podcast_data = await getCMS("podcast");

const fp_headlines = async () => {
  let topics = podcast_data._value.links;

  let i = topics.length - 1;
  let last = i - count_headlines;
  let headlines = [];
  while (i >= 0 && i > last) {
    let date = new Date(parseInt(topics[i].publication_date));

    // filter out podcasts with a future pub. date
    if (date.getTime() <= Date.now()) {
      headlines.push({
        timestamp: date,
        thumbnail: "public/assets/images/podcast-472x200.png",
        date: date.toLocaleDateString("en-US", {
          month: "short",
          day: "2-digit",
          year: "numeric",
        }),
        title: decode(topics[i].text),
        link: topics[i].url,
      });
    }

    i--;
  }

  return headlines;
};

let podcasts = [];
try {
  podcasts = await fp_headlines();
} catch (e) {
  console.log(e);
}

let combined = [...reminders, ...newsfeed, ...magazine, ...podcasts];
let headlines = combined
  .sort(function (a, b) {
    return b.timestamp - a.timestamp;
  })
  .slice(0, count_headlines);

const got_headlines = headlines.length == count_headlines;

const common_query = "tags/c/ask/common-issues/82/none/f" + current_release;

const fp_common_issues = async () => {
  let dcdata = await $fetch(`${discourse_uri}/${common_query}.json`);
  let topics = dcdata.topic_list.topics;

  let i = 0;
  let issues = [];
  while (i < count_common + 1) {
    let title = topics[i].title;

    if (title == "About the Common Issues category") {
      i++;
      continue;
    }

    issues.push({
      link: {
        url: `${discourse_uri}/t/${topics[i].slug}`,
        text: title,
      },
    });

    i++;
  }

  return issues.slice(0, count_common);
};

const solved_query = "q=%23ask%20status%3Asolved%20order%3Alatest_topic";
const user_avatars = "https://sea1.discourse-cdn.com/fedoraproject";

const fp_solved_issues = async () => {
  let dcdata = await $fetch(`${discourse_uri}/search.json?${solved_query}`);
  let solved = dcdata.posts;

  let i = 0;
  let issues = [];
  while (i < count_solved) {
    let avatar;
    if (solved[i].avatar_template) {
      avatar = solved[i].avatar_template.replace("{size}", "48");
      if (avatar.startsWith("/user_avatar")) {
        avatar = user_avatars + avatar;
      }
    } else {
      avatar = "/assets/images/unknown_avatar.png";
    }

    let topic;
    if (solved[i].topic_id) {
      topic = await $fetch(`${discourse_uri}/t/${solved[i].topic_id}.json`);
    }

    if (topic) {
      issues.push({
        avatar: avatar,
        link: {
          url: `${discourse_uri}/t/${topic.slug}`,
          text: topic.title,
        },
      });
    }

    i++;
  }

  return issues;
};

const commblog_uri = "https://communityblog.fedoraproject.org";
const commblog_api = "wp-json/fedora-ssr-endpoint";

const cb_headlines = async () => {
  let index = await $fetch(`${commblog_uri}/${commblog_api}/v1/index/1`);

  let i = 0;
  let headlines = [];
  while (i < count_commblog) {
    let date = new Date(index[i].date);

    headlines.push({
      timestamp: date,
      thumbnail: index[i].feature,
      date: date.toLocaleDateString("en-US", {
        month: "short",
        day: "2-digit",
        year: "numeric",
      }),
      link: {
        url: `${commblog_uri}/${index[i].slug}`,
        text: decode(index[i].title),
      },
    });

    i++;
  }

  return headlines;
};

let common = [],
  solved = [],
  commblog = [];
let got_common, got_solved, got_commblog;

if (parseInt(sidebars)) {
  try {
    common = await fp_common_issues();
  } catch (e) {
    console.log(e);
  }

  got_common = common.length == count_common;

  try {
    solved = await fp_solved_issues();
  } catch (e) {
    console.log(e);
  }

  got_solved = solved.length == count_solved;

  try {
    commblog = await cb_headlines();
  } catch (e) {
    console.log(e);
  }

  got_commblog = commblog.length == count_commblog;
}
</script>

<template>
  <div id="startpage" class="relative bg-fp-gray-lightest dark:bg-neutral-900">
    <!-- https://daniel.do/article/making-noisy-svgs/ -->
    <svg
      viewbox="0 0 100% 100%"
      class="absolute left-0 w-full top-0 h-full dark:hidden"
    >
      <defs>
        <rect id="sp-background" x="0" y="0" width="100%" height="100%" />
        <filter id="sp-background-noise">
          <feTurbulence
            type="fractalNoise"
            baseFrequency="19.5"
            numOctaves="10"
            result="turbulence"
          />
          <feComposite
            operator="in"
            in="turbulence"
            in2="SourceAlpha"
            result="composite"
          />
          <feColorMatrix in="composite" type="luminanceToAlpha" />
          <feBlend in="SourceGraphic" in2="composite" mode="color-burn" />
        </filter>
      </defs>
      <use
        href="#sp-background"
        fill="white"
        filter="url('#sp-background-noise')"
        opacity="0.5"
      />
    </svg>
    <div class="relative z-10 mx-8 flex gap-8 py-10">
      <!-- Left Sidebar -->
      <div class="sp_sidebar hidden w-[22em] max-w-[25vw] flex-none">
        <!-- Documentation -->
        <StartPageSidebarBlock
          link="https://docs.fedoraproject.org/en-US/fedora/latest/"
          :title="user_documentation.sectionTitle"
          :content="user_documentation.content"
          iconname="fa6-solid:book"
          iconsize="40"
        />
        <!-- Common Issues -->
        <StartPageSidebarBlock
          :link="`${discourse_uri}/${common_query}`"
          title="Common Issues"
          :content="common"
          iconname="fa6-solid:wrench"
          iconsize="32"
          :pulsers="count_common.toString()"
        >
          <template #footnote>
            <span class="text-base/4text-gray-400 font-semibold"
              >{{ $t("source:") }}
              <a
                target="_blank"
                :href="`${discourse_uri}/${common_query}`"
                class="text-fp-newblue"
                >discussion​.fedoraproject​.org</a
              ></span
            >
          </template>
        </StartPageSidebarBlock>
      </div>

      <!-- Center Column -->
      <div class="mx-auto w-full max-w-screen-xl flex-initial">
        <!-- Search Bar -->
        <div class="flex justify-center pb-12">
          <form
            class="max-h-[2em]"
            method="get"
            id="search"
            action="https://duckduckgo.com/"
          >
            <input
              class="w-full rounded-2xl bg-white py-2 font-semibold leading-[2em] ltr:pl-6 rtl:pr-6 dark:bg-gray-700 dark:text-gray-100 sm:text-2xl"
              type="text"
              name="q"
              maxlength="300"
              :placeholder="t('Search with DuckDuckGo')"
            />
            <input type="submit" value="Search" style="visibility: hidden" />
          </form>
        </div>
        <!-- Center Grid Content -->
        <h2
          class="mb-2 px-4 text-2xl font-semibold leading-none text-black dark:text-fp-gray-200"
        >
          {{ $t("Latest news and publications from the Fedora Project") }}:
          <ClientOnly>
            <template #fallback>
              <!-- Evil Icons Spinner-3 by Alexander Madyankin and Roman Shamin (MIT) -->
              <svg
                id="sp_spinner"
                class="inline animate-spin text-fp-blue invisible"
                xmlns="http://www.w3.org/2000/svg"
                width="24"
                height="24"
                viewBox="0 0 50 50"
              >
                <path
                  fill="currentColor"
                  d="M41.9 23.9c-.3-6.1-4-11.8-9.5-14.4c-6-2.7-13.3-1.6-18.3 2.6c-4.8 4-7 10.5-5.6 16.6c1.3 6 6 10.9 11.9 12.5c7.1 2 13.6-1.4 17.6-7.2c-3.6 4.8-9.1 8-15.2 6.9c-6.1-1.1-11.1-5.7-12.5-11.7c-1.5-6.4 1.5-13.1 7.2-16.4c5.9-3.4 14.2-2.1 18.1 3.7c1 1.4 1.7 3.1 2 4.8c.3 1.4.2 2.9.4 4.3c.2 1.3 1.3 3 2.8 2.1c1.3-.8 1.2-2.5 1.1-3.8c0-.4.1.7 0 0z"
                />
              </svg>
            </template>
          </ClientOnly>
        </h2>
        <!-- this is the static/ssr version of the newsitems -->
        <div class="sp_static flex flex-wrap" dir="ltr">
          <div
            v-for="h in headlines.slice(0, count_headlines_narrow)"
            class="mb-4 w-full p-4 md:w-1/2 2xl:w-1/3"
          >
            <StartPageNewsItem
              :link="h.link"
              :thumbnail="h.thumbnail"
              :date="h.date"
              :title="h.title"
              :comments="h.comments"
            />
          </div>
          <div
            v-for="h in headlines.slice(
              count_headlines_narrow,
              count_headlines,
            )"
            class="mb-4 w-full p-4 md:w-1/2 2xl:w-1/3 hidden 2xl:block"
          >
            <StartPageNewsItem
              :link="h.link"
              :thumbnail="h.thumbnail"
              :date="h.date"
              :title="h.title"
              :comments="h.comments"
            />
          </div>
        </div>
        <ClientOnly>
          <!-- this is the dynamic/client-side version of the newsitems -->
          <div class="flex flex-wrap" dir="ltr">
            <div
              v-for="h in headlines.slice(0, count_headlines_narrow)"
              class="mb-4 w-full p-4 md:w-1/2 2xl:w-1/3"
            >
              <StartPageNewsItem
                :link="h.link"
                :thumbnail="h.thumbnail"
                :date="h.date"
                :title="h.title"
                :comments="h.comments"
              />
            </div>
            <div
              v-for="h in headlines.slice(
                count_headlines_narrow,
                count_headlines,
              )"
              class="mb-4 w-full p-4 md:w-1/2 2xl:w-1/3 hidden 2xl:block"
            >
              <StartPageNewsItem
                :link="h.link"
                :thumbnail="h.thumbnail"
                :date="h.date"
                :title="h.title"
                :comments="h.comments"
              />
            </div>
          </div>
          <template #fallback>
            <div class="sp_pulser flex flex-wrap collapse fixed" dir="ltr">
              <div
                v-for="i in count_headlines_narrow"
                class="mb-4 w-full p-4 md:w-1/2 2xl:w-1/3"
              >
                <StartPageNewsItemLoading />
              </div>
              <div
                v-for="i in count_headlines - count_headlines_narrow"
                class="mb-4 w-full p-4 md:w-1/2 2xl:w-1/3 hidden 2xl:block"
              >
                <StartPageNewsItemLoading />
              </div>
            </div>
          </template>
        </ClientOnly>
        <div class="xl:hidden">
          <!-- Latest Solved Issues Mobile View -->
          <StartPageSidebarBlock
            :link="`${discourse_uri}/search?${solved_query}`"
            title="Latest Solved Issues"
            :content="solved"
            :pulsers="count_solved.toString()"
          >
            <template #footnote>
              <span class="text-base/4text-gray-400 font-semibold"
                >{{ $t("source:") }}
                <a
                  target="_blank"
                  :href="`${discourse_uri}/search?${solved_query}`"
                  class="text-fp-newblue"
                  >discussion​.fedoraproject​.org</a
                ></span
              >
            </template>
          </StartPageSidebarBlock>
          <!-- Community Blog Mobile View -->
          <StartPageSidebarBlock
            link="https://communityblog.fedoraproject.org/"
            title="Fedora Community Blog"
            subtitle="news for project contributors"
            :content="commblog"
            iconname="fa6-solid:feather-pointed"
            iconsize="32"
            :pulsers="count_commblog.toString()"
          />
          <!-- Documentation Mobile View -->
          <StartPageSidebarBlock
            link="https://docs.fedoraproject.org/en-US/fedora/latest/"
            :title="user_documentation.sectionTitle"
            :content="user_documentation.content"
            iconname="fa6-solid:book"
            iconsize="40"
          />
          <!-- Common Issues Mobile View -->
          <StartPageSidebarBlock
            :link="`${discourse_uri}/${common_query}`"
            title="Common Issues"
            :content="common"
            iconname="fa6-solid:wrench"
            iconsize="32"
            :pulsers="count_common.toString()"
          >
            <template #footnote>
              <span class="text-base/4text-gray-400 font-semibold"
                >{{ $t("source:") }}
                <a
                  target="_blank"
                  :href="`${discourse_uri}/${common_query}`"
                  class="text-fp-newblue"
                  >discussion​.fedoraproject​.org</a
                ></span
              >
            </template>
          </StartPageSidebarBlock>
        </div>
      </div>

      <!-- Right Sidebar -->
      <div class="sp_sidebar hidden w-[22em] max-w-[25vw] flex-none">
        <ClientOnly>
          <!-- Latest Council Video -->
          <StartPageSidebarBlock
            link="https://www.youtube.com/playlist?list=PL0x39xti0_64uSci6Wqk_E-IMSyq6vEuE"
            :title="latest_council_video.sectionTitle"
          >
            <template #loneitem>
              <iframe
                type="text/html"
                :src="`${base}/council-video.html`"
                frameborder="0"
                class="mx-auto h-[9em] w-[16em]"
              >
              </iframe>
            </template>
          </StartPageSidebarBlock>
          <template #fallback>
            <!-- Latest Council Video no Javascript -->
            <StartPageSidebarBlock
              link="https://www.youtube.com/playlist?list=PL0x39xti0_64uSci6Wqk_E-IMSyq6vEuE"
              :title="latest_council_video.sectionTitle"
            >
              <template #loneitem>
                <div
                  class="mx-auto h-[9em] w-[16em] bg-gray-400 animate-pulse"
                ></div>
              </template>
            </StartPageSidebarBlock>
          </template>
        </ClientOnly>
        <!-- Latest Solved Issues -->
        <StartPageSidebarBlock
          :link="`${discourse_uri}/search?${solved_query}`"
          title="Latest Solved Issues"
          :content="solved"
          :pulsers="count_solved.toString()"
        >
          <template #footnote>
            <span class="text-base/4text-gray-400 font-semibold"
              >{{ $t("source:") }}
              <a
                target="_blank"
                :href="`${discourse_uri}/search?${solved_query}`"
                class="text-fp-newblue"
                >discussion​.fedoraproject​.org</a
              ></span
            >
          </template>
        </StartPageSidebarBlock>
        <!-- Fedora Community Blog -->
        <StartPageSidebarBlock
          link="https://communityblog.fedoraproject.org/"
          title="Fedora Community Blog"
          subtitle="news for project contributors"
          :content="commblog"
          iconname="fa6-solid:feather-pointed"
          iconsize="32"
          :pulsers="count_commblog.toString()"
        />
      </div>
    </div>

    <FpPublicationSection
      class="relative z-10 bg-transparent dark:bg-neutral-900"
    />

    <FpCommunicationSection
      color="magenta"
      :sectionTitle="comm_channels.sectionTitle"
      :content="comm_channels.content"
      class="relative z-10 bg-white dark:bg-neutral-900"
    />

    <FpOrgChartSection
      class="relative z-10 bg-fp-gray-lightest dark:bg-neutral-900"
    />
  </div>
</template>

<style scoped>
a {
  cursor: default;
}
</style>
