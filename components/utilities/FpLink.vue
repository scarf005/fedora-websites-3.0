<script setup>
defineProps({
  href: String,
  current: Boolean,
  class: String,
});
const localePath = useLocalePath();
</script>

<template>
  <NuxtLink
    :href="localePath(href)"
    :aria-current="current ? 'page' : undefined"
    :class="class"
  >
    <slot></slot>
  </NuxtLink>
</template>
