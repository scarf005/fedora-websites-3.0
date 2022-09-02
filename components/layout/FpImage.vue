<script setup>
defineProps({
  image: String,
});
</script>

<template>
  <img
    class="z-10"
    :src="`${$config.app.baseURL + '/' + image.replace('public/', '')}`"
    alt="Screenshot"
  />
</template>
