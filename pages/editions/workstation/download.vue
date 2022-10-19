<script setup>
const { data } = await useAsyncData("page-data", () => {
  return queryContent("/editions/workstation/download").find();
});
</script>
<template>
  <p>{{ data }}</p>
</template>
