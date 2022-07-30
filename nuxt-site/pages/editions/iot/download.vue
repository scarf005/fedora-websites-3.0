<script setup>
const { data } = await useAsyncData('page-data', () => {
  return queryContent("/pages/iot/download").find()
})

</script>
<template>
  <p>{{ data }}</p>
</template>
