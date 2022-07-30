<script setup>
const { data } = await useAsyncData('page-data', () => {
  return queryContent("/pages/editions/server/download").find()
})


</script>
<template>
  <p>{{ data }}</p>
</template>