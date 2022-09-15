<script setup>
const { locale } = useI18n();
let { data } = await useAsyncData("page-data", () => {
  return queryContent("/pages/events/flock/home/." + locale._value).findOne();
});

if (data._value === null) {
  ({ data } = await useAsyncData("page-data-fallback", () => {
    return queryContent("/pages/events/flock/home/.en").findOne();
  }));
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
  <FpHero :background="data.header.images.backgroundImage" alignment="bg-top">
    <FpBanner
      :title="data.header.title"
      :subtitle="data.header.subtitle"
      :logo="data.header.logo"
      color="text-fp-purple"
      border="border border-fp-purple"
      background="text-white bg-fp-purple"
      :ctas="data.header.cta"
    >
      <h2
        class="text-white my-8 font-semibold"
        style="text-shadow: 4px 4px 4px black"
      >
        {{ data.header.eventDate }}
      </h2>
    </FpBanner>
    <div class="flex p-12">
      <div v-for="card in data.header.cards" class="mr-8 w-60">
        <div
          class="text-fp-blue font-semibold leading-none text-lg"
          style="text-shadow: 1px 2px 4px black"
        >
          <img
            class="inline align-baseline h-10 max-w-none mr-1"
            :src="`${
              $config.app.baseURL + '/' + card.image.replace('public/', '')
            }`"
          />
          {{ card.subtitle }}
        </div>
        <p class="mt-2 text-slate-400 text-sm">{{ card.description }}</p>
      </div>
    </div>
  </FpHero>

  <main class="flex flex-col items-center">
    <!-- TODO: Explore -->
    <section class="w-full pb-10 bg-gradient-to-b from-slate-200">
      <div class="w-10/12 my-10 mx-auto">
        <h2
          class="text-5xl text-center mb-12 font-bold bg-clip-text text-transparent bg-gradient-to-r from-fp-green to-fp-blue-light"
        >
          Explore the latest in Open Source
        </h2>
        <div
          class="flex flex-wrap justify-around items-stretch text-center gap-4 text-fp-blue-dark"
        >
          <FpCard v-for="card in data.exploreSection.cards">
            <FpCardImage :src="card.imageURI" />
            <FpCardTitle>{{ card.title }}</FpCardTitle>
            <FpCardText>{{ card.description }}</FpCardText>
            <FpCardAction>{{ card.link.text }}</FpCardAction>
          </FpCard>
        </div>
      </div>
    </section>

    <!-- TODO: Hybrid Experience -->
    <section class="w-10/12 mx-auto my-10">
      <h2
        class="text-5xl text-center mb-12 font-bold bg-clip-text text-transparent bg-gradient-to-r from-fp-green to-fp-blue-light"
      >
        A Hybrid Experience
      </h2>
    </section>

    <!-- TODO: Important Dates -->
    <section class="w-10/12 mx-auto my-10">
      <h2
        class="text-5xl text-center mb-12 font-bold bg-clip-text text-transparent bg-gradient-to-r from-fp-green to-fp-blue-light"
      >
        Important Dates
      </h2>
    </section>

    <!-- TODO: Event Calendar -->
    <section class="w-10/12 mx-auto my-10">
      <h2
        class="text-5xl text-center mb-12 font-bold bg-clip-text text-transparent bg-gradient-to-r from-fp-green to-fp-blue-light"
      >
        Event Calendar
      </h2>
    </section>

    <!-- Community Section -->
    <section class="my-10">
      <FpCommunity :data="data.section[0]" />
    </section>

    <!-- TODO: Our Sponsors -->
    <section class="w-10/12 mx-auto my-10">
      <h2
        class="text-5xl text-center mb-12 font-bold bg-clip-text text-transparent bg-gradient-to-r from-fp-green to-fp-blue-light"
      >
        Our Sponsors
      </h2>
      <p class="font-normal text-gray-600 mx-auto max-w-lg text-center">
        Thank you to our sponsors, supporting this event is one of the ways that
        they contribute to open source.
      </p>

      <FpSponsors :sponsors="data.sponsors" />
    </section>

    <!-- Benefits of Sponsoring -->
    <section class="w-10/12 my-10">
      <header
        class="grid md:grid-cols-2 gap-4 md:w-11/12 mx-auto text-center md:text-left"
      >
        <h3
          class="text-fp-blue font-medium mb-4 xl:mb-6 md:col-span-2 xl:col-span-1"
        >
          {{ data.section[1].header.sectionTitle }}
        </h3>
      </header>
      <FpList columns="sm:grid-cols-2 gap-12 lg:gap-4">
        <FpListItem
          v-for="item in data.section[1].content.list"
          v-bind="item"
        />
      </FpList>
    </section>
  </main>
</template>
