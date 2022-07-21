<script setup>
useHead({
  title: "The Fedora Project",
  viewport: "width=device-width, initial-scale=1, maximum-scale=1",
  charset: "utf-8",
  meta: [
    {
      name: "description",
      content: "Fedora Linux is an open source project. ",
    },
  ],
  link: [
    {
      rel: "icon",
      href: "/favicon.ico",
    },
  ],
});
</script>

<template>
  <div id="app">
    <the-nav-bar />
    <nuxt-page />
    <the-footer />
  </div>
</template>
