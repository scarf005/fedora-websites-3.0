<script setup>
const { data } = await useAsyncData("page-data", () => {
  return queryContent("/pages/editions/server/home").find();
});
useHead({
  title: "Fedora Server | The Fedora Project",
});
</script>
<template>
  <p>{{ data }}</p>
</template>
