<script setup>
const data = await getCMS("editions/coreos/home");
useContentHead(data);
</script>

<template>
  <!-- Hero Section -->
  <FpHero
    :background="data.header_images[1].image"
    alignment="bg-top"
    class="relative z-0"
  >
    <TheLocalBar
      image="assets/images/fedora-coreos-logo.png"
      home="/coreos"
      :items="[
        { name: 'Download', link: '/coreos/download' },
        { name: 'Community', link: '/coreos/community' },
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
      <FpImage :src="data.header_images[0].image" />
    </FpBanner>
    <svg
      viewBox="0 0 1918.6658 172.80759"
      version="1.1"
      xmlns="http://www.w3.org/2000/svg"
      xmlns:svg="http://www.w3.org/2000/svg"
      class="absolute -bottom-2.5 -z-10"
    >
      <g transform="translate(-0.38340506,-449.49539)">
        <path
          class="fill-white dark:fill-neutral-800"
          d="m 0.38340505,456.69538 c 0,0 534.13975495,87.11876 983.48064495,87.11876 449.34085,0 935.18515,-94.31876 935.18515,-94.31876 V 622.303 H 0.38340505 Z"
        />
      </g>
    </svg>
  </FpHero>

  <!-- Why Section -->
  <div class="py-6 px-2 dark:bg-neutral-800">
    <FpHero :background="data.sections[0].images" alignment="bg-bottom">
      <section class="mx-auto max-w-screen-xl p-2 pt-12 md:p-0">
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
  </div>

  <!-- Platforms Section -->
  <div class="bg-magenta-100 dark:bg-neutral-100" style="min-height: 60vh">
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
  <section class="dark:bg-neutral-800">
    <FpCommunity :data="data.sections[2]" class="dark:!bg-none" />
  </section>

  <!-- Call To Action -->
  <section class="dark:bg-black">
    <FpCallToAction :cta="data.links" image="assets/images/coreos_logo.png" />
  </section>
</template>
