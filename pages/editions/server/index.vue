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
      color="text-fp-green"
      border="border border-fp-green"
      background="text-white bg-fp-green"
      :cta1="data[0].header.cta[0].text"
      :link1="data[0].header.cta[0].url"
    />
  </FpHero>
</template>
