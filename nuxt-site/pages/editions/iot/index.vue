<script setup>
  // pull data from the content directory like this
  const { data } = await useAsyncData('page-data', () => {
    return queryContent("pages/editions/iot/home").find()
  })
</script>
<template>
  <main>
    <FpHero
      :title="data[0].header.title"
      :subtitle="data[0].header.subtitle"
      :image="data[0].header.images.image"
      :background="data[0].header.images.backgroundImage"
    />
  </main>
</template>