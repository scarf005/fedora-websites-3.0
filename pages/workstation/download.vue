<script setup>
const { locale } = useI18n();
let { data } = await useAsyncData("page-data", () => {
  return queryContent(
    "/editions/workstation/download." + locale._value
  ).findOne();
});

if (data._value === null) {
  ({ data } = await useAsyncData("page-data-fallback", () => {
    return queryContent("/editions/workstation/download").sort().find();
  }));
  data._value = data._value[data._value.length - 1];
}
useContentHead(data);
</script>

<template>
  <TheLocalBar
    image="assets/images/workstation_logo.png"
    home="/workstation"
    textColor="text-fp-blue"
    :items="[
      { name: 'Download', link: '/workstation/download' },
      { name: 'Community', link: '/workstation/community' },
    ]"
  />
  <div class="container mx-auto">
    <section class="my-8 mx-auto px-8 text-center lg:text-start xl:px-0">
      <div class="container mx-auto">
        <h1 class="mb-4 mb-8 text-4xl text-fp-gray">
          {{ data.title.substring(0, 8) }}
          <span class="text-fp-green">{{
            data.title.substring(8, data.title.length)
          }}</span>
        </h1>
        <p class="text-fp-gray">{{ data.description }}</p>
      </div>
    </section>
    <template v-for="(cta, idx) in data.links">
      <FpLink :href="cta.url" class="mx-5 text-blue-500">
        <Icon v-if="idx === 1" :name="`fa6-brands:${icon}`" />
        {{ cta.text }}
      </FpLink>
    </template>

    <div class="flex">
      <div class="flex-1">
        <h2>{{ data.sections[0].content[0].title }}</h2>
      </div>
      <div class="flex-1">
        <h2>{{ data.sections[0].content[1].title }}</h2>
      </div>
    </div>
  </div>
</template>
