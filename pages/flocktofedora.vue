<script setup>
useHead({
  title: "Flock to Fedora | Fedora Contributor Conference",
});
const { data } = await useAsyncData("page-data", () => {
  return queryContent("/pages/events/flock").find();
});
</script>
<template>
  <FpHero
    :background="data[0].header.images.backgroundImage"
    alignment="bg-top"
  >
    <FpBanner
      :title="data[0].header.title"
      :subtitle="data[0].header.subtitle"
      :logo="data[0].header.logo"
      color="text-fp-purple"
      border="border border-fp-purple"
      background="text-white bg-fp-purple"
      :ctas="data[0].header.cta"
    >
      <h2 class="text-white my-8 font-semibold">
        {{ data[0].header.eventDate }}
      </h2>
    </FpBanner>
    <div class="flex p-12">
      <div v-for="card in data[0].header.cards" class="mr-8 w-60">
        <div class="text-fp-blue font-semibold leading-none text-lg">
          <img 
	    class="inline align-baseline h-10 max-w-none mr-1" 
	    :src="`${$config.app.baseURL + '/' + card.image.replace('public/', '')}`"
	  />
	  {{ card.subtitle }}
	</div>
        <p class="mt-2 text-slate-500 text-sm">{{ card.description }}</p>
      </div>
    </div>
  </FpHero>

  <main class="flex flex-col items-center mt-8">

    <!-- TODO: Explore -->
    <section class="w-10/12 mx-auto my-10">
      <h2
        class="text-5xl text-center mb-12 font-bold bg-clip-text text-transparent bg-gradient-to-r from-fp-green to-fp-blue-light"
      >
        Explore the latest in Open Source
      </h2>
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
      <FpCommunity :data="data[0].section[0]" />
    </section>

    <!-- TODO: Our Sponsors -->
    <section class="w-10/12 mx-auto my-10">
      <h2
        class="text-5xl text-center mb-12 font-bold bg-clip-text text-transparent bg-gradient-to-r from-fp-green to-fp-blue-light"
      >
        Our Sponsors
      </h2>
    </section>

    <!-- Benefits of Sponsoring -->
    <section class="w-10/12 my-10">
      <header
        class="grid md:grid-cols-2 gap-4 md:w-11/12 mx-auto text-center md:text-left"
      >
        <h3
          class="text-fp-blue font-medium mb-4 xl:mb-6 md:col-span-2 xl:col-span-1"
        >
          {{ data[0].section[1].header.sectionTitle }}
        </h3>
      </header>
      <FpList columns="sm:grid-cols-2 gap-12 lg:gap-4">
        <FpListItem
          v-for="item in data[0].section[1].content.list"
          v-bind="item"
        />
      </FpList>
    </section>

  </main>
</template>
