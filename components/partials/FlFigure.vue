<script setup>
const props = defineProps({
  path: String,
  alt: String,
  caption: String,
});
</script>
<template>
  <figure class="mx-auto my-auto hidden lg:block">
    <FpImage class="z-10 lg:w-60" :src="path" :alt="$t(alt)" />
    <figcaption
      class="mt-2 text-center text-xs dark:text-fp-gray-dark lg:mt-6 text-gray-600"
      v-if="caption"
    >
      {{ caption }}
    </figcaption>
  </figure>
</template>
