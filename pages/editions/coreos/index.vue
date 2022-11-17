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
  <!-- Hero Section -->
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
      color="text-fp-magenta"
      border="border border-fp-magenta"
      background="text-white bg-fp-magenta"
      :ctas="data.links"
      icon="youtube"
    >
      <FpImage :image="data.header_images[0].image" />
    </FpBanner>
  </FpHero>

  <!-- Why Section -->
  <FpHero :background="data.sections[0].images" alignment="bg-bottom">
    <section class="mx-auto w-10/12 pt-12">
      <h3
        class="mb-4 font-medium text-fp-magenta md:col-span-2 xl:col-span-1 xl:mb-6"
      >
        {{ data.sections[0].sectionTitle }}
      </h3>
      <FpList columns="sm:grid-cols-2 gap-12 lg:gap-4">
        <FpListItem v-for="item in data.sections[0].content" v-bind="item" />
      </FpList>
    </section>
  </FpHero>

  <!-- Platforms Section -->
  <div class="bg-magenta-100" style="min-height: 60vh">
    <section class="mx-auto w-10/12 pt-12">
      <h3
        class="mb-4 text-center font-medium text-fp-blue md:col-span-2 xl:col-span-1 xl:mb-6"
      >
        {{ data.sections[1].sectionTitle }}
      </h3>
      <FpList columns="sm:grid-cols-4 gap-12 lg:gap-4" :disableDots="true">
        <FpListItem
          v-for="item in data.sections[1].content"
          v-bind="item"
          images="true"
        />
      </FpList>
    </section>
  </div>

  <!-- Community Section -->
  <section>
    <FpCommunity :data="data.sections[2]" />
  </section>

  <!-- Call To Action -->
  <section>
    <FpCallToAction :cta="data.links" image="assets/images/coreos_logo.jpg" />
  </section>
</template>
