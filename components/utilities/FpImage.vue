<script setup>
const props = defineProps({
  src: String,
  darksrc: String,
});
const colorMode = useColorMode();
</script>

<template>
  <img
    class="z-10"
    v-if="colorMode.value == 'dark' && darksrc"
    :src="`${
      $config.app.baseURL.replace(new RegExp('/$'), '') +
      '/' +
      darksrc.replace('public/', '')
    }`"
    :alt="`${
      $config.app.baseURL.replace(new RegExp('/$'), '') +
      '/' +
      darksrc.replace('public', '')
    }`"
  />
  <img
    v-else
    class="z-10"
    :src="`${
      $config.app.baseURL.replace(new RegExp('/$'), '') +
      '/' +
      src.replace('public/', '')
    }`"
    :alt="`${
      $config.app.baseURL.replace(new RegExp('/$'), '') +
      '/' +
      src.replace('public', '')
    }`"
  />
</template>
