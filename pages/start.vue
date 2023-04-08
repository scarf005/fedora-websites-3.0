<!-- vim:set ts=2 et: -->

<script setup>
import { decode } from "html-entities";

const data = await getCMS("start");
useContentHead(data);

const magazine_uri = "https://fedoramagazine.org";
const magazine_api = "wp-json/fedora-ssg-endpoint";

const fm_headlines = async () => {
  let index = await $fetch(`${magazine_uri}/${magazine_api}/v1/index/1`);

  let i = 0;
  let headlines = [];
  while (i < 6) {
    let date = new Date(index[i].date);

    headlines.push({
      date: date,
      month: date.toLocaleDateString("en-US", {
        month: "short",
      }),
      day: date.toLocaleDateString("en-US", {
        day: "2-digit",
      }),
      feature: index[i].feature,
      title: decode(index[i].title),
      excerpt: index[i].excerpt,
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
  while (i < 7) {
    let date = new Date(topics[i].created_at);

    if (topics[i].title == "About the Announce List category") {
      i++;
      continue;
    }

    headlines.push({
      date: date,
      month: date.toLocaleDateString("en-US", {
        month: "short",
      }),
      day: date.toLocaleDateString("en-US", {
        day: "2-digit",
      }),
      icon: "public/assets/images/fedora-discussion-plus-icon.png",
      title: topics[i].title,
      link: `${discourse_uri}/t/${topics[i].slug}`,
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
      return b.date - a.date;
    })
    .slice(0, 6);
} else if (magazine.length > 0) {
  headlines = magazine;
} else if (newsfeed.length > 0) {
  headlines = newsfeed;
} else {
  headlines = [];
}
</script>

<template>
  <FpHero :background="data.header_images[0].image" alignment="mt-2">
    <div class="mx-auto w-4/5 max-w-7xl pb-6 md:mt-2">
      <h2 class="py-4 text-[30px] font-semibold text-white dark:text-gray-400">
        {{ data.description }}
      </h2>
      <div
        v-for="h in headlines"
        class="sm:max-h-22 opacity-85 mb-6 flex flex-wrap bg-white px-4 py-4 dark:bg-gray-600 dark:opacity-80 sm:flex-nowrap"
      >
        <div class="w-16 w-1/2 flex-shrink-0 pr-4 align-top sm:w-auto">
          <div
            class="text-[16px] font-semibold uppercase leading-none sm:text-center"
          >
            {{ h.month }}
          </div>
          <div class="text-[30px] font-bold leading-none sm:text-center">
            {{ h.day }}
          </div>
        </div>
        <div class="w-1/2 flex-shrink-0 pb-4 sm:w-auto sm:pr-4 md:pb-0">
          <a :href="h.link">
            <img v-if="h.feature" :src="h.feature" class="float-right h-14" />
            <FpImage
              v-if="h.icon"
              :src="h.icon"
              class="float-right h-14 w-[132px] bg-gray-200 py-4 px-4"
            />
          </a>
        </div>
        <div class="mb-[1px] h-14 max-h-14 overflow-y-hidden align-top">
          <div
            class="text-lg font-semibold leading-none text-fp-newblue sm:text-xl"
          >
            <a :href="h.link">{{ h.title }}</a>
          </div>
          <div v-if="h.excerpt" class="hidden text-lg sm:block sm:truncate">
            {{ h.excerpt }}
          </div>
        </div>
      </div>
    </div>
  </FpHero>

  <FpPublicationSection class="bg-gray-200 dark:bg-neutral-900" />

  <!-- communication channels -->
  <FpCommunicationSection
    color="magenta"
    :sectionTitle="data.sections[0].sectionTitle"
    :content="data.sections[0].content"
  />
</template>
