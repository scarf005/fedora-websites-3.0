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
      <h2 class="text-white mt-3 font-semibold">
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
    <!-- Community Section -->
    <section>
      <FpCommunity :data="data[0].section[0]" />
    </section>
  </main>
</template>
