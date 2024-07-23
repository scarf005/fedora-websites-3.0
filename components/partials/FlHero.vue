<script setup>
const props = defineProps({});
</script>
<template>
  <FpHero
    :background="data.header_images[1].image"
    alignment="bg-top"
    class="bg-gray-500 bg-blend-multiply"
  >
    <FpBanner
      :logo="data.header_images[0].image"
      color="text-fp-purple"
      border="border border-fp-purple"
      background="text-white bg-fp-purple"
      :ctas="data.links"
    >
      <!-- TODO: change me to #location -->
      <template #title>
        <div
          class="mx-auto sm:-mt-10 max-w-xs text-right text-lg font-semibold uppercase text-white -mt-8 sm:max-w-lg sm:text-2xl"
        >
          {{ $t(data.location) }}
        </div>
      </template>
      <template #subtitle>
        <h2
          class="mt-5 font-semibold text-white sm:mt-24 text-2xl sm:text-4xl lg:text-6xl"
        >
          {{ $t(data.title) }}
        </h2>
      </template>
      <h2 class="my-4 text-center font-semibold text-white">
        {{ $t(data.description) }}
      </h2>
    </FpBanner>
  </FpHero>
</template>
