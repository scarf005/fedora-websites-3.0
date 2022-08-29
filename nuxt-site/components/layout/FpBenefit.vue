<script setup>
defineProps({
  image: Object,
  title: String,
  description: String,
});
</script>

<template>
  <div class="grid grid-cols-1 md:grid-cols-2 w-10/12 mx-auto">
    <div class="col-span-1 p-5">
      <img
        class="z-10"
        :src="`${
          $config.app.baseURL + '/' + image.image.replace('nuxt-site/public/', '')
        }`"
        alt="Screenshot"
      />
    </div>
    <div class="col-span-1 text-left flex flex-col justify-center p-5">
      <h2 class="mb-5 font-bold">{{ title }}</h2>
      <p>
        {{ description }}
      </p>
    </div>
  </div>
</template>
