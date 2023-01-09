<script setup>
defineProps({});

// Data Import
let { data } = await useAsyncData(() => {
  return queryContent("/partials/compliance").findOne();
});
</script>
<template>
  <div class="container mx-auto max-w-7xl">
    <div class="p-2">
      <h2 class="mb-5 text-center text-base text-white">
        {{ $t(data.title) }}
      </h2>
      <p class="text-sm text-fp-gray">
        {{ $t(data.description) }}
      </p>
    </div>
  </div>
</template>
