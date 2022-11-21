<script setup>
defineProps({
  src: String,
});
</script>
<template>
  <FpImage class="mx-auto mb-4 max-h-[100px]" :src="src" />
</template>
