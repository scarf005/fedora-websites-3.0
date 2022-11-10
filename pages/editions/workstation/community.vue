<script setup>
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
</script>

<template>
  <main class="mt-4 border-t-8 border-fp-green">
    <header>
      <TheLocalBar
        image="assets/images/fedora-workstation-logo.png"
        :items="[
          { name: 'Download', link: '/download' },
          { name: 'Community', link: '#' },
          { name: 'Help', link: '#' },
        ]"
      />
      <section class="my-8 mx-auto px-8 text-center lg:text-start xl:px-0">
        <div class="container mx-auto">
          <h1 class="mb-4 text-fp-green xl:mb-8">{{ data.title }}</h1>
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
    <section class="mx-auto bg-fp-green-light/10">
      <div class="container mx-auto flex flex-col justify-center pb-8">
        <header class="py-8 text-center xl:text-start">
          <h2 class="text-fp-green xl:text-4xl">
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
      </div>
    </section>

    <!-- ways to get involved -->
    <section class="bg-fp-blue-light/10">
      <div
        class="container mx-auto grid justify-center gap-8 py-12 lg:grid-cols-2 lg:justify-start xl:py-8"
      >
        <header class="col-span-full my-8 mx-auto text-center lg:text-start">
          <h2 class="text-fp-green xl:text-4xl">
            {{ data.sections[2].sectionTitle }}
          </h2>
        </header>
        <div
          v-for="content in data.sections[2].content.slice(0, 2)"
          :key="content.id"
          class="mx-auto max-w-lg text-center lg:text-start"
        >
          <h3 class="font-medium text-fp-blue">{{ content.title }}</h3>
          <p class="max-w-sm text-fp-gray-darkest">{{ content.description }}</p>
        </div>
      </div>
    </section>
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
        <p
          class="mb-12 max-w-4xl text-center text-fp-gray-darkest md:text-start"
        >
          {{ data.sections[3].content[6].description }}
        </p>
        <FpBtn
          :url="data.sections[3].content[6].link.url"
          class="mx-auto block"
          >{{ data.sections[3].content[6].link.text }}</FpBtn
        >
      </div>
      <FpImage
        :image="data.sections[3].content[6].image"
        class="order-first hidden h-fit w-48 md:block"
      />
    </article>
    <PublicationSection />
  </main>
</template>
