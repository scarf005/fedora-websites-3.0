<script setup>
defineProps({
  image: Object,
  title: String,
  description: String,
  columns: String
});
</script>

<template>
  <div :class="`grid grid-cols-1 w-10/12 mx-auto mt-8 md:grid-cols-${columns}`">
    <div class="col-span-1 p-1 sm:p-5">
      <FpImage :image="image.image"/>
    </div>
    <div :class="`col-span-${columns - 1} text-left flex flex-col justify-center p-1 sm:p-5 text-center sm:text-start`">
      <h2 class="mb-5 font-bold text-gray-700">{{ title }}</h2>
      <p class="font-normal text-gray-600">
        {{ description }}
      </p>
    </div>
  </div>
</template>
