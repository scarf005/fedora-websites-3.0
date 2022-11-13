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
      href: "https://getfedora.org/static/images/favicon.ico",
    },
  ],
});
</script>

<template>
  <div id="app" class="dark:bg-neutral-700 dark:text-white">
    <TheNavBar />
    <div class="pt-12">
      <NuxtPage />
    </div>
    <TheFooter />
  </div>
</template>
