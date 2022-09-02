<script setup>
defineProps({
  image: Object,
  title: String,
  description: String,
});
</script>

<template>
  <div class="grid grid-cols-1 md:grid-cols-2 w-10/12 mx-auto mt-8">
    <div class="col-span-1 p-1 sm:p-5">
      <img
        class="z-10"
        :src="`${
          $config.app.baseURL + '/' + image.image.replace('public/', '')
        }`"
        alt="Screenshot"
      />
    </div>
    <div class="col-span-1 text-left flex flex-col justify-center p-1 sm:p-5 text-center sm:text-start">
      <h2 class="mb-5 font-bold text-gray-700 max-w-md">{{ title }}</h2>
      <p class="font-normal text-gray-600 max-w-md">
        {{ description }}
      </p>
    </div>
  </div>
</template>
