<script setup>
defineProps({
  columns: String,
});
</script>

<template>
  <ul
    class="max-w-screen-xl mx-auto list-outside marker:text-fp-blue-light marker:text-4xl grid place-items-center"
    :class="columns"
  >
    <slot></slot>
  </ul>
</template>
