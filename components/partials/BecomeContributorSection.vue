<script setup>
defineProps({});

// Data Import
let { data } = await useAsyncData(() => {
  return queryContent("/partials/become_contributor").findOne();
});
</script>
<template>
  <div class="container mx-auto max-w-7xl">
    <div class="my-5 p-2">
      <h4
        class="mb-2 text-lg font-semibold text-fp-blue-light dark:text-gray-200"
      >
        <Icon
          name="fa6-solid:door-open"
          class="mr-1 !align-top text-fp-blue-light dark:text-gray-200"
          size="1.5rem"
        />
        {{ $t(data.sectionTitle) }}
      </h4>
      <p class="mx-2 mb-5 mt-2 text-xl text-gray-800 dark:text-gray-300">
        {{ $t(data.sectionDescription) }}
      </p>

      <p
        class="mb-8 mt-12 text-center font-display text-sm font-semibold uppercase text-fp-gray"
      >
        {{ $t(data.officialChannels.title) }}
      </p>
      <div class="flex flex-wrap justify-center gap-24">
        <FpLink
          class="text-center text-blue-500"
          v-for="item in data.officialChannels.content"
          :href="item.link"
        >
          <FpImage
            class="max-h-14 dark:brightness-200 dark:grayscale"
            :src="item.image"
          />
        </FpLink>
      </div>
      <p
        class="mb-8 mt-16 text-center font-display text-sm font-semibold uppercase text-fp-gray"
      >
        {{ $t(data.communityChannels.title) }}
      </p>
      <div class="flex flex-wrap items-center justify-center gap-24">
        <FpLink
          class="text-center text-xl text-fp-blue-dark underline dark:text-gray-200"
          v-for="item in data.communityChannels.content"
          :href="item.link"
        >
          <FpImage
            class="mr-2 inline-block max-h-14 dark:brightness-200 dark:grayscale"
            :src="item.image"
          />{{ $t(item.title) }}</FpLink
        >
      </div>
    </div>
  </div>
</template>
