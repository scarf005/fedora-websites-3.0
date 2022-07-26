<script setup>
// pull data from the content directory like this
const { data } = await useAsyncData('page-data', () => {
  return queryContent("editions/workstation/").find()
})
</script>
<template>
  <!-- add content to the page like this -->
  <main>
    <h1>{{ data[0].hero.title }}</h1>
    <p>{{ data[0].hero.description }}</p>
    <img :src="`../../../assets/${data[0].hero.image}`" alt="We need to clean up this path issue" class="mt-8" />
  </main>
</template>
