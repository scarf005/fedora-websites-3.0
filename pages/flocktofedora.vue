<script setup>
const { locale } = useI18n();
const contentPath = 'events/flock';

let { data } = await useAsyncData("page-data", () => {
  return queryContent(contentPath + "." + locale._value).findOne();
});

if (data._value === null) {
  // Fallback to english content
  ({ data } = await useAsyncData("page-data-fallback", () => {
    return queryContent().where({_file: contentPath + ".yml"}).findOne();
  }));
}
useContentHead(data);

const explore = data._value.sections[1];
const watch = data._value.sections[2];
const community = data._value.sections[5];
const sponsors = data._value.sections[6];
const sponsorsBenefits = data._value.sections[7];
</script>
<template>
  <FpHero :background="data.header_images[1].image" alignment="bg-top">
    <FpBanner
      :subtitle="data.title"
      :logo="data.header_images[0].image"
      color="text-fp-purple"
      border="border border-fp-purple"
      background="text-white bg-fp-purple"
      :ctas="data.links"
      :subtitleStyle="{ color: 'fp-blue', isBold: 'true' }"
      icon="calendar"
    >
      <h2
        class="my-8 font-semibold text-white"
        style="text-shadow: 4px 4px 4px black"
      >
        {{ data.description }}
      </h2>
    </FpBanner>
    <div class="mx-auto flex max-w-screen-xl p-12">
      <div
        v-for="card in data.sections[0].content"
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
          {{ card.title }}
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
          {{ explore.sectionTitle }}
        </h2>
        <div
          class="flex flex-wrap items-stretch justify-around gap-4 text-center text-fp-blue-dark"
        >
          <FpCard v-for="card in explore.content">
            <FpCardImage :src="card.image" />
            <FpCardTitle>{{ card.title }}</FpCardTitle>
            <FpCardText>{{ card.description }}</FpCardText>
            <FpCardAction>{{ card.link.text }}</FpCardAction>
          </FpCard>
        </div>

        <h3
          class="mt-20 text-center text-2xl font-semibold text-fp-blue-dark sm:text-4xl"
        >
          {{ watch.sectionTitle }}
        </h3>
        <div
          class="mx-auto mt-8 grid w-full grid-cols-1 rounded-lg bg-white lg:grid-cols-2"
        >
          <div class="col-span-1 p-1 sm:p-5">
            <iframe
              width="560"
              height="315"
              :src="watch.content[0].image"
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
              {{ watch.content[0].title }}
            </h4>
            <p class="font-normal text-gray-600">
              {{ watch.content[0].description }}
            </p>
            <p class="mt-4 text-right">
              <a
                class="text-fp-blue"
                :href="watch.content[0].link.url"
                >{{ watch.content[0].link.text }}
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
    <!-- <section class="mx-auto my-10 w-full">
      <div class="my-10 mx-auto w-10/12 max-w-screen-xl">
        <h2
          class="mx-auto mb-12 max-w-max bg-gradient-to-r from-fp-purple via-fp-blue-light to-fp-purple bg-clip-text text-center text-3xl font-bold text-transparent sm:text-5xl md:leading-normal lg:text-7xl"
        >
          A Hybrid Experience
        </h2>
      </div>
    </section> -->

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
        :background="community.image"
        alignment="bg-top"
      >
        <section class="mx-auto w-10/12 max-w-screen-xl py-24">
          <h2
            class="mx-auto mb-12 max-w-max bg-gradient-to-r from-fp-purple via-fp-blue-light to-fp-purple bg-clip-text text-center text-3xl font-bold text-transparent sm:text-5xl lg:text-7xl"
          >
            {{ community.sectionTitle }}
          </h2>
          <h4 class="mx-0 mb-20 text-center text-lg text-fp-blue-dark sm:mx-20">
            {{ community.description }}
          </h4>

          <FpList columns="sm:grid-cols-2">
            <FpListItem
              v-for="item in community.content"
              v-bind="item"
	      :iconURI="item.image"
	      :image="null"
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
        {{ sponsors.sectionTitle }}
      </h2>
      <p class="mx-auto max-w-lg text-center font-normal text-gray-600">
        {{ sponsors.description }}
      </p>

      <FpSponsors :sponsors="sponsors.content" />
    </section>

    <!-- Benefits of Sponsoring -->
    <section class="my-10 w-10/12">
      <header
        class="mx-auto max-w-screen-xl text-center md:w-11/12 md:text-left"
      >
        <h3 class="mb-4 text-center font-medium text-fp-blue">
          {{ sponsorsBenefits.sectionTitle }}
        </h3>
      </header>
      <FpList columns="sm:grid-cols-2">
        <FpListItem
          v-for="item in sponsorsBenefits.content"
          v-bind="item"
        />
      </FpList>
    </section>
  </main>
</template>
