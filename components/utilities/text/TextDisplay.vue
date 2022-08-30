<script setup>
// NOTE: This may not be able to be a single component

// TODO: Have a keyword to differentiate between h1, h2, and h3
// TODO: Use another keyword to differentiate between the different types of gradients
// TODO: Style should default to center
</script>
<template>
  <h3 v-if="keyword">
    <slot></slot>
  </h3>
  <h2 v-else-if="keyword2">
    <slot></slot>
  </h2>
  <h1 v-else>
    <slot></slot>
  </h1>
</template>
