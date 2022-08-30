<script setup>
defineProps({
  background: String,
  alignment: String
});
</script>

<template>
  <div
    :style="{
      backgroundImage: `url(${
        $config.app.baseURL + '/' + background.replace('public/', '')
      })`,
    }"
    style="min-height: 60vh"
    :class="[alignment, 'pt-6 pb-30 bg-cover']"
  >
    <slot />
  </div>
</template>
