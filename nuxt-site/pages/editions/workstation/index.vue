<script setup>
useHead({
  title: "Fedora Workstation | The Fedora Project",
});
const { data } = await useAsyncData("page-data", () => {
  return queryContent("/pages/editions/workstation/home").find();
});
</script>
<template>
  <FpHero :background="data[0].header.images.backgroundImage">
    <FpBanner
      :title="data[0].header.title"
      :subtitle="data[0].header.subtitle"
      :image="data[0].header.images.image"
      color="text-green"
      border="border-green"
      background="bg-green"
      :cta1="data[0].header.cta[0].text"
      :link1="data[0].header.cta[0].url"
      :cta2="data[0].header.cta[1].text"
      :link2="data[0].header.cta[1].url"
    />
  </FpHero>
  <main class="flex flex-col items-center my-8">
    <!-- Why Fedora Workstation -->
    <section class="w-10/12">
      <header
        class="grid md:grid-cols-2 gap-4 md:w-11/12 mx-auto text-center md:text-left"
      >
        <h3
          class="text-blue font-medium mb-4 xl:mb-6 md:col-span-2 xl:col-span-1"
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
    <section class="mt-32">
      <FpBenefit
        v-for="item in data[0].section[1].content.list"
        v-bind="item"
      />
    </section>
  </main>
</template>
