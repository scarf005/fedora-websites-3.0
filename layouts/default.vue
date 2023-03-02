<script setup>
useHead({
  viewport: "width=device-width, initial-scale=1, maximum-scale=1",
  charset: "utf-8",
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
  <div id="app">
    <TheNav />
    <div class="pt-12">
      <slot />
    </div>
    <TheFooter />
  </div>
</template>

<style>
body {
  @apply dark:bg-neutral-700 dark:text-white;
}
.markdown a {
  text-decoration: underline;
  text-underline-offset: 0.15em;
  font-weight: bold;
}
</style>
