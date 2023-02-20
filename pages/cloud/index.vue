<script setup>
const data = await getCMS("editions/cloud/home");
useContentHead(data);
</script>

<template>
  <!-- Hero Section -->
  <FpHero :background="data.header_images[1].image" alignment="bg-bottom">
    <TheLocalBar
      image="assets/images/fedora-cloud-logo.png"
      home="/cloud"
      :items="[
        { name: 'Download', link: '/cloud/download' },
        { name: 'Community', link: '/cloud/community' },
      ]"
    />

    <FpBanner
      :title="data.title"
      :subtitle="data.description"
      color="text-fp-blue"
      border="border border-fp-blue"
      background="text-white bg-fp-blue"
      :ctas="data.links"
      icon="youtube"
    >
      <FpImage :src="data.header_images[0].image" />
    </FpBanner>
  </FpHero>

  <!-- Why Section -->
  <FpHero :background="data.sections[0].images" alignment="bg-bottom">
    <section class="mx-auto max-w-screen-xl p-2 pt-12 md:p-0">
      <h3
        class="mb-4 font-medium text-fp-blue md:col-span-2 xl:col-span-1 xl:mb-6"
      >
        {{ $t(data.sections[0].sectionTitle) }}
      </h3>
      <FpList columns="sm:grid-cols-2 gap-12 lg:gap-4">
        <FpListItem v-for="item in data.sections[0].content" v-bind="item" />
      </FpList>
    </section>
  </FpHero>

  <!-- Platforms Section -->
  <div class="bg-default-100" style="min-height: 60vh">
    <section class="mx-auto w-10/12 pt-12">
      <h3
        class="mb-4 text-center font-medium text-fp-blue md:col-span-2 xl:col-span-1 xl:mb-6"
      >
        {{ $t(data.sections[1].sectionTitle) }}
      </h3>
      <FpList columns="sm:grid-cols-3 gap-12 lg:gap-4" :disableDots="true">
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
    <FpCallToAction :cta="data.links" image="assets/images/cloud_logo.png" />
  </section>
</template>
