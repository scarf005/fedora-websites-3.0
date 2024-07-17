<script setup>
defineProps({
  description: {
    type: String,
  },
});
</script>
<template>
  <div class="container mx-auto max-w-7xl">
    <div class="p-2">
      <ContentRenderer
        class="markdown text-center dark:text-white"
        tag="div"
        v-if="description"
        :value="description"
      />
    </div>
  </div>
</template>
