<script setup>
const { locale } = useI18n();
let { data } = await useAsyncData("page-data", () => {
  return queryContent(
    "/pages/editions/server/home/." + locale._value
  ).findOne();
});

if (data._value === null) {
  ({ data } = await useAsyncData("page-data-fallback", () => {
    return queryContent("/pages/editions/server/home/").findOne();
  }));
}
useHead({
  title: data._value.title + " | The Fedora Project",
  meta: [
    {
      name: "description",
      content: data._value.description,
    },
  ],
});
</script>
<template>
  <FpHero
    :background="data.header.images.backgroundImage"
    alignment="bg-bottom"
  >
    <FpBanner
      :title="data.header.title"
      :subtitle="data.header.subtitle"
      color="text-fp-blue"
      border="border border-fp-blue"
      background="text-white bg-fp-blue"
      :ctas="data.header.cta"
    >
      <FpImage :image="data.header.images.image" />
    </FpBanner>
  </FpHero>
</template>
