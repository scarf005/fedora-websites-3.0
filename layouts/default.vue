<script setup>
const i18nHead = useLocaleHead({
  addDirAttribute: true,
});
useHead({
  htmlAttrs: {
    dir: i18nHead.value.htmlAttrs.dir || "ltr",
  },
  viewport: "width=device-width, initial-scale=1, maximum-scale=1",
  charset: "utf-8",
  link: [],
});
</script>

<template>
  <div id="app">
    <a
      href="#main"
      class="sr-only !fixed z-50 top-[3px] left-[3px] !h-[48px] leading-[48px] bg-fp-blue-700 !px-6 text-sm text-white focus:not-sr-only"
    >
      Skip to main content
    </a>
    <TheNav />
    <a
      id="main"
      class="sr-only !absolute !w-full !pt-8 focus:not-sr-only"
      href="#main"
      >Start of main content</a
    >
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
.markdown-inline,
.markdown-inline > * {
  display: inline;
}
</style>
