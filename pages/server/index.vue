<script setup>
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

  <!-- Benefits Section -->
  <section class="pt-32 dark:bg-neutral-900">
    <h2
      class="mb-12 bg-gradient-to-r from-fp-green to-fp-orange bg-clip-text text-center text-5xl font-bold text-transparent"
    >
      {{ $t(data.sections[0].sectionTitle) }}
    </h2>
    <FpBenefit
      v-for="item in data.sections[0].content"
      v-bind="item"
      columns="2"
    />
  </section>

  <!-- Community Section -->
  <section class="max-w-full dark:bg-neutral-800">
    <FpCommunity :data="data.sections[1]" class="dark:!bg-none" />
  </section>

  <!-- Call To Action -->
  <section class="dark:bg-black">
    <FpCallToAction
      :cta="data.links"
      image="assets/images/fedora-server-logo.png"
    />
  </section>
</template>
