<script setup>
defineProps({
  cta: Array,
});
</script>
<template>
  <div class="flex h-96 flex-col items-center justify-center">
    <FpImage image="assets/images/workstation_logo.jpg" class="max-w-sm" />
    <p class="p-10 text-center text-2xl text-gray-500">Try it now.</p>
    <FpBtn :url="cta[0].url">Get Started</FpBtn>
  </div>
</template>
