<script setup>
const { locale } = useI18n();
const data = await getCMS("editions/server/home");
useContentHead(data);
</script>
<template>
  <FpHero :background="data.header_images[1].image" alignment="bg-bottom">
    <TheLocalBar
      image="assets/images/fedora_white.png"
      home="/server"
      :items="[
        { name: 'Download', link: '/server/download' },
        { name: 'Community', link: '/server/community' },
      ]"
    />
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
