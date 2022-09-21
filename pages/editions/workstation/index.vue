<script setup>
const { locale } = useI18n();
let { data } = await useAsyncData("page-data", () => {
  return queryContent(
    "/pages/editions/workstation/home/." + locale._value
  ).findOne();
});

if (data._value === null) {
  ({ data } = await useAsyncData("page-data-fallback", () => {
    return queryContent("/pages/editions/workstation/home/").sort().find();
  }));
  data._value = data._value[data._value.length - 1];
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
      :reviewUrl="data.header.reviewUrl"
      :ctas="data.header.cta"
      color="text-fp-green"
      border="border border-fp-green"
      background="text-white bg-fp-green"
    >
      <div class="hero-laptop-container">
        <div class="px-auto mb-48 max-w-sm sm:max-w-xl">
          <FpImage
            class="w-full"
            image="assets/images/workstation_framework.png"
          />
          <video
            class="-mt-[310px] w-full px-11 sm:-mt-[473px] sm:px-[70px]"
            autoplay=""
            loop=""
            muted=""
            playsinline=""
            preload="auto"
          >
            <source src="/assets/images/hero.mp4" type="video/mp4" />
          </video>
        </div>
      </div>
    </FpBanner>
  </FpHero>

  <main class="mt-8 flex flex-col items-center">
    <!-- Why Fedora Workstation -->
    <section class="w-10/12">
      <header
        class="mx-auto grid gap-4 text-center md:w-11/12 md:grid-cols-2 md:text-left"
      >
        <h3
          class="mb-4 font-medium text-fp-blue md:col-span-2 xl:col-span-1 xl:mb-6"
        >
          {{ data.section[0].header.sectionTitle }}
        </h3>
      </header>
      <FpList columns="sm:grid-cols-2 gap-12 lg:gap-4">
        <FpListItem
          v-for="item in data.section[0].content.list"
          v-bind="item"
        />
      </FpList>
    </section>

    <!-- Benefits Section -->
    <section class="mt-32">
      <h2
        class="mb-12 bg-gradient-to-r from-fp-green to-fp-blue-light bg-clip-text text-center text-5xl font-bold text-transparent"
      >
        {{ data.section[1].header.sectionTitle }}
      </h2>
      <FpBenefit
        v-for="item in data.section[1].content.list"
        v-bind="item"
        columns="2"
      />
    </section>

    <!-- Developers Section -->
    <section>
      <h2
        class="mb-12 bg-gradient-to-r from-fp-green to-fp-blue-light bg-clip-text text-center text-5xl font-bold text-transparent"
      >
        {{ data.section[2].header.sectionTitle }}
      </h2>
      <div class="mx-auto mb-12 max-w-7xl">
        <FpBenefit
          v-for="item in data.section[2].content.list"
          v-bind="item"
          columns="4"
        />
      </div>
    </section>

    <!-- Get Started Developing Section -->
    <section class="w-full">
      <div
        class="mx-auto max-w-7xl bg-gradient-to-r from-green-200 to-blue-100 p-2 sm:p-10"
      >
        <h3 class="text-center font-bold text-fp-blue">
          {{ data.section[3].header.sectionTitle }}
        </h3>
        <FpList columns="sm:grid-cols-3 gap-12 lg:gap-4" disableDots="true">
          <FpListItem
            v-for="item in data.section[3].content.list"
            v-bind="item"
            images="true"
            buttons="true"
          />
        </FpList>
      </div>
    </section>

    <!-- Community Section -->
    <section>
      <FpCommunity :data="data.section[4]" />
    </section>

    <!-- Call To Action -->
    <section>
      <FpCallToAction :cta="data.header.cta" />
    </section>
  </main>
</template>
