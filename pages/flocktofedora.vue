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
    <section class="w-full pb-10 bg-slate-100">
      <div class="w-10/12 max-w-screen-xl my-10 mx-auto">
        <h2
          class="2xl:px-72 text-5xl md:text-7xl text-center mb-12 font-bold bg-clip-text text-transparent bg-gradient-to-r from-fp-purple via-fp-blue-light to-fp-purple"
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
	<h3 class="mt-20 text-4xl text-center font-semibold text-fp-blue-dark">Watch Footage from Past Events</h3>
        <div class="grid grid-cols-1 md:grid-cols-2 w-10/12 mx-auto mt-8 bg-white rounded-lg">
          <div class="col-span-1 p-1 sm:p-5">
	    <iframe 
	      width="560" 
	      height="315" 
	      src="https://www.youtube-nocookie.com/embed/LqBVHz76Wxc" 
	      title="YouTube video player" 
	      frameborder="0" 
	      allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
	      allowfullscreen
	      class="w-full">
	    </iframe>
          </div>
          <div class="col-span-1 text-left flex flex-col justify-center p-1 sm:p-5 text-center sm:text-start mx-12">
            <h4 class="mb-5 font-semibold text-fp-blue-dark">What to expect</h4>
            <p class="font-normal text-gray-600 ">
              Flock is an annual conference for contributors of Fedora Linux. It is where the community plans and showcases the strategy and work on the project. Check out the recordings from previous years of Flock and Nest.
            </p>
          </div>
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
        class="grid md:grid-cols-2 gap-4 md:w-11/12 max-w-screen-xl mx-auto text-center md:text-left"
      >
        <h3
          class="text-fp-blue font-medium mb-4"
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
