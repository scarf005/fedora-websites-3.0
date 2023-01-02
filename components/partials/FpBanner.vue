<script setup>
import FpBtn from "../utilities/FpBtn.vue";
defineProps({
  logo: String,
  title: String,
  subtitle: String,
  subtitleStyle: {
    color: String,
    isBold: Boolean,
  },
  reviewUrl: String,
  color: String,
  border: String,
  background: String,
  ctas: Array,
  icon: String,
});
</script>
<template>
  <div class="mx-auto mt-16 max-w-7xl px-4 text-center sm:mt-24 sm:px-6">
    <div class="mx-auto max-w-sm sm:max-w-xl">
      <FpImage v-if="logo" class="z-10" :src="logo" alt="logo" />
    </div>
    <h1 v-if="title" class="font-semibold text-white">
      <span class="block">{{ $t(title) }}</span>
    </h1>
    <h2
      v-if="subtitle"
      class="mt-3"
      :class="[
        'text-' + (subtitleStyle?.color || 'white'),
        { 'font-semibold': subtitleStyle?.isBold },
      ]"
    >
      {{ $t(subtitle) }}
    </h2>
  </div>
  <div class="my-5 flex justify-center">
    <slot />
  </div>
  <div class="spacing-1 mt-5 flex justify-center">
    <template v-for="(cta, idx) in ctas">
      <FpBtn
        :url="cta.url"
        :color="[
          'text-center',
          {
            [background]: idx == 0,
            [color]: idx > 0,
            [border]: idx > 0,
            'bg-white': idx > 0,
          },
        ]"
      >
        <Icon v-if="idx === 1 && icon" :name="`fa6-brands:${icon}`" />
        {{ $t(cta.text) }}
      </FpBtn>
      <div v-if="idx < ctas.length - 1" class="w-2" />
    </template>
  </div>
  <div class="mt-5 flex justify-center px-4">
    <a
      v-if="reviewUrl"
      class="z-10 mx-2 cursor-pointer px-12 py-4 font-semibold"
      :class="color"
    >
      {{ $t("Watch the latest reviews ➔") }}
    </a>
  </div>
</template>
