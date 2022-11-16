<script setup>
const { locale } = useI18n();
let { data } = await useAsyncData("page-data", () => {
  return queryContent("/editions/coreos/home." + locale._value).findOne();
});

if (data._value === null) {
  ({ data } = await useAsyncData("page-data-fallback", () => {
    return queryContent("/editions/coreos/home").sort().find();
  }));
  data._value = data._value[data._value.length - 1];
}
useContentHead(data);
</script>

<template>
  <FpHero :background="data.header_images[1].image" alignment="bg-bottom">
    <TheLocalBar
      image="assets/images/fedora-coreos-logo.png"
      :items="[
        { name: 'Download', link: 'download' },
        { name: 'Community', link: 'community' },
        { name: 'Help', link: '#' },
      ]"
    />

    <FpBanner
      :title="data.title"
      :subtitle="data.description"
      color="text-fp-purple"
      border="border border-fp-purple"
      background="text-white bg-fp-purple"
      :ctas="data.links"
      icon="youtube"
    >
      <FpImage :image="data.header_images[0].image" />
    </FpBanner>
  </FpHero>
</template>
