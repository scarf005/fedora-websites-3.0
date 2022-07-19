<script setup>
defineProps({
  url: String,
});
</script>

<template>
  <a :href="url" class="">
    <slot></slot>
  </a>
</template>
