<!-- vim:set ts=2 et: -->

<script setup>
import { decode } from "html-entities";

const data = await getCMS("start");
useContentHead(data);

const magazine_uri = "https://fedoramagazine.org";
const magazine_api = "wp-json/fedora-ssg-endpoint";

const fm_headlines = async () => {
  let index = await $fetch(`${magazine_uri}/${magazine_api}/v1/index/1`);

  let i,
    headlines = [];
  for (i = 0; i < 6; i++) {
    let date = new Date(index[i].date);

    headlines.push({
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
  }

  return headlines;
};

let headlines;
try {
  headlines = await fm_headlines();
} catch (e) {
  console.log(e);
}
</script>

<template>
  <div class="mx-auto w-4/5 max-w-7xl md:mt-2">
    <h2 class="py-4 text-[30px] font-semibold">{{ data.description }}</h2>
    <div
      v-for="h in headlines"
      class="sm:max-h-22 mb-6 flex flex-wrap bg-gray-200 px-4 py-4 dark:bg-neutral-900 sm:flex-nowrap"
    >
      <div class="w-16 w-1/2 flex-shrink-0 pr-4 align-top sm:w-auto">
        <div class="text-[16px] font-semibold uppercase leading-none">
          {{ h.month }}
        </div>
        <div class="text-[30px] font-bold leading-none">
          {{ h.day }}
        </div>
      </div>
      <div class="w-1/2 flex-shrink-0 pb-4 sm:w-auto sm:pr-4 md:pb-0">
        <a :href="h.link">
          <img :src="h.feature" class="float-right h-14" />
        </a>
      </div>
      <div class="mb-[1px] h-14 max-h-14 overflow-y-hidden align-top">
        <div class="text-lg font-semibold leading-none text-fp-blue sm:text-xl">
          <a :href="h.link">{{ h.title }}</a>
        </div>
        <div class="hidden text-lg sm:block sm:truncate">{{ h.excerpt }}</div>
      </div>
    </div>
  </div>

  <FpPublicationSection class="bg-gray-200 dark:bg-neutral-900" />

  <!-- communication channels -->
  <FpCommunicationSection
    color="magenta"
    :sectionTitle="data.sections[0].sectionTitle"
    :content="data.sections[0].content"
  />
</template>
