<script setup>
defineProps({
  url: String,
});
</script>

<template>
  <a :href="url">
    <slot></slot>
  </a>
</template>
