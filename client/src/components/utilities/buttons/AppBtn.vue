<script setup>
defineProps({
  url: String,
});
</script>

<template>
  <a :href="url" class="btn">
    <slot></slot>
  </a>
</template>

<style lang="postcss">
.btn {
  @apply font-medium bg-blue-light hover: bg-blue-light/[0.6] ease-in-out duration-300 hover:ease-in-out max-w-fit rounded py-2 px-4 lg:py-3 lg:px-6;
}
</style>