<script setup>
// pull data from the content directory like this
const { data } = await useAsyncData('page-data', () => {
  return queryContent("editions/workstation/").find()
})
</script>
<template>
  <!-- add content to the page like this -->
  <main>
    <p>{{ data[0].title }}</p>
    <!--    <img :src="`${data[0].hero.image}`" alt="We need to clean up this path issue" class="mt-8" /> -->
  </main>
</template>
