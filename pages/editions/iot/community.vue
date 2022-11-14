<script setup>
const { locale } = useI18n();
let { data } = await useAsyncData("page-data", () => {
  return queryContent("/editions/iot/community." + locale._value).findOne();
});

if (data._value === null) {
  ({ data } = await useAsyncData("page-data-fallback", () => {
    return queryContent("/editions/iot/community").sort().find();
  }));
  data._value = data._value[data._value.length - 1];
}
let events = await useAsyncData(() => {
  return queryContent("/partials/events").findOne();
});
useContentHead(data);
</script>
<template>
  <main class="mt-4 border-t-8 border-fp-purple">
    <FpHeader
      :title="data.title"
      :description="data.description"
      :details="data.sections[0].sectionDescription"
      color="text-fp-purple"
      bgColor="bg-fp-blue-light/10"
    />
    <!-- communication channels -->
    <section class="mx-auto bg-fp-purple-light/10">
      <div class="container mx-auto flex flex-col justify-center pb-8">
        <header class="py-8 text-center xl:text-start">
          <h2 class="text-fp-purple xl:text-4xl">
            {{ data.sections[1].sectionTitle }}
          </h2>
        </header>
        <div class="flex flex-wrap justify-center gap-10 2xl:justify-between">
          <FpCard
            v-for="card in data.sections[1].content"
            :key="card.id"
            :title="card.title"
            :description="card.description"
            :image="card.image"
            :link="card.link"
            class="m-4 flex flex-col justify-between md:max-w-xs"
          />
        </div>
        <FpJoinTip />
      </div>
    </section>

    <!-- ways to get involved -->
    <section class="bg-fp-blue-light/10">
      <div
        class="container mx-auto grid justify-center gap-8 py-12 lg:grid-cols-2 lg:justify-start xl:py-8"
      >
        <header
          class="col-span-full my-8 mx-auto w-full text-center md:text-start"
        >
          <h2 class="text-fp-purple xl:text-4xl">
            {{ data.sections[2].sectionTitle }}
          </h2>
        </header>
        <div
          v-for="content in data.sections[2].content"
          :key="content.id"
          class="max-w-lg text-center lg:text-start"
        >
          <h3 class="font-medium text-fp-blue">{{ content.title }}</h3>
          <p class="max-w-sm text-fp-gray-darkest">{{ content.description }}</p>
        </div>

        <FpJoinTip
          description="Your friendly and helpful contributions to these communication channels would be greatly appreciated"
        />
      </div>
    </section>
    <!-- Fedora Events -->
    <EventSection color="text-fp-purple" />
    <!-- Publication Section -->
    <PublicationSection />
  </main>
</template>
