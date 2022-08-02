<script setup>
defineProps({
  title: String,
  image: String,
  background: String,
  subtitle: String,
});
</script>

<template>
  <div
    :style="{
      backgroundImage: `url(${
        $config.app.baseURL + '/' + background.replace('nuxt-site/public/', '')
      })`,
    }"
    class="pt-6 pb-30 bg-cover"
  >
    <div class="mt-16 mx-auto max-w-7xl px-4 sm:mt-24 sm:px-6 text-center">
      <h1 class="text-6xl tracking-tight font-medium text-white">
        <span class="block">{{ title }}</span>
      </h1>
      <p class="mt-3 mx-auto text-3xl text-white">
        {{ subtitle }}
      </p>
    </div>

    <div class="flex justify-center my-5">
      <img
        class="z-10"
        :src="`${
          $config.app.baseURL + '/' + image.replace('nuxt-site/public/', '')
        }`"
        alt="Screenshot"
      />
    </div>

    <div class="mt-5 flex justify-center px-4">
      <button class="mx-2 shadow bg-purple px-12 py-4 z-10">
        Download Now
      </button>
      <button
        class="mx-2 shadow bg-white border border-purple text-purple px-12 py-4 z-10"
      >
        <font-awesome-icon icon="fa-brands fa-youtube" />
        Reviewed by Reviewer
      </button>
    </div>
    <div
      class="bg-white -rotate-6 h-72 absolute z-0 -bottom-40 sm:bottom-0"
      style="width: 110%"
    ></div>
  </div>
</template>