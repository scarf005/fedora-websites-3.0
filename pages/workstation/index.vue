<script setup>
const data = await getCMS("editions/workstation/home");
useContentHead(data);
</script>
<template>
  <FpHero :background="data.header_images[1].image" alignment="bg-bottom">
    <TheLocalBar
      image="assets/images/fedora-workstation-logo.png"
      home="/workstation"
      :items="[
        { name: 'Download', link: '/workstation/download' },
        { name: 'Community', link: '/workstation/community' },
      ]"
    />
    <FpBanner
      :title="data.title"
      :subtitle="data.description"
      :ctas="data.links"
      color="text-fp-green"
      border="border border-fp-green"
      background="text-white bg-fp-green"
      icon="youtube"
    >
      <div class="hero-laptop-container">
        <div class="px-auto mb-48 max-w-sm sm:max-w-xl">
          <FpImage
            class="w-full"
            src="assets/images/workstation_framework.png"
          />
        </div>
      </div>
    </FpBanner>
  </FpHero>

  <main>
    <!-- Why Fedora Workstation -->
    <div class="py-6 px-2 dark:bg-neutral-800">
      <section>
        <header
          class="mx-auto grid max-w-screen-xl gap-4 p-2 text-center md:grid-cols-2 md:p-0 md:text-left"
        >
          <h3
            class="mb-4 font-medium text-fp-blue md:col-span-2 xl:col-span-1 xl:mb-6"
          >
            {{ $t(data.sections[0].sectionTitle) }}
          </h3>
        </header>
        <FpList columns="sm:grid-cols-2 gap-12 lg:gap-4">
          <FpListItem v-for="item in data.sections[0].content" v-bind="item" />
        </FpList>
      </section>
    </div>
    <!-- Benefits Section -->
    <section class="mt-32">
      <h2
        class="mb-12 bg-gradient-to-r from-fp-green to-fp-blue-light bg-clip-text text-center text-5xl font-bold text-transparent"
      >
        {{ $t(data.sections[1].sectionTitle) }}
      </h2>
      <FpBenefit
        v-for="item in data.sections[1].content"
        v-bind="item"
        columns="2"
      />
    </section>

    <!-- Developers Section -->
    <section>
      <h2
        class="mb-12 bg-gradient-to-r from-fp-green to-fp-blue-light bg-clip-text text-center text-5xl font-bold text-transparent"
      >
        {{ $t(data.sections[2].sectionTitle) }}
      </h2>
      <div class="mx-auto mb-12 max-w-7xl">
        <FpBenefit
          v-for="item in data.sections[2].content"
          v-bind="item"
          columns="4"
        />
      </div>
    </section>

    <!-- Get Started Developing Section -->
    <section
      class="mx-auto mb-10 max-w-7xl rounded-xl bg-gradient-to-r from-green-200 to-blue-100 dark:from-black dark:to-slate-800"
    >
      <div class="p-2 sm:p-10">
        <h3 class="mb-8 text-center font-bold text-fp-blue dark:text-gray-100">
          {{ $t(data.sections[3].sectionTitle) }}
        </h3>
        <FpList columns="sm:grid-cols-3 gap-12 lg:gap-4" :disableDots="true">
          <FpListItem
            v-for="item in data.sections[3].content"
            v-bind="item"
            :images="true"
            buttons="true"
          />
        </FpList>
      </div>
    </section>

    <!-- Community Section -->
    <section class="max-w-full dark:bg-neutral-900">
      <FpCommunity :data="data.sections[4]" class="dark:!bg-none" />
    </section>

    <!-- Call To Action -->
    <section class="dark:bg-black">
      <FpCallToAction
        :cta="data.links"
        image="assets/images/workstation_logo.png"
      />
    </section>
  </main>
</template>
