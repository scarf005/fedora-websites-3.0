<script setup>
defineProps({
  image: Object,
  title: String,
  description: String,
  columns: String
});
</script>

<template>
  <div class="grid grid-cols-1 w-10/12 mx-auto mt-8" :class="`md:grid-cols-${columns}`">
    <div class="col-span-1 p-1 sm:p-5">
      <FpImage :image="image.image"/>
    </div>
    <div class="col-span-1 text-left flex flex-col justify-center p-1 sm:p-5 text-center sm:text-start">
      <h2 class="mb-5 font-bold text-gray-700 max-w-md">{{ title }}</h2>
      <p class="font-normal text-gray-600 max-w-md">
        {{ description }}
      </p>
    </div>
  </div>
</template>
