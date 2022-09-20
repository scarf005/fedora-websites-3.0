<script setup>
const { locale } = useI18n();
let { data } = await useAsyncData("page-data", () => {
  return queryContent(
    "/pages/editions/workstation/home/." + locale._value
  ).findOne();
});

if (data._value === null) {
  ({ data } = await useAsyncData("page-data-fallback", () => {
    return queryContent("/pages/editions/workstation/home/.en").findOne();
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
      :reviewUrl="data.header.reviewUrl"
      :ctas="data.header.cta"
      color="text-fp-green"
      border="border border-fp-green"
      background="text-white bg-fp-green"
    >
      <div class="hero-laptop-container">
        <div class="mb-48 px-auto max-w-sm sm:max-w-xl">
          <FpImage
            class="w-full"
            image="assets/images/workstation_framework.png"
          />
          <video
            class="w-full px-11 sm:px-[70px] -mt-[310px] sm:-mt-[473px]"
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

  <main class="flex flex-col items-center mt-8">
    <!-- Why Fedora Workstation -->
    <section class="w-10/12">
      <header
        class="grid md:grid-cols-2 gap-4 md:w-11/12 mx-auto text-center md:text-left"
      >
        <h3
          class="text-fp-blue font-medium mb-4 xl:mb-6 md:col-span-2 xl:col-span-1"
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
        class="text-5xl text-center mb-12 font-bold bg-clip-text text-transparent bg-gradient-to-r from-fp-green to-fp-blue-light"
      >
        {{ data.section[1].header.sectionTitle }}
      </h2>
      <FpBenefit v-for="item in data.section[1].content.list" v-bind="item" columns="2" />
    </section>

    <!-- Developers Section -->
    <section>
      <h2
        class="text-5xl text-center mb-12 font-bold bg-clip-text text-transparent bg-gradient-to-r from-fp-green to-fp-blue-light"
      >
      {{ data.section[2].header.sectionTitle }}
      </h2>
      <div class="mb-12 max-w-7xl mx-auto">
        <FpBenefit v-for="item in data.section[2].content.list" v-bind="item" columns="2" />

      </div>
    </section>

    <!-- Get Started Developing Section -->
    <section class="w-full">
      <div
        class="h-96 bg-gradient-to-r from-green-200 to-blue-100 max-w-7xl mx-auto p-2 sm:p-10"
      >
        <h3 class="text-fp-blue font-bold text-center">
          {{ data.section[3].header.sectionTitle }}
        </h3>
        <FpBenefit v-for="item in data.section[3].content.list" v-bind="item" columns="2" />
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
