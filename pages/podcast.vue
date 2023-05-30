<!-- vim:set ts=2 sw=2 et: -->

<script setup>
const data = await getCMS("podcast");
useContentHead(data);

// podcasts
const podcasts = data._value.sections[0];

// communication channels
const comm_channels = data._value.sections[1];

// show the newest episodes at the top of the page
let episodes = podcasts.content;
episodes.reverse();

const date_format = {
  month: "long",
  day: "numeric",
  year: "numeric",
};
</script>

<template>
  <div class="bg-fp-gray-lightest px-8 pt-8 dark:bg-neutral-900">
    <div class="mx-auto max-w-screen-xl">
      <div class="mb-8 text-center xl:text-start">
        <h2 class="xl:text-4xl">
          {{ podcasts.sectionTitle }}
        </h2>
      </div>
      <ul>
        <li v-for="e in episodes" class="mb-4">
          <a
            :href="e.link.url"
            class="text-2xl font-semibold leading-none text-fp-blue"
          >
            {{
              `${e.title} (${new Date(e.description).toLocaleDateString(
                "en-US",
                date_format
              )})`
            }}
          </a>
        </li>
      </ul>
    </div>
    <FpCommunicationSection
      color="magenta"
      :sectionTitle="comm_channels.sectionTitle"
      :content="comm_channels.content"
    />
  </div>
</template>
