<script setup>
const data = await getCMS("editions/iot/download");
</script>
<template>
  <p>{{ data }}</p>
</template>
