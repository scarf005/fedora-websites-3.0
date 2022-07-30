<script setup>
const { data } = await useAsyncData('page-data', () => {
  return queryContent("/pages/editions/workstation/home").find()
})

</script>
<template>
  <p>{{ data }}</p>
</template>
