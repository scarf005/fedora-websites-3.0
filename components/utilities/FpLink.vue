<script setup>
defineProps({
  url: String,
  current: Boolean,
});
</script>

<template>
  <a
    :href="`${
      url.includes('https')
        ? url
        : $config.app.baseURL.replace(new RegExp('/$'), '') + url
    }`"
    class="rounded-md px-3 py-4 text-base font-medium text-gray-500 hover:text-fp-purple dark:text-gray-300"
    :aria-current="current ? 'page' : undefined"
  >
    <slot></slot>
  </a>
</template>
