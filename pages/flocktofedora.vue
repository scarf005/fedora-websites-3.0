<script setup>
const { locale } = useI18n();
let { data } = await useAsyncData("page-data", () => {
  return queryContent("/pages/events/flock/." + locale._value).findOne();
});

if (data._value === null) {
  ({ data } = await useAsyncData("page-data-fallback", () => {
    return queryContent("/pages/events/flock/.en").findOne();
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
    <div class="flex p-12 max-w-screen-xl mx-auto">
      <div v-for="card in data.header.cards" class="mr-8 max-w-[17rem] bg-black/70 rounded-lg p-4">
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
        <p class="text-slate-300 text-sm">{{ card.description }}</p>
      </div>
    </div>
  </FpHero>

  <main class="flex flex-col items-center">
    <!-- TODO: Explore -->
    <section class="w-full pb-10 bg-slate-100">
      <div class="w-10/12 max-w-screen-xl my-10 mx-auto">
        <h2
          class="mx-auto max-w-screen-md text-3xl sm:text-5xl lg:text-7xl text-center mb-12 font-bold bg-clip-text text-transparent bg-gradient-to-r from-fp-purple via-fp-blue-light to-fp-purple"
        >
          {{ data.exploreSection.header.title }}
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

	<h3 class="mt-20 text-2xl sm:text-4xl text-center font-semibold text-fp-blue-dark">{{ data.exploreSection.pastEvents.header.title }}</h3>
        <div class="grid grid-cols-1 lg:grid-cols-2 w-full mx-auto mt-8 bg-white rounded-lg">
          <div class="col-span-1 p-1 sm:p-5">
	    <iframe 
	      width="560" 
	      height="315" 
	      :src="data.exploreSection.pastEvents.card.videoURL" 
	      title="YouTube video player" 
	      frameborder="0" 
	      allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
	      allowfullscreen
	      class="w-full">
	    </iframe>
          </div>
          <div class="col-span-1 text-left flex flex-col justify-center p-3 pt-5 sm:p-5 text-fp-blue-dark mx-0 xl:mx-12">
            <h4 class="mb-5 font-semibold">{{ data.exploreSection.pastEvents.card.title }}</h4>
            <p class="font-normal text-gray-600 ">
	      {{ data.exploreSection.pastEvents.card.description }}
            </p>
            <p class="mt-4 text-right">
              <a class="text-fp-blue" :href="data.exploreSection.pastEvents.card.link.targetURL">{{ data.exploreSection.pastEvents.card.link.text }}
                <font-awesome-icon class="ml-2" icon="fa-solid fa-arrow-right-long" />
	      </a>
            </p>
          </div>
        </div>

      </div>
    </section>

    <!-- TODO: Hybrid Experience -->
    <section class="w-full mx-auto my-10">
      <div class="w-10/12 max-w-screen-xl my-10 mx-auto">
        <h2
          class="max-w-max mx-auto text-3xl sm:text-5xl lg:text-7xl md:leading-normal text-center mb-12 font-bold bg-clip-text text-transparent bg-gradient-to-r from-fp-purple via-fp-blue-light to-fp-purple"
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
      <FpHero :background="data.communitySection.header.backgroundImageURI" alignment="bg-top">
        <section class="w-10/12 max-w-screen-xl mx-auto py-24">
          <h2
            class="max-w-max mx-auto text-3xl sm:text-5xl lg:text-7xl text-center mb-12 font-bold bg-clip-text text-transparent bg-gradient-to-r from-fp-purple via-fp-blue-light to-fp-purple"
	  >
            {{ data.communitySection.header.title }}
          </h2>
          <h4 class="text-lg text-fp-blue-dark mb-20 mx-0 sm:mx-20 text-center">
            {{ data.communitySection.header.subtitle1 }}
          </h4>

          <FpList columns="sm:grid-cols-2">
            <FpListItem v-for="item in data.communitySection.list" v-bind="item" />
          </FpList>
        </section>
      </FpHero>

    </section>

    <!-- TODO: Our Sponsors -->
    <section class="w-10/12 mx-auto my-10">
      <h2
        class="max-w-max mx-auto text-3xl sm:text-5xl lg:text-7xl text-center mb-12 font-bold bg-clip-text text-transparent bg-gradient-to-r from-fp-purple via-fp-blue-light to-fp-purple"
      >
        {{ data.sponsorSection.header.title }}
      </h2>
      <p class="font-normal text-gray-600 mx-auto max-w-lg text-center">
	{{ data.sponsorSection.header.subtitle }}
      </p>

      <FpSponsors :sponsors="data.sponsorSection.sponsors" />
    </section>

    <!-- Benefits of Sponsoring -->
    <section class="w-10/12 my-10">
      <header
        class="md:w-11/12 max-w-screen-xl mx-auto text-center md:text-left"
      >
        <h3
          class="text-center text-fp-blue font-medium mb-4"
        >
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
