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
              <span class="text-sm">{{
                data.sections[0].content[0].title
              }}</span>
              {{ data.sections[0].content[0].description }}
            </p>
            <p class="text-fp-gray">
              <span class="text-sm">{{
                data.sections[0].content[1].title
              }}</span>
              {{ data.sections[0].content[1].description }}
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

      <!-- FEDORA MEDIA WRITER -->
      <div class="my-10 grid grid-cols-2">
        <div class="col-span-2 flex p-5 md:col-span-1">
          <div>
            <FpImage :src="data.sections[1].images" />
          </div>
          <div>
            <h2 class="text-fp-blue">
              {{ data.sections[1].sectionTitle }}
            </h2>
            <p class="mb-10 text-fp-gray">
              {{ data.sections[1].sectionDescription }}
            </p>

            <div class="flex">
              <FpLink
                :href="item.link.url"
                v-for="item in data.sections[1].content"
                class="rounded-xl border border-blue-400 px-6 py-3 text-blue-400"
              >
                <Icon name="fa-download" /> {{ item.link.text }}
              </FpLink>
            </div>
          </div>
        </div>

        <!-- DOWNLOADS -->
        <div class="col-span-2 p-5 md:col-span-1">
          <h2 class="text-fp-blue">
            {{ data.sections[2].sectionTitle }}
          </h2>
          <p class="mb-10 text-fp-gray">
            {{ data.sections[2].sectionDescription }}
          </p>
          <div v-for="item in data.sections[2].content">
            <p class="mt-10 font-bold">{{ item.description }}</p>

            <div
              class="flex items-center justify-between rounded-xl border border-gray-200 bg-white p-5"
            >
              <p>
                <span class="mr-5 font-semibold text-gray-800">{{
                  item.title
                }}</span
                ><span class="text-gray-500"> {{ item.link.text }}</span>
              </p>
              <FpLink
                :href="item.link.url"
                class="rounded-xl border border-blue-400 p-3 px-5 text-blue-400"
              >
                <Icon name="fa-download" />
              </FpLink>
            </div>
          </div>
        </div>
      </div>

      <!-- OTHER SECTIONS -->
      <div class="my-10 flex">
        <div class="flex-1">
          <h2 class="text-fp-blue">
            {{ data.sections[3].content[0].title }}
          </h2>
          <p class="text-fp-gray">
            {{ data.sections[3].content[0].description }}
          </p>
          <FpLink :href="data.sections[3].content[0].link.url">{{
            data.sections[3].content[0].link.text
          }}</FpLink>
        </div>
        <div class="flex-1">
          <h2 class="text-fp-blue">
            {{ data.sections[3].content[1].title }}
          </h2>
          <p class="text-fp-gray">
            {{ data.sections[3].content[1].description }}
          </p>
          <FpLink :href="data.sections[3].content[1].link.url">{{
            data.sections[3].content[1].link.text
          }}</FpLink>
        </div>
      </div>
      <div class="my-10">
        <h2 class="text-fp-blue">
          {{ data.sections[4].sectionTitle }}
        </h2>
        <p class="text-fp-gray">
          {{ data.sections[4].sectionDescription }}
        </p>
        <FpLink :href="data.sections[4].content[0].link.url">{{
          data.sections[4].content[0].link.text
        }}</FpLink>
      </div>
      <div class="my-10">
        <h2 class="text-fp-blue">
          {{ data.sections[5].sectionTitle }}
        </h2>
        <p class="text-base text-fp-gray">
          {{ data.sections[5].content[0].description }}
        </p>
        <p class="text-xs text-gray-300">
          {{ data.sections[5].content[1].description }}
        </p>
      </div>
      <div class="my-10">
        <h2 class="text-fp-blue">
          {{ data.sections[6].sectionTitle }}
        </h2>
        <p class="text-base text-fp-gray">
          {{ data.sections[6].sectionDescription }}
        </p>
        <div v-for="item in data.sections[6].content">
          <FpLink href="item.link.url">{{ item.title }}</FpLink>
        </div>

        <p class="text-base text-fp-gray">
          {{ data.sections[7].sectionTitle }}
        </p>
        <div v-for="item in data.sections[7].content">
          <FpLink href="item.link.url">{{ item.title }}</FpLink>
        </div>
      </div>

      <div class="my-10">
        <h2 class="text-fp-blue">
          {{ data.sections[8].sectionTitle }}
        </h2>
        <p class="text-base text-fp-gray">
          {{ data.sections[8].sectionDescription }}
        </p>
      </div>
    </div>
  </main>
</template>
