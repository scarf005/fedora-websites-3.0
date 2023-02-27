<script setup>
// Action? -> pass in function on what to happen once it is toggled
// Label?
defineProps({
  url: String,
  color: [String, Array],
});
</script>

<template>
  <label class="relative inline-flex cursor-pointer items-center">
    <input
      type="checkbox"
      value=""
      class="peer sr-only"
      @click="$emit('switchToggled')"
    />
    <div class="fp-switch peer"></div>
  </label>
</template>

<style>
.fp-switch {
  @apply h-6 w-11 rounded-full bg-fp-gray-200 after:absolute after:top-[2px] after:left-[2px] after:h-5 after:w-5 after:rounded-full after:border after:border-gray-300 after:bg-white after:transition-all after:content-[''] peer-checked:bg-fp-newblue peer-checked:after:translate-x-full peer-checked:after:border-white peer-focus:outline-none peer-focus:ring-4 peer-focus:ring-blue-300 dark:border-gray-600 dark:bg-gray-700 dark:peer-focus:ring-blue-800;
}
</style>
