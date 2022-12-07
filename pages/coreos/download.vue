<script setup>
const { data } = await useAsyncData("page-data", () => {
  return queryContent("/editions/coreos/download").find();
});
</script>
<template>
  <p>{{ data }}</p>
</template>
