<script setup>
defineProps({
  columns: String,
  disableDots: Boolean,
});
</script>

<template>
  <ul
    class="mx-10 sm:mx-8 grid place-items-center"
    :class="`${columns} ${
      disableDots ? 'list-none' : 'list-outside marker:text-fp-blue-light marker:text-4xl'
    }`"
  >
    <slot></slot>
  </ul>
</template>
