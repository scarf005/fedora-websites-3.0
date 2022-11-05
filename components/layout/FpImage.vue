<script setup>
defineProps({
  image: String,
});
</script>

<template>
  <nuxt-img
    class="z-10"
    :src="`${$config.app.baseURL + '/' + image.replace('public/', '')}`"
    alt="Screenshot"
  />
</template>
