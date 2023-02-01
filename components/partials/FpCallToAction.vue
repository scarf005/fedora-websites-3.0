<script setup>
defineProps({
  cta: Array,
  image: String,
});
</script>
<template>
  <div class="flex h-96 flex-col items-center justify-center">
    <FpImage :src="image" class="max-w-sm" />
    <p class="p-10 text-center text-2xl text-gray-500 dark:text-gray-300">
      {{ $t("Try it now.") }}
    </p>
    <FpBtn :href="cta[0].url">{{ $t("Get Started") }}</FpBtn>
  </div>
</template>
