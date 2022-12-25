<script setup>
import { mdparser } from "../../config/utilities";
const { locale } = useI18n();

let { data } = await useAsyncData("page-data", () => {
  return queryContent(
    "/editions/workstation/community/" + locale._value
  ).findOne();
});

if (data._value === null) {
  ({ data } = await useAsyncData("page-data-fallback", () => {
    return queryContent("/editions/workstation/community").sort().find();
  }));
  data._value = data._value[data._value.length - 1];
}

useContentHead(data);

if (data._value.sections[3].content[6].description) {
  data._value.sections[3].content[6].descriptionMd = await mdparser(
    data._value.sections[3].content[6].description
  );
}
</script>

<template>
  <main class="mt-4 border-t-8 border-fp-green">
    <TheLocalBar
      image="assets/images/workstation_logo.png"
      home="/workstation"
      textColor="text-green-400"
      :items="[
        { name: 'Download', link: '/workstation/download' },
        { name: 'Community', link: '/workstation/community' },
      ]"
    />
    <div class="container mx-auto max-w-7xl">
      <section class="my-8 mx-auto px-8 text-center lg:text-start xl:px-0">
        <h1 class="mb-4 text-fp-green xl:mb-8">{{ data.title }}</h1>
        <p class="text-fp-gray">{{ data.description }}</p>
      </section>
      <FpDescriptionSection
        :sectionDescription="data.sections[0].sectionDescription"
      />

      <!-- communication channels -->
      <FpCommunicationSection
        color="green"
        :sectionTitle="data.sections[1].sectionTitle"
        :content="data.sections[1].content"
      />

      <!-- ways to get involved -->
      <FpGetInvolvedSection
        color="green"
        :sectionTitle="data.sections[2].sectionTitle"
        :content="data.sections[2].content"
      />

      <!-- Fedora Events -->
      <EventSection color="text-fp-green" />

      <!-- Fedora Release Parties -->
      <section
        class="container col-span-full mx-auto my-8 flex flex-col items-center md:items-start"
      >
        <h3 class="font-bold text-fp-blue-dark">
          {{ data.sections[3].content[5].title }}
        </h3>
        <p class="mt-6 text-fp-gray-darkest">
          {{ data.sections[3].content[5].description }}
        </p>
      </section>

      <!-- Nest Banner -->
      <article
        class="container mx-auto flex w-full justify-center gap-8 self-center bg-gradient-to-r from-fp-green-light/40 to-fp-blue-light/40 p-12 lg:gap-16 xl:my-6 xl:py-20"
      >
        <div class="mx-auto justify-end">
          <h3 class="mb-12 text-center font-bold text-fp-blue-dark">
            {{ data.sections[3].content[6].title }}
          </h3>
          <div>
            <ContentRenderer
              tag="p"
              class="mb-12 max-w-4xl text-center text-fp-gray-darkest md:text-start"
              :value="data.sections[3].content[6].descriptionMd"
            />
          </div>
          <FpBtn
            :url="data.sections[3].content[6].link.url"
            class="mx-auto block"
            >{{ data.sections[3].content[6].link.text }}</FpBtn
          >
        </div>
        <FpImage
          :src="data.sections[3].content[6].image"
          class="order-first hidden h-fit w-48 md:block"
        />
      </article>

      <PublicationSection />
    </div>
  </main>
</template>
