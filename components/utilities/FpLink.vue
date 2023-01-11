<script setup>
defineProps({
  href: String,
  current: Boolean,
  class: String,
});
</script>

<template>
  <NuxtLink
    :href="href"
    :aria-current="current ? 'page' : undefined"
    :class="class"
  >
    <slot></slot>
  </NuxtLink>
</template>
