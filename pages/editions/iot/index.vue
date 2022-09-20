<script setup>
const { locale } = useI18n();
let { data } = await useAsyncData("page-data", () => {
  return queryContent("/pages/editions/iot/home/." + locale._value).findOne();
});

if (data._value === null) {
  ({ data } = await useAsyncData("page-data-fallback", () => {
    return queryContent("/pages/editions/iot/home/").sort().find();
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
      :background="data.header.images.backgroundImage"
      alignment="bg-bottom"
    >
      <FpBanner
        :title="data.header.title"
        :subtitle="data.header.subtitle"
        color="text-fp-purple"
        border="border border-fp-purple"
        background="text-white bg-fp-purple"
        :ctas="data.header.cta"
      >
        <FpImage :image="data.header.images.image" />
      </FpBanner>
    </FpHero>
    <FpHero
      :background="data.section[0].header.headerImage.image"
      alignment="bg-bottom"
    >
      <section class="w-10/12 pt-12 mx-auto">
        <h3
          class="text-fp-blue font-medium mb-4 xl:mb-6 md:col-span-2 xl:col-span-1"
        >
          {{ data.section[0].header.sectionTitle }}
        </h3>
        <FpList columns="sm:grid-cols-2 gap-12 lg:gap-4">
          <FpListItem
            v-for="item in data.section[0].content.list"
            v-bind="item"
          />
        </FpList>
      </section>
    </FpHero>
    <div class="bg-magenta-100" style="min-height: 60vh">
      <section class="w-10/12 mx-auto pt-12">
        <h3
          class="text-center text-fp-blue font-medium mb-4 xl:mb-6 md:col-span-2 xl:col-span-1"
        >
          {{ data.section[1].header.sectionTitle }}
        </h3>
        <FpList columns="sm:grid-cols-4 gap-12 lg:gap-4" disableDots="true">
          <FpListItem
            v-for="item in data.section[1].content.list"
            v-bind="item"
            images="true"
          />
        </FpList>
      </section>
    </div>
    <FpCommunity :data="data.section[2]" />
  </main>
</template>
