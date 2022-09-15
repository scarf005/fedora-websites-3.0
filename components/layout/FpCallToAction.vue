<script setup>
defineProps({
  cta: Array,
});
</script>
<template>
  <div class="flex flex-col justify-center items-center h-96">
    <FpImage image="assets/images/workstation_logo.jpg" class="max-w-sm" />
    <p class="text-center text-2xl text-gray-500 p-10">Try it now.</p>
    <FpBtn :url="cta[0].url">Get Started</FpBtn>
  </div>
</template>
