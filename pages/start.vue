<!-- vim:set ts=2 sw=2 et: -->

<script setup>
import { decode } from "html-entities";

const { t } = useI18n();

const data = await getCMS("start");
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
      children: `document.getElementById("spinner").style.visibility = "visible";`,
      body: true,
    },
  ],
});

// number of headlines to display
const count_headlines = 9;
const count_headlines_narrow = 6;

// number of common issues to display
const count_common = 6;

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
      thumbnail: "/assets/images/announcements-472x200.png",
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
  if (process.client) {
    newsfeed = await fa_headlines();
  }
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
    });

    i++;
  }

  return headlines;
};

let magazine = [];
try {
  if (process.client) {
    magazine = await fm_headlines();
  }
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
        thumbnail: "/assets/images/podcast-472x200.png",
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
  if (process.client) {
    podcasts = await fp_headlines();
  }
} catch (e) {
  console.log(e);
}

let combined = [...newsfeed, ...magazine, ...podcasts];
let headlines = combined
  .sort(function (a, b) {
    return b.timestamp - a.timestamp;
  })
  .slice(0, count_headlines);

const got_headlines = process.server || headlines.length == count_headlines;

const common_query = "c/ask/common-issues/82/none";

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
      title: title,
      link: `${discourse_uri}/t/${topics[i].slug}`,
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
        title: topic.title,
        link: `${discourse_uri}/t/${topic.slug}`,
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
      title: decode(index[i].title),
      link: `${commblog_uri}/${index[i].slug}`,
    });

    i++;
  }

  return headlines;
};

let common = [],
  solved = [],
  commblog = [];
let got_common, got_solved, got_commblog;

if (parseInt(sidebars) && process.client) {
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

// https://tailwindcss.com/docs/responsive-design
const width_2xl = 1536;

// https://stackoverflow.com/a/71210364 (CC BY-SA 4.0)
const get_width = () => {
  let width = ref(window.innerWidth);

  const onWidthChange = () => (width.value = window.innerWidth);

  onMounted(() => window.addEventListener("resize", onWidthChange));
  onUnmounted(() => window.removeEventListener("resize", onWidthChange));

  return computed(() => width.value);
};

let width = width_2xl;
if (process.client) {
  width = get_width();
}

let static_headlines = await fp_headlines();
</script>

<template>
  <div class="bg-fp-gray-lightest dark:bg-neutral-900">
    <div class="mx-8 flex gap-8 py-10">
      <!-- Left Sidebar -->
      <div
        v-if="sidebars != '0'"
        class="hidden w-[22em] max-w-[25vw] flex-none xl:block"
      >
        <!-- Documentation -->
        <div class="mb-6 rounded-2xl bg-white p-4 dark:bg-gray-700">
          <h2 class="mb-8 text-2xl leading-none">
            <a
              href="https://docs.fedoraproject.org/en-US/fedora/latest/"
              class="text-2xl font-semibold leading-none text-fp-newblue"
              >{{ $t(user_documentation.sectionTitle) }}</a
            >
          </h2>
          <div v-for="d in user_documentation.content" class="mb-6">
            <div class="flex items-center">
              <a :href="d.link.url" class="flex-none"
                ><Icon name="fa6-solid:book" size="48" class="text-fp-blue"
              /></a>
              <a
                :href="d.link.url"
                class="max-h-12 overflow-hidden text-base font-semibold ltr:ml-6 rtl:mr-6"
                >{{ d.link.text }}</a
              >
            </div>
          </div>
        </div>
        <ClientOnly>
          <!-- Common Issues -->
          <div class="rounded-2xl bg-white p-4 dark:bg-gray-700" dir="ltr">
            <h2 class="mb-8 text-2xl leading-none">
              <a
                :href="`${discourse_uri}/${common_query}`"
                class="text-2xl font-semibold leading-none text-fp-newblue"
                >{{ $t("Common Issues") }}</a
              >
            </h2>
            <div v-for="i in common" class="mb-6">
              <div class="ml-2 flex items-center">
                <a :href="i.link" class="flex-none p-2"
                  ><Icon name="fa6-solid:wrench" size="32" class="text-fp-blue"
                /></a>
                <a
                  :href="i.link"
                  class="ml-4 max-h-12 overflow-hidden text-base font-semibold"
                  >{{ i.title }}</a
                >
              </div>
            </div>
            <div class="whitespace-no-wrap text-right">
              <span class="text-base/4text-gray-400 font-semibold"
                >{{ $t("From") }}
                <a href="https://ask.fedoraproject.org/" class="text-fp-newblue"
                  >ask​.​fedoraproject​.​org</a
                ></span
              >
            </div>
          </div>
        </ClientOnly>
      </div>

      <!-- Center Column -->
      <div class="mx-auto max-w-screen-xl flex-initial">
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
        <div>
          <ClientOnly>
            <!-- Center Grid Content -->
            <h2 class="mb-2 px-4 text-2xl font-semibold leading-none">
              {{ $t("Latest news and publications from the Fedora Project") }}:
            </h2>
            <div v-if="got_headlines" class="flex flex-wrap" dir="ltr">
              <div
                v-for="h in width < width_2xl
                  ? headlines.slice(0, count_headlines_narrow)
                  : headlines"
                class="mb-4 w-full p-4 md:w-1/2 2xl:w-1/3"
              >
                <StartPageNewsItem
                  :link="h.link"
                  :thumbnail="h.thumbnail"
                  :date="h.date"
                  :title="h.title"
                />
              </div>
            </div>
            <div v-else class="flex flex-wrap" dir="ltr">
              <div
                v-for="i in count_headlines"
                class="mb-4 w-full p-4 md:w-1/2 2xl:w-1/3"
              >
                <StartPageNewsItemLoading />
              </div>
            </div>
            <!-- the fallback template is what users without javascript will see -->
            <template #fallback>
              <!-- Center Grid Content no Javascript -->
              <h2 class="mb-2 px-4 text-2xl font-semibold leading-none">
                {{ $t("Latest Fedora Podcasts") }}:
                <!-- Evil Icons Spinner-3 by Alexander Madyankin and Roman Shamin (MIT) -->
                <svg
                  id="spinner"
                  style="visibility: hidden"
                  class="inline animate-spin text-fp-blue"
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
              </h2>
              <div
                v-if="static_headlines.length > 0"
                class="flex flex-wrap"
                dir="ltr"
              >
                <div class="flex flex-wrap" dir="ltr">
                  <div
                    v-for="h in width < width_2xl
                      ? static_headlines.slice(0, count_headlines_narrow)
                      : static_headlines"
                    class="mb-4 w-full p-4 md:w-1/2 2xl:w-1/3"
                  >
                    <StartPageNewsItem
                      :link="h.link"
                      :thumbnail="h.thumbnail"
                      :date="h.date"
                      :title="h.title"
                    />
                  </div>
                </div>
              </div>
            </template>
          </ClientOnly>
        </div>
        <!-- Latest Solved Issues Mobile View -->
        <div
          class="mb-6 rounded-2xl bg-white p-6 dark:bg-gray-700 xl:hidden"
          dir="ltr"
        >
          <h2 class="mb-8 text-2xl leading-none">
            <a
              :href="`${discourse_uri}/search?${solved_query}`"
              class="text-2xl font-semibold leading-none text-fp-newblue"
              >{{ $t("Latest Solved Issues") }}</a
            >
          </h2>
          <div class="mb-6 grid grid-cols-1 gap-6 md:grid-cols-2">
            <div v-for="s in solved">
              <div class="flex items-center">
                <a :href="s.link" class="flex-none"
                  ><img :src="s.avatar" class="h-12 w-12 rounded object-cover"
                /></a>
                <a
                  :href="s.link"
                  class="ml-6 max-h-12 overflow-hidden text-base font-semibold"
                  >{{ s.title }}</a
                >
              </div>
            </div>
          </div>
          <div class="whitespace-no-wrap text-right">
            <span class="text-base/4text-gray-400 font-semibold"
              >{{ $t("From") }}
              <a href="https://ask.fedoraproject.org/" class="text-fp-newblue"
                >ask​.​fedoraproject​.​org</a
              ></span
            >
          </div>
        </div>
        <!-- Community Blog Mobile View -->
        <div
          class="mb-6 rounded-2xl bg-white p-6 dark:bg-gray-700 xl:hidden"
          dir="ltr"
        >
          <h2 class="text-2xl leading-none">
            <a
              href="https://communityblog.fedoraproject.org/"
              class="text-2xl font-semibold leading-none text-fp-newblue"
              >Fedora Community Blog</a
            >
            <p class="mb-6 font-semibold text-fp-newblue">
              ({{ $t("news for project contributors") }})
            </p>
          </h2>
          <div class="grid grid-cols-1 gap-6 md:grid-cols-2">
            <div v-for="p in commblog" class="mb-6">
              <div class="ml-2 flex items-center">
                <a :href="p.link" class="flex-none p-2"
                  ><Icon
                    name="fa6-solid:feather-pointed"
                    size="32"
                    class="text-fp-blue"
                /></a>
                <a
                  :href="p.link"
                  class="ml-4 max-h-12 overflow-hidden text-base font-semibold"
                  >{{ p.title }}</a
                >
              </div>
            </div>
          </div>
        </div>
        <!-- Documentation Mobile View -->
        <div class="mb-6 rounded-2xl bg-white p-6 dark:bg-gray-700 xl:hidden">
          <h2 class="mb-8 text-2xl leading-none">
            <a
              href="https://docs.fedoraproject.org/en-US/fedora/latest/"
              class="text-2xl font-semibold leading-none text-fp-newblue"
              >{{ $t(user_documentation.sectionTitle) }}</a
            >
          </h2>
          <div class="grid grid-cols-1 gap-6 md:grid-cols-2">
            <div v-for="d in user_documentation.content">
              <div class="flex items-center">
                <a :href="d.link.url" class="flex-none"
                  ><Icon name="fa6-solid:book" size="48" class="text-fp-blue"
                /></a>
                <a
                  :href="d.link.url"
                  class="max-h-12 overflow-hidden text-base font-semibold ltr:ml-6 rtl:mr-6"
                  >{{ d.link.text }}</a
                >
              </div>
            </div>
          </div>
        </div>
        <!-- Common Issues Mobile View -->
        <div
          class="mb-6 rounded-2xl bg-white p-6 dark:bg-gray-700 xl:hidden"
          dir="ltr"
        >
          <h2 class="mb-8 text-2xl leading-none">
            <a
              :href="`${discourse_uri}/${common_query}`"
              class="text-2xl font-semibold leading-none text-fp-newblue"
              >{{ $t("Common Issues") }}</a
            >
          </h2>
          <div class="mb-6 grid grid-cols-1 gap-6 md:grid-cols-2">
            <div v-for="i in common">
              <div class="ml-2 flex items-center">
                <a :href="i.link" class="flex-none p-2"
                  ><Icon name="fa6-solid:wrench" size="32" class="text-fp-blue"
                /></a>
                <a
                  :href="i.link"
                  class="ml-4 max-h-12 overflow-hidden text-base font-semibold"
                  >{{ i.title }}</a
                >
              </div>
            </div>
          </div>
          <div class="whitespace-no-wrap text-right">
            <span class="text-base/4text-gray-400 font-semibold"
              >{{ $t("From") }}
              <a href="https://ask.fedoraproject.org/" class="text-fp-newblue"
                >ask​.​fedoraproject​.​org</a
              ></span
            >
          </div>
        </div>
      </div>

      <!-- Right Sidebar -->
      <div
        v-if="sidebars != '0'"
        class="hidden w-[22em] max-w-[25vw] flex-none xl:block"
      >
        <ClientOnly>
          <!-- Latest Council Video -->
          <div class="mb-6 rounded-2xl bg-white p-4 dark:bg-gray-700">
            <h2 class="mb-8 text-2xl leading-none">
              <a
                href="https://www.youtube.com/playlist?list=PL0x39xti0_64uSci6Wqk_E-IMSyq6vEuE"
                target="_blank"
                class="text-2xl font-semibold leading-none text-fp-newblue"
                >{{ $t(latest_council_video.sectionTitle) }}</a
              >
            </h2>
            <div class="mb-6 grid place-items-center">
              <iframe
                type="text/html"
                src="/council-video.html"
                frameborder="0"
                class="h-[9em] w-[16em]"
              >
              </iframe>
            </div>
          </div>
          <!-- Latest Solved Issues -->
          <div class="mb-6 rounded-2xl bg-white p-4 dark:bg-gray-700" dir="ltr">
            <h2 class="mb-8 text-2xl leading-none">
              <a
                :href="`${discourse_uri}/search?${solved_query}`"
                class="text-2xl font-semibold leading-none text-fp-newblue"
                >{{ $t("Latest Solved Issues") }}</a
              >
            </h2>
            <div v-for="s in solved" class="mb-6">
              <div class="flex items-center">
                <a :href="s.link" class="flex-none"
                  ><img :src="s.avatar" class="h-12 w-12 rounded object-cover"
                /></a>
                <a
                  :href="s.link"
                  class="ml-6 max-h-12 overflow-hidden text-base font-semibold"
                  >{{ s.title }}</a
                >
              </div>
            </div>
            <div class="whitespace-no-wrap text-right">
              <span class="text-base/4text-gray-400 font-semibold"
                >{{ $t("From") }}
                <a href="https://ask.fedoraproject.org/" class="text-fp-newblue"
                  >ask​.​fedoraproject​.​org</a
                ></span
              >
            </div>
          </div>
          <!-- Fedora Community Blog -->
          <div class="rounded-2xl bg-white p-4 dark:bg-gray-700" dir="ltr">
            <h2 class="text-2xl leading-none">
              <a
                href="https://communityblog.fedoraproject.org/"
                class="text-2xl font-semibold leading-none text-fp-newblue"
                >Fedora Community Blog</a
              >
              <p class="mb-6 font-semibold text-fp-newblue">
                ({{ $t("news for project contributors") }})
              </p>
            </h2>
            <div v-for="p in commblog" class="mb-6">
              <div class="ml-2 flex items-center">
                <a :href="p.link" class="flex-none p-2"
                  ><Icon
                    name="fa6-solid:feather-pointed"
                    size="32"
                    class="text-fp-blue"
                /></a>
                <a
                  :href="p.link"
                  class="ml-4 max-h-12 overflow-hidden text-base font-semibold"
                  >{{ p.title }}</a
                >
              </div>
            </div>
          </div>
          <!-- right-hand sidebar content for users without javascript -->
          <template #fallback>
            <!-- Latest Council Video no Javascript -->
            <div class="mb-6 rounded-2xl bg-white p-4 dark:bg-gray-700">
              <h2 class="mb-8 text-2xl leading-none">
                <a
                  href="https://www.youtube.com/playlist?list=PL0x39xti0_64uSci6Wqk_E-IMSyq6vEuE"
                  target="_blank"
                  class="text-2xl font-semibold leading-none text-fp-newblue"
                  >{{ $t(latest_council_video.sectionTitle) }}</a
                >
              </h2>
              <div class="mb-6 grid place-items-center">
                <div class="relative bg-black h-[9em] w-[16em] overflow-hidden">
                  <FpLink :href="latest_council_video.content[0].link.url">
                    <FpImage :src="latest_council_video.content[0].image" />
                  </FpLink>
                  <div
                    class="z-1 absolute top-2 w-full grid place-items-center"
                  >
                    <div
                      class="px-2 text-2xl font-semibold bg-white/50 rounded-2xl text-center"
                    >
                      {{ latest_council_video.content[0].link.text }}
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </template>
        </ClientOnly>
      </div>
    </div>
  </div>

  <FpPublicationSection class="bg-fp-gray-lightest dark:bg-neutral-900" />

  <FpCommunicationSection
    color="magenta"
    :sectionTitle="comm_channels.sectionTitle"
    :content="comm_channels.content"
  />

  <FpOrgChartSection />
</template>
