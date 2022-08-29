<script setup>
defineProps({
  title: String,
  subtitle: String,
  image: String,
  color: String,
  border: String,
  background: String,
  cta1: String,
  link1: String,
  cta2: String,
  link2: String,
});
</script>
<template>
  <div class="mt-16 mx-auto max-w-7xl px-4 sm:mt-24 sm:px-6 text-center">
    <h1 class="text-6xl tracking-tight text-white">
      <span class="block">{{ title }}</span>
    </h1>
    <p class="mt-3 mx-auto text-3xl text-white">
      {{ subtitle }}
    </p>
  </div>
  <div class="flex justify-center my-5">
    <FpImage :image="image" />
  </div>
  <div class="mt-5 flex px-4 justify-center">
    <a :href="link1" class="flex flex-1 justify-end">
      <button class="mx-2 shadow sm:px-12 sm:py-4 z-10" :class="background">
        {{ cta1 }}
      </button>
    </a>
    <a :href="link2" class="flex-1">
      <button
        class="mx-2 shadow bg-white border sm:px-12 sm:py-4 z-10"
        :class="[color, border]"
      >
        <!-- <font-awesome-icon icon="fa-brands fa-youtube" /> -->
        {{ cta2 }}
      </button>
    </a>
  </div>
  <div class="mt-5 flex justify-center px-4">
    <a class="mx-2 px-12 py-4 z-10 cursor-pointer font-semibold" :class="color">
      Watch the latest reviews ➔
    </a>
  </div>
</template>
