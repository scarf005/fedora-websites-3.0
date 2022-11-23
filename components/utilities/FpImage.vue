<script setup>
defineProps({
  src: String,
});
</script>

<template>
  <img
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
