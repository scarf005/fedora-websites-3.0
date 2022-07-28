<script setup>
const { data } = await useAsyncData('page-data', () => {
  return queryContent("editions/workstation/").find()
})
</script>
<template>
  <main>
    <h1>{{ data[0].title }}</h1>
  </main>
</template>
