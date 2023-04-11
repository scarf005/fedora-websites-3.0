<!-- vim:set ts=2 et: -->

<script setup>
import { decode } from "html-entities";

const data = await getCMS("start");
useContentHead(data);

// number of headlines to display
const count_headlines = 8;

// number of solved issues to display
const count_solved = 6;

// user documentation
const user_documentation = data._value.sections[0];

// communication channels
const comm_channels = data._value.sections[1];

const magazine_uri = "https://fedoramagazine.org";
const magazine_api = "wp-json/fedora-ssg-endpoint";

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

const discourse_uri = "https://discussion.fedoraproject.org";
const discourse_api = "c/news/announce-list/76.json";

const fp_headlines = async () => {
  let dcdata = await $fetch(`${discourse_uri}/${discourse_api}`);
  let topics = dcdata.topic_list.topics;

  let i = 0;
  let headlines = [];
  while (i < count_headlines + 1) {
    let date = new Date(topics[i].created_at);

    if (topics[i].title == "About the Announce List category") {
      i++;
      continue;
    }

    headlines.push({
      timestamp: date,
      thumbnail: "/assets/images/announcements-472x200.png",
      date: date.toLocaleDateString("en-US", {
        month: "short",
        day: "2-digit",
        year: "numeric",
      }),
      title: topics[i].title,
      link: `${discourse_uri}/t/${topics[i].slug}`,
    });

    i++;
  }

  return headlines.slice(0, count_headlines);
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

let magazine = [];
try {
  magazine = await fm_headlines();
} catch (e) {
  console.log(e);
}

let newsfeed = [];
try {
  newsfeed = await fp_headlines();
} catch (e) {
  console.log(e);
}

let headlines;
if (magazine.length > 0 && newsfeed.length > 0) {
  let combined = [...magazine, ...newsfeed];
  headlines = combined
    .sort(function (a, b) {
      return b.timestamp - a.timestamp;
    })
    .slice(0, count_headlines);
} else if (magazine.length > 0) {
  headlines = magazine;
} else if (newsfeed.length > 0) {
  headlines = newsfeed;
} else {
  headlines = [];
}

let solved = [];
try {
  solved = await fp_solved_issues();
} catch (e) {
  console.log(e);
}
</script>

<template>
  <div class="min-h-screen bg-fp-gray-lightest dark:bg-neutral-900">
    <div
      v-if="headlines.length == count_headlines"
      class="mx-auto flex w-11/12 gap-10 py-8"
    >
      <ClientOnly>
        <div class="w-full flex-auto pt-4 2xl:w-4/5">
          <h2
            class="mb-2 px-4 text-2xl font-semibold leading-none text-gray-600 dark:text-gray-400"
            dir="ltr"
          >
            {{ "Latest news and publications from the Fedora Project:" }}
          </h2>
          <div class="flex flex-wrap" dir="ltr">
            <div
              v-for="h in headlines"
              class="mb-4 w-full p-4 md:w-1/2 lg:w-1/4"
            >
              <div>
                <a :href="h.link">
                  <img :src="h.thumbnail" class="w-full rounded-lg" />
                </a>
              </div>
              <div class="text-base leading-8 text-gray-500">
                {{ h.date }}
              </div>
              <div class="max-h-[5.25rem] overflow-hidden">
                <a
                  :href="h.link"
                  class="align-top text-xl font-semibold text-fp-blue"
                  >{{ h.title }}</a
                >
              </div>
            </div>
          </div>
          <FpPublicationSection
            class="bg-fp-gray-lightest dark:bg-neutral-900"
          />
        </div>
        <div
          v-if="solved.length == count_solved"
          class="hidden flex-none px-4 2xl:block 2xl:w-1/5"
          dir="ltr"
        >
          <div class="mb-6 rounded-2xl bg-white p-4 dark:bg-gray-700">
            <h2 class="mb-8 text-2xl leading-none">
              <a
                :href="`${discourse_uri}/search?${solved_query}`"
                class="text-2xl font-semibold leading-none text-fp-newblue"
                >{{ "Latest Solved Issues" }}</a
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
                >From
                <a href="https://ask.fedoraproject.org/" class="text-fp-newblue"
                  >ask​.​fedoraproject​.​org</a
                ></span
              >
            </div>
          </div>
          <div class="rounded-2xl bg-white p-4 dark:bg-gray-700">
            <h2 class="mb-8 text-2xl leading-none">
              <a
                href="https://docs.fedoraproject.org/"
                class="text-2xl font-semibold leading-none text-fp-newblue"
                >{{ user_documentation.sectionTitle }}</a
              >
            </h2>
            <div v-for="d in user_documentation.content" class="mb-6">
              <div class="flex items-center">
                <a :href="d.link.url" class="flex-none"
                  ><Icon name="fa6-solid:book" size="48" class="text-fp-blue"
                /></a>
                <a
                  :href="d.link.url"
                  class="ml-6 max-h-12 overflow-hidden text-base font-semibold"
                  >{{ d.link.text }}</a
                >
              </div>
            </div>
          </div>
        </div>
      </ClientOnly>
    </div>
  </div>

  <!-- communication channels -->
  <FpCommunicationSection
    color="magenta"
    :sectionTitle="comm_channels.sectionTitle"
    :content="comm_channels.content"
  />
</template>
