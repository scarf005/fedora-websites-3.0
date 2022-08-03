<script setup>
defineProps({
  background: String,
});
</script>

<template>
  <div
    :style="{
      backgroundImage: `url(${
        $config.app.baseURL + '/' + background.replace('nuxt-site/public/', '')
      })`,
    }"
    class="pt-6 pb-30 bg-cover"
  >
    <slot />
    <div
      class="bg-white -rotate-6 h-72 absolute z-0 -bottom-40 sm:bottom-0"
      style="width: 110%"
    ></div>
  </div>
</template>
