<script setup>
const base = "";

useHead({
  viewport: "width=device-width, initial-scale=1, maximum-scale=1",
  charset: "utf-8",
  meta: [],
  link: [
    {
      rel: "icon",
      type: "image/x-icon",
      href: base + "/favicon.ico",
    },
  ],
});
</script>

<template>
  <div id="app">
    <TheNavBar />
    <div class="pt-12">
      <slot />
    </div>
    <TheFooter />
  </div>
</template>
