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
  <main class="mt-4 border-t-8 border-fp-green">
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
          <div class="flex">
            <p class="mr-5 text-fp-gray">
              <span class="text-sm">RELEASE DATE</span> April 19, 2022
            </p>
            <p class="text-fp-gray">
              <span class="text-sm">SUPPORTED THROUGH</span> May 17 2023
            </p>
          </div>
        </div>
      </section>
      <template v-for="(cta, idx) in data.links">
        <FpLink :href="cta.url" class="mx-5 text-blue-500">
          <Icon name="fa-book" />
          {{ cta.text }}
        </FpLink>
      </template>

      <div class="my-10 grid grid-cols-2">
        <div class="col-span-2 flex p-5 md:col-span-1">
          <div>
            <FpImage :src="data.sections[0].content[0].image" />
          </div>
          <div>
            <h2 class="text-fp-blue">
              {{ data.sections[0].content[0].title }}
            </h2>
            <p class="mb-10 text-fp-gray">
              {{ data.sections[0].content[0].description }}
            </p>
          </div>
        </div>
        <div class="col-span-2 p-5 md:col-span-1">
          <h2 class="text-fp-blue">
            {{ data.sections[0].content[1].title }}
          </h2>
          <p class="mb-10 text-fp-gray">
            {{ data.sections[0].content[1].description }}
          </p>
          <!-- downloads -->
          <div v-for="item in [1, 2, 3]">
            <p class="mt-10 font-bold">For Intel and AMD systems:</p>
            <div
              class="flex items-center justify-between rounded-xl border border-gray-200 bg-white p-5"
            >
              <p>Fedora Workstation 35 x86_64 DVD ISO</p>
              <FpBtn color="text-blue-400 border border-blue-400"
                ><Icon name="fa-download"
              /></FpBtn>
            </div>
          </div>
        </div>
      </div>

      <div class="my-10 flex">
        <div class="flex flex-1">
          <div>
            <h2 class="text-fp-blue">
              {{ data.sections[1].content[0].title }}
            </h2>
            <p class="text-fp-gray">
              {{ data.sections[1].content[0].description }}
            </p>
          </div>
        </div>
        <div class="flex-1">
          <h2 class="text-fp-blue">
            {{ data.sections[1].content[1].title }}
          </h2>
          <p class="text-fp-gray">
            {{ data.sections[1].content[1].description }}
          </p>
        </div>
      </div>
    </div>
  </main>
</template>
