<script setup>
const props = defineProps({
  background_image: String,
  logo_image: String,
  cta_links: Array,
  title: String,
  description: String,
});
</script>
<template>
  <FpHero
    :background="background_image"
    alignment="bg-top"
    class="bg-gray-500 bg-blend-multiply"
  >
    <FpBanner
      :logo="logo_image"
      color="text-fp-purple"
      border="border border-fp-purple"
      background="text-white bg-fp-purple"
      :ctas="cta_links"
    >
      <template #title>
        <slot name="location"></slot>
      </template>
      <template #subtitle>
        <h2
          class="mt-5 font-semibold text-white sm:mt-24 text-2xl sm:text-4xl lg:text-6xl"
        >
          {{ $t(title) }}
        </h2>
      </template>
      <h2 class="my-4 text-center font-semibold text-white">
        {{ $t(description) }}
      </h2>
    </FpBanner>
  </FpHero>
</template>
