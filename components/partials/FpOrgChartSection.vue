<!-- vim:set ts=2 sw=2 et: -->

<script setup>
defineProps({});

// Data Import
const { data } = await useAsyncData(() => {
  return queryContent("/partials/fporgchart").findOne();
});

const title = data._value.title;
const subtext = data._value.subtext;

const bgimage = data._value.image;
const [bgwidth, bgheight] = data._value.dimensions.split(",");

const links = data._value.links.map(({ text, url, region }) => ({
  text: text,
  url: url,
  region: region.split(","),
}));
</script>

<template>
  <section class="px-8">
    <div class="container mx-auto max-w-7xl pb-8">
      <header class="py-8">
        <h2 class="text-center xl:text-start">
          {{ $t(title) }}
        </h2>
        <p v-if="subtext" class="text-center text-2xl xl:text-start">
          {{ $t(subtext) }}
        </p>
      </header>
      <div class="relative">
        <FpImage :src="bgimage" class="rounded-2xl" />
        <div class="absolute top-0 left-0 h-full w-full">
          <svg
            width="100%"
            height="100%"
            :viewBox="`0 0 ${bgwidth} ${bgheight}`"
          >
            <a v-for="link in links" :href="link.url" target="_blank">
              <circle
                v-if="link.region.length == 3"
                :cx="link.region[0]"
                :cy="link.region[1]"
                :r="link.region[2]"
                :alt="link.text"
                class="duration-250 fill-white opacity-0 transition ease-in-out hover:opacity-20"
              />
              <rect
                v-if="link.region.length == 4"
                :x="link.region[0]"
                :y="link.region[1]"
                :width="link.region[2]"
                :height="link.region[3]"
                rx="1rem"
                :alt="link.text"
                class="duration-250 fill-white opacity-0 transition ease-in-out hover:opacity-20"
              />
            </a>
          </svg>
        </div>
      </div>
    </div>
  </section>
</template>
