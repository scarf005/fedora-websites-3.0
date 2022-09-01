<script setup>
const { data } = await useAsyncData("page-data", () => {
  return queryContent("/pages/editions/server/home").find();
});
useHead({
  title: "Fedora Server | The Fedora Project",
});
</script>
<template>
  <FpHero :background="data[0].header.images.backgroundImage" alignment="bg-bottom">
    <FpBanner
      :title="data[0].header.title"
      :subtitle="data[0].header.subtitle"
      :image="data[0].header.images.image"
      color="text-fp-blue"
      border="border border-fp-blue"
      background="text-white bg-fp-blue"
      :cta1="data[0].header.cta[0].text"
      :link1="data[0].header.cta[0].url"
    />
  </FpHero>
</template>
