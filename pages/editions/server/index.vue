<script setup>
const { locale } = useI18n();
const { data } = await useAsyncData("page-data", () => {
  return queryContent()
    .where({ _path: "/pages/editions/server/home/." + locale._value })
    .find();
});
useHead({
  title: data._value[0].title + " | The Fedora Project",
});
</script>
<template>
  <FpHero
    :background="data[0].header.images.backgroundImage"
    alignment="bg-bottom"
  >
    <FpBanner
      :title="data[0].header.title"
      :subtitle="data[0].header.subtitle"
      color="text-fp-blue"
      border="border border-fp-blue"
      background="text-white bg-fp-blue"
      :ctas="data[0].header.cta"
    >
      <FpImage :image="data[0].header.images.image" />
    </FpBanner>
  </FpHero>
</template>
