<!-- vim:set ts=2 sw=2 et: -->

<script setup>
const data = await getCMS("podcast");
useContentHead(data);

const links = data._value.links;

// show the newest podcasts at the top of the page
let podcasts = [];
for (let i = links.length - 1; i >= 0; i--) {
  // filter out podcasts with a future pub. date
  if (links[i].publication_date <= Date.now()) {
    podcasts.push(links[i]);
  }
}

const date_format = {
  month: "long",
  day: "numeric",
  year: "numeric",
};

// communication channels
const comm_channels = data._value.sections[0];
</script>

<template>
  <FpImage
    class="w-full from-fp-newblue-500 to-fp-blue ltr:bg-gradient-to-r rtl:bg-gradient-to-l dark:from-fp-darkblue-500 dark:to-fp-blue"
    :src="data.image"
  />
  <div class="bg-fp-gray-lightest px-8 pt-8 dark:bg-neutral-900">
    <div class="mx-auto max-w-screen-xl">
      <div class="mb-8 text-center xl:text-start">
        <h2 class="xl:text-4xl">
          {{ $t("Podcasts") }}
        </h2>
      </div>
      <ul>
        <li v-for="p in podcasts" class="mb-4">
          <a
            :href="p.url"
            class="text-2xl font-semibold leading-none text-fp-blue"
          >
            {{
              `${p.text} (${new Date(
                parseInt(p.publication_date)
              ).toLocaleDateString("en-US", date_format)})`
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
