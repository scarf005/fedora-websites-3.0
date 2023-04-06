<script setup>
defineProps({
  href: String,
  current: Boolean,
  class: String,
  rel: String,
});
const localePath = useLocalePath();
</script>

<template>
  <a
    :href="`${
      href.includes('https')
        ? href
        : $config.app.baseURL.replace(new RegExp('/$'), '') + localePath(href)
    }`"
    :aria-current="current ? 'page' : undefined"
    :rel="rel"
    :class="class"
  >
    <slot></slot>
  </a>
</template>
