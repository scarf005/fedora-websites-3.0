<script setup>
defineProps({
  url: String,
});
</script>

<template>
  <a :href="url" class="bg-blue-light hover:bg-blue-light/[0.6] ease-in-out">
    <slot></slot>
  </a>
</template>

