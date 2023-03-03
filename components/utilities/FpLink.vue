<script setup>
defineProps({
  href: String,
  current: Boolean,
  class: String,
});
const localePath = useLocalePath();
</script>

<template>
  <a
    :href="`${
      href.includes('https')
        ? href
        : localePath($config.app.baseURL.replace(new RegExp('/$'), '') + href)
    }`"
    :aria-current="current ? 'page' : undefined"
    :class="class"
  >
    <slot></slot>
  </a>
</template>
