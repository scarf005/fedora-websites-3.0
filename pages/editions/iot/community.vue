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
useContentHead(data);
</script>
<template>
  <main class="mt-4 border-t-8 border-fp-purple">
    <header>
      <section class="my-8 mx-auto px-8 text-center lg:text-start xl:px-0">
        <div class="container mx-auto">
          <h1 class="mb-4 text-fp-purple xl:mb-8">{{ data.title }}</h1>
          <p class="text-fp-gray">{{ data.description }}</p>
        </div>
      </section>
      <section class="mx-auto bg-fp-blue-light/5">
        <div
          class="container mx-auto px-8 py-12 text-center lg:px-0 lg:text-start"
        >
          <p class="text-fp-gray-darkest">
            {{ data.sections[0].sectionDescription }}
          </p>
        </div>
      </section>
    </header>

    <!-- communication channels -->
    <section class="mx-auto bg-fp-purple-light/10">
      <div class="container mx-auto flex flex-col justify-center pb-8">
        <header class="py-8 text-center xl:text-start">
          <h2 class="text-fp-purple xl:text-4xl">
            {{ data.sections[1].sectionTitle }}
          </h2>
        </header>
        <div class="flex flex-wrap justify-center gap-10 2xl:justify-between">
          <article
            v-for="card in data.sections[1].content"
            :key="card.id"
            class="m-4 flex flex-col justify-between md:max-w-xs"
          >
            <h3
              class="text-center text-2xl font-semibold text-fp-blue lg:text-start"
            >
              {{ card.title }}
            </h3>
            <p
              class="mx-auto mt-2 hidden w-52 break-words text-center text-sm text-fp-gray-darkest sm:block lg:w-80 lg:text-start lg:text-base"
            >
              {{ card.description }}
            </p>
            <FpImage :image="card.image" :alt="card.image" class="mx-auto" />

            <NuxtLink
              :to="card.link.url"
              class="mx-auto flex w-full justify-center rounded-lg bg-fp-blue-light py-2 font-medium text-white"
              >{{ card.link.text }}</NuxtLink
            >
          </article>
        </div>
      </div>
    </section>

    <!-- ways to get involved -->
    <section class="bg-fp-blue-light/10">
      <div
        class="container mx-auto grid justify-center gap-8 py-12 lg:grid-cols-2 lg:justify-start xl:py-8"
      >
        <header class="col-span-full my-8 mx-auto text-center lg:text-start">
          <h2 class="text-fp-purple xl:text-4xl">
            {{ data.sections[2].sectionTitle }}
          </h2>
        </header>
        <div
          v-for="content in data.sections[2].content"
          :key="content.id"
          class="mx-auto max-w-lg text-center lg:text-start"
        >
          <h3 class="font-medium text-fp-blue">{{ content.title }}</h3>
          <p class="max-w-sm text-fp-gray-darkest">{{ content.description }}</p>
        </div>
      </div>
    </section>
    <!-- Fedora Events -->
    <EventSection color="text-fp-purple" />
    <!-- Publication Section -->
    <PublicationSection />
  </main>
</template>
