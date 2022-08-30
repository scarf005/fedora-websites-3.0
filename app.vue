<script setup>
const base = process.env.CI_PAGES_URL
  ? new URL(process.env.CI_PAGES_URL).pathname
  : "";

useHead({
  viewport: "width=device-width, initial-scale=1, maximum-scale=1",
  charset: "utf-8",
  meta: [
    {
      name: "description",
      content: "Fedora Linux is an open source project.",
    },
  ],
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
    <the-nav-bar />
    <div class="pt-12">
      <nuxt-page />
    </div>
    <the-footer />
  </div>
</template>
