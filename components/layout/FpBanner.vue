<script setup>
import FpBtn from "../utilities/FpBtn.vue";
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
    <h1 class="text-white font-semibold">
      <span class="block">{{ title }}</span>
    </h1>
    <h2 class="text-white mt-3">
      {{ subtitle }}
    </h2>
  </div>
  <div class="flex justify-center my-5">
    <FpImage :image="image" />
  </div>
  <div class="mt-5 flex justify-center spacing-1">
    <FpBtn :url="link1" :color="[background, 'text-center']">
      {{ cta1 }}
    </FpBtn>
    <div class="w-2"/>
    <FpBtn :url="link2" :color="[color, border, 'text-center bg-white']">
      <!-- <font-awesome-icon icon="fa-brands fa-youtube" /> -->
      {{ cta2 }}
    </FpBtn>
  </div>
  <div class="mt-5 flex justify-center px-4">
    <a class="mx-2 px-12 py-4 z-10 cursor-pointer font-semibold" :class="color">
      Watch the latest reviews ➔
    </a>
  </div>
</template>
