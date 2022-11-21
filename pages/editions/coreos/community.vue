<script setup>
const { locale } = useI18n();

let { data } = await useAsyncData("page-data", () => {
  return queryContent("/editions/coreos/community/" + locale._value).findOne();
});

if (data._value === null) {
  ({ data } = await useAsyncData("page-data-fallback", () => {
    return queryContent("/editions/coreos/community").sort().find();
  }));
  data._value = data._value[data._value.length - 1];
}

useContentHead(data);
</script>

<template>
  <main class="mt-4 border-t-8 border-fp-magenta">
    <header>
      <TheLocalBar
        image="assets/images/fedora-coreos-logo.png"
        home="/editions/coreos"
        :items="[
          { name: 'Download', link: '/editions/coreos/download' },
          { name: 'Community', link: '/editions/coreos/community' },
          { name: 'Help', link: '/editions/coreos/help' },
        ]"
      />
      <section class="my-8 mx-auto px-8 text-center lg:text-start xl:px-0">
        <div class="container mx-auto">
          <h1 class="mb-4 text-fp-magenta xl:mb-8">{{ data.title }}</h1>
          <p class="text-fp-gray">{{ data.description }}</p>
        </div>
      </section>
      <section class="mx-auto bg-fp-magenta-light/5">
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
    <section class="mx-auto bg-fp-magenta-light/10">
      <div class="container mx-auto flex flex-col justify-center pb-8">
        <header class="py-8 text-center xl:text-start">
          <h2 class="text-fp-magenta xl:text-4xl">
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
        <FpJoinTip
          description="Your friendly and helpful contributions to these communication channels would be greatly appreciated"
        />
      </div>
    </section>

    <!-- ways to get involved -->
    <section class="bg-fp-magenta-light/5">
      <div
        class="container mx-auto grid justify-center gap-8 py-12 lg:grid-cols-2 lg:justify-start xl:py-8"
      >
        <header class="col-span-full my-8 mx-auto text-center lg:text-start">
          <h2 class="text-fp-magenta xl:text-4xl">
            {{ data.sections[2].sectionTitle }}
          </h2>
        </header>
        <div
          v-for="content in data.sections[2].content.slice(0, 2)"
          :key="content.id"
          class="mx-auto max-w-lg text-center lg:text-start"
        >
          <h3 class="font-medium text-fp-magenta">{{ content.title }}</h3>
          <p class="max-w-sm text-fp-gray-darkest">{{ content.description }}</p>
        </div>
        <FpJoinTip
          description="Attending a meeting or reporting and discussing issues you've found can be a great first step at contribution"
        />
      </div>
    </section>
  </main>
</template>
