<script setup>
defineProps({
  image: String,
  altText: String,
});
</script>

<template>
  <img
    class="z-10"
    :src="`${$config.app.baseURL + '/' + image.replace('public/', '')}`"
    :alt="`${$config.app.baseURL + '/' + image}`"
  />
</template>
