<script setup>
const { locale } = useI18n();
let { data } = await useAsyncData("page-data", () => {
  return queryContent("/editions/server/home." + locale._value).findOne();
});

if (data._value === null) {
  ({ data } = await useAsyncData("page-data-fallback", () => {
    return queryContent("/editions/server/home").sort().find();
  }));
  data._value = data._value[data._value.length - 1];
}
useContentHead(data);
</script>
<template>
  <FpHero :background="data.header_images[1].image" alignment="bg-bottom">
    <FpBanner
      :title="data.title"
      :subtitle="data.description"
      color="text-fp-blue"
      border="border border-fp-blue"
      background="text-white bg-fp-blue"
      :ctas="data.links"
    >
      <FpImage :src="data.header_images[0].image" />
    </FpBanner>
  </FpHero>
</template>
