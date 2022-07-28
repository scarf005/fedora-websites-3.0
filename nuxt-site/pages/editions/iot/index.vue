<script setup>
// pull data from the content directory like this
const { data } = await useAsyncData('page-data', () => {
  return queryContent("editions/iot/").find()
})
</script>
<template>
  <!-- add content to the page like this -->
  <main>
    <p>{{ data[0].title }}</p>
    <img :src="`${$config.app.baseURL + data[0].heroImage}`" :alt="data[0].name" class="mt-8" />
  </main>
</template>
