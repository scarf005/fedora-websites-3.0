<script setup>
defineProps({
  columns: String,
  disableDots: Boolean,
});
</script>

<template>
  <ul
    class="mx-auto grid max-w-screen-xl place-items-center p-2 md:p-0"
    :class="`${columns} ${
      disableDots
        ? 'list-none'
        : 'list-outside marker:text-4xl marker:text-fp-blue-light'
    }`"
  >
    <slot></slot>
  </ul>
</template>
