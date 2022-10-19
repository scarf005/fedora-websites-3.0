<script setup>
const { locale } = useI18n();
let { data } = await useAsyncData("page-data", () => {
  return queryContent("/events/flock/." + locale._value).findOne();
});

if (data._value === null) {
  ({ data } = await useAsyncData("page-data-fallback", () => {
    return queryContent("/pages/events/flock/").sort().find();
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
  <FpHero :background="data.header.images.backgroundImage" alignment="bg-top">
    <FpBanner
      :title="data.header.title"
      :subtitle="data.header.subtitle"
      :logo="data.header.logo"
      color="text-fp-purple"
      border="border border-fp-purple"
      background="text-white bg-fp-purple"
      :ctas="data.header.cta"
      :subtitleStyle="{ color: 'fp-blue', isBold: 'true' }"
    >
      <h2
        class="my-8 font-semibold text-white"
        style="text-shadow: 4px 4px 4px black"
      >
        {{ data.header.eventDate }}
      </h2>
    </FpBanner>
    <div class="mx-auto flex max-w-screen-xl p-12">
      <div
        v-for="card in data.header.cards"
        class="mr-8 max-w-[17rem] rounded-lg bg-black/70 p-4"
      >
        <div
          class="text-lg font-semibold leading-none text-fp-blue"
          style="text-shadow: 1px 2px 4px black"
        >
          <img
            class="mr-1 inline h-10 max-w-none align-baseline"
            :src="`${
              $config.app.baseURL + '/' + card.image.replace('public/', '')
            }`"
          />
          {{ card.subtitle }}
        </div>
        <p class="text-sm text-slate-300">{{ card.description }}</p>
      </div>
    </div>
  </FpHero>

  <main class="flex flex-col items-center">
    <!-- TODO: Explore -->
    <section class="w-full bg-slate-100 pb-10">
      <div class="my-10 mx-auto w-10/12 max-w-screen-xl">
        <h2
          class="mx-auto mb-12 max-w-screen-md bg-gradient-to-r from-fp-purple via-fp-blue-light to-fp-purple bg-clip-text text-center text-3xl font-bold text-transparent sm:text-5xl lg:text-7xl"
        >
          {{ data.exploreSection.header.title }}
        </h2>
        <div
          class="flex flex-wrap items-stretch justify-around gap-4 text-center text-fp-blue-dark"
        >
          <FpCard v-for="card in data.exploreSection.cards">
            <FpCardImage :src="card.imageURI" />
            <FpCardTitle>{{ card.title }}</FpCardTitle>
            <FpCardText>{{ card.description }}</FpCardText>
            <FpCardAction>{{ card.link.text }}</FpCardAction>
          </FpCard>
        </div>

        <h3
          class="mt-20 text-center text-2xl font-semibold text-fp-blue-dark sm:text-4xl"
        >
          {{ data.exploreSection.pastEvents.header.title }}
        </h3>
        <div
          class="mx-auto mt-8 grid w-full grid-cols-1 rounded-lg bg-white lg:grid-cols-2"
        >
          <div class="col-span-1 p-1 sm:p-5">
            <iframe
              width="560"
              height="315"
              :src="data.exploreSection.pastEvents.card.videoURL"
              title="YouTube video player"
              frameborder="0"
              allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
              allowfullscreen
              class="w-full"
            >
            </iframe>
          </div>
          <div
            class="col-span-1 mx-0 flex flex-col justify-center p-3 pt-5 text-left text-fp-blue-dark sm:p-5 xl:mx-12"
          >
            <h4 class="mb-5 font-semibold">
              {{ data.exploreSection.pastEvents.card.title }}
            </h4>
            <p class="font-normal text-gray-600">
              {{ data.exploreSection.pastEvents.card.description }}
            </p>
            <p class="mt-4 text-right">
              <a
                class="text-fp-blue"
                :href="data.exploreSection.pastEvents.card.link.targetURL"
                >{{ data.exploreSection.pastEvents.card.link.text }}
                <font-awesome-icon
                  class="ml-2"
                  icon="fa-solid fa-arrow-right-long"
                />
              </a>
            </p>
          </div>
        </div>
      </div>
    </section>

    <!-- TODO: Hybrid Experience -->
    <section class="mx-auto my-10 w-full">
      <div class="my-10 mx-auto w-10/12 max-w-screen-xl">
        <h2
          class="mx-auto mb-12 max-w-max bg-gradient-to-r from-fp-purple via-fp-blue-light to-fp-purple bg-clip-text text-center text-3xl font-bold text-transparent sm:text-5xl md:leading-normal lg:text-7xl"
        >
          A Hybrid Experience
        </h2>
      </div>
    </section>

    <!-- TODO: Important Dates -->
    <!--
    <section class="w-10/12 mx-auto my-10">
      <h2
        class="text-5xl text-center mb-12 font-bold bg-clip-text text-transparent bg-gradient-to-r from-fp-green to-fp-blue-light"
      >
        Important Dates
      </h2>
    </section>
    -->

    <!-- TODO: Event Calendar -->
    <!--
    <section class="w-10/12 mx-auto my-10">
      <h2
        class="text-5xl text-center mb-12 font-bold bg-clip-text text-transparent bg-gradient-to-r from-fp-green to-fp-blue-light"
      >
        Event Calendar
      </h2>
    </section>
    -->

    <!-- Community Section -->
    <section class="my-10">
      <FpHero
        :background="data.communitySection.header.backgroundImageURI"
        alignment="bg-top"
      >
        <section class="mx-auto w-10/12 max-w-screen-xl py-24">
          <h2
            class="mx-auto mb-12 max-w-max bg-gradient-to-r from-fp-purple via-fp-blue-light to-fp-purple bg-clip-text text-center text-3xl font-bold text-transparent sm:text-5xl lg:text-7xl"
          >
            {{ data.communitySection.header.title }}
          </h2>
          <h4 class="mx-0 mb-20 text-center text-lg text-fp-blue-dark sm:mx-20">
            {{ data.communitySection.header.subtitle1 }}
          </h4>

          <FpList columns="sm:grid-cols-2">
            <FpListItem
              v-for="item in data.communitySection.list"
              v-bind="item"
            />
          </FpList>
        </section>
      </FpHero>
    </section>

    <!-- TODO: Our Sponsors -->
    <section class="mx-auto my-10 w-10/12">
      <h2
        class="mx-auto mb-12 max-w-max bg-gradient-to-r from-fp-purple via-fp-blue-light to-fp-purple bg-clip-text text-center text-3xl font-bold text-transparent sm:text-5xl lg:text-7xl"
      >
        {{ data.sponsorSection.header.title }}
      </h2>
      <p class="mx-auto max-w-lg text-center font-normal text-gray-600">
        {{ data.sponsorSection.header.subtitle }}
      </p>

      <FpSponsors :sponsors="data.sponsorSection.sponsors" />
    </section>

    <!-- Benefits of Sponsoring -->
    <section class="my-10 w-10/12">
      <header
        class="mx-auto max-w-screen-xl text-center md:w-11/12 md:text-left"
      >
        <h3 class="mb-4 text-center font-medium text-fp-blue">
          {{ data.sponsorSection.benefits.header.title }}
        </h3>
      </header>
      <FpList columns="sm:grid-cols-2">
        <FpListItem
          v-for="item in data.sponsorSection.benefits.list"
          v-bind="item"
        />
      </FpList>
    </section>
  </main>
</template>
