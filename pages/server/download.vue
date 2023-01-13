<script setup>
const data = await getCMS("editions/server/dowload");
</script>
<template>
  <p>{{ data }}</p>
</template>
