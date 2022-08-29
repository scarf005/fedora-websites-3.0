<script setup>
defineProps({
  columns: String,
});
</script>

<template>
  <ul
    class="mx-10 sm:mx-8 list-outside marker:text-blue-light marker:text-4xl grid place-items-center" :class="columns">
    <slot></slot>
  </ul>
</template>
