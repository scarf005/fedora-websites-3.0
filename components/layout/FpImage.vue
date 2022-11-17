<script setup>
defineProps({
  image: String,
});
</script>

<template>
  <img
    class="z-10"
    :src="`${
      $config.app.baseURL.replace(new RegExp('/$'), '') +
      '/' +
      image.replace('public/', '')
    }`"
    :alt="`${
      $config.app.baseURL.replace(new RegExp('/$'), '') +
      '/' +
      image.replace('public', '')
    }`"
  />
</template>
