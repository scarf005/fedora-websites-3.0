<script setup>
defineProps({
  image: Object,
  title: String,
  description: String,
  columns: String,
});
</script>

<template>
  <div :class="`mx-auto mt-8 grid w-10/12 grid-cols-1 md:grid-cols-${columns}`">
    <div class="col-span-1 p-1 sm:p-5">
      <FpImage :image="image.image" />
    </div>
    <div
      :class="`col-span-${
        columns - 1
      } flex flex-col justify-center p-1 text-left text-center sm:p-5 sm:text-start`"
    >
      <h2 class="mb-5 font-bold text-gray-700">{{ title }}</h2>
      <p class="font-normal text-gray-600">
        {{ description }}
      </p>
    </div>
  </div>
</template>
