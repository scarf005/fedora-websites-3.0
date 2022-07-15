<script setup>
defineProps = {
  url: String,
};
</script>
<template>
  <router-link :to="url">
    <slot></slot>
  </router-link>
</template>
