<script setup>
const { locale } = useI18n();
let { data } = await useAsyncData("page-data", () => {
  return queryContent("/editions/iot/home/." + locale._value).findOne();
});

if (data._value === null) {
  ({ data } = await useAsyncData("page-data-fallback", () => {
    return queryContent("/editions/iot/home/").sort().find();
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
  <main>
    <FpHero
      :background="data.header_images[1].image"
      alignment="bg-bottom"
    >
      <FpBanner
        :title="data.title"
        :subtitle="data.description"
        color="text-fp-purple"
        border="border border-fp-purple"
        background="text-white bg-fp-purple"
        :ctas="data.links"
      >
        <FpImage :image="data.header_images[0].image" />
      </FpBanner>
    </FpHero>

    <FpHero
      :background="data.sections[0].images"
      alignment="bg-bottom"
    >
      <section class="mx-auto w-10/12 pt-12">
        <h3
          class="mb-4 font-medium text-fp-blue md:col-span-2 xl:col-span-1 xl:mb-6"
        >
          {{ data.sections[0].sectionTitle }}
        </h3>
        <FpList columns="sm:grid-cols-2 gap-12 lg:gap-4">
          <FpListItem
            v-for="item in data.sections[0].content"
            v-bind="item"
          />
        </FpList>
      </section>
    </FpHero>
  <div class="bg-magenta-100" style="min-height: 60vh">
      <section class="mx-auto w-10/12 pt-12">
        <h3
          class="mb-4 text-center font-medium text-fp-blue md:col-span-2 xl:col-span-1 xl:mb-6"
        >
          {{ data.sections[1].sectionTitle }}
        </h3>
        <FpList columns="sm:grid-cols-4 gap-12 lg:gap-4" disableDots="true">
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
      <FpCallToAction
        :cta="data.links"
        image="assets/images/fiot-logo.png"
      />
    </section> 
    
  </main>
</template>
