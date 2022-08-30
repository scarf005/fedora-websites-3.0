<script setup>
defineProps({
  background: String,
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
    class="pt-6 pb-30 bg-cover bg-bottom"
  >
    <slot />
  </div>
</template>
