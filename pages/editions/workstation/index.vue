<script setup>
useHead({
  title: "Fedora Workstation | The Fedora Project",
});
const { locale } = useI18n();
const { data } = await useAsyncData("page-data", () => {
  return queryContent("/pages/editions/workstation/home")
    .where({ lang: locale._value })
    .find();
});
</script>
<template>
  <FpHero
    :background="data[0].header.images.backgroundImage"
    alignment="bg-bottom"
  >
    <FpBanner
      :title="data[0].header.title"
      :subtitle="data[0].header.subtitle"
      :reviewUrl="data[0].header.reviewUrl"
      color="text-fp-green"
      border="border border-fp-green"
      background="text-white bg-fp-green"
      :ctas="data[0].header.cta"
    >
      <div class="hero-laptop-container">
        <div class="mb-48 px-auto max-w-sm sm:max-w-xl">
          <FpImage
            class="w-full"
            image="assets/images/workstation_framework.png"
          />
          <video
            class="w-full px-11 sm:px-[70px] -mt-[305px] sm:-mt-[465px]"
            autoplay=""
            loop=""
            muted=""
            playsinline=""
            preload="auto"
          >
            <source
              src="https://static.gnome.org/release/40/hero.mp4"
              type="video/mp4"
            />
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
          {{ data[0].section[0].header.sectionTitle }}
        </h3>
      </header>
      <FpList columns="sm:grid-cols-2 gap-12 lg:gap-4">
        <FpListItem
          v-for="item in data[0].section[0].content.list"
          v-bind="item"
        />
      </FpList>
    </section>

    <!-- Benefits Section -->
    <section class="mt-32">
      <h2
        class="text-5xl text-center mb-12 font-bold bg-clip-text text-transparent bg-gradient-to-r from-fp-green to-fp-blue-light"
      >
        Features for everyone.
      </h2>
      <FpBenefit
        v-for="item in data[0].section[1].content.list"
        v-bind="item"
      />
    </section>

    <!-- Developers Section -->
    <section>
      <h2
        class="text-5xl text-center mb-12 font-bold bg-clip-text text-transparent bg-gradient-to-r from-fp-green to-fp-blue-light"
      >
        Great for Developers
      </h2>
      <div class="mb-12 max-w-7xl mx-auto">
        <FpList columns="sm:grid-cols-2 gap-12 lg:gap-4">
          <FpListItem
            v-for="item in data[0].section[0].content.list"
            v-bind="item"
          />
        </FpList>
      </div>
    </section>

    <!-- Get Started Section -->
    <section class="w-full">
      <div
        class="h-96 bg-gradient-to-r from-green-200 to-blue-100 max-w-7xl mx-auto p-2 sm:p-10"
      >
        <h3 class="text-fp-blue font-bold text-center">
          Get started developing with Fedora
        </h3>
      </div>
    </section>

    <!-- Community Section -->
    <section>
      <FpCommunity :data="data[0].section[2]" />
    </section>

    <!-- Call To Action -->
    <section>
      <div class="flex justify-center items-center h-96">
        <FpImage image="assets/images/workstation_logo.jpg" class="max-w-sm" />
      </div>
    </section>
  </main>
</template>
