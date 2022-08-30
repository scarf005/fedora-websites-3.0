<script setup>
defineProps({
  url: String,
  color: String,
});
</script>

<template>
  <a
    :href="url"
    class="font-medium cursor-pointer ease-in-out duration-300 hover:ease-in-out max-w-fit rounded py-2 px-4 lg:py-3 lg:px-6 ease-in-out"
    :class="color || 'text-white  bg-fp-blue-light hover:bg-fp-blue-light/[0.6]'"
  >
    <slot></slot>
  </a>
</template>
