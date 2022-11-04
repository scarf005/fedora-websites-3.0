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
          <article
            v-for="card in data.sections[1].content"
            :key="card.id"
            class="m-4 flex flex-col justify-between md:max-w-xs"
          >
            <h3
              class="mb-2 text-center text-2xl font-semibold text-fp-blue lg:text-start"
            >
              {{ card.title }}
            </h3>
            <p
              class="my-2 mx-auto hidden w-52 break-words text-center text-sm text-fp-gray-darkest sm:block lg:w-80 lg:text-start lg:text-base"
            >
              {{ card.description }}
            </p>
            <FpImage
              :image="card.image"
              :alt="card.image"
              class="my-2 mx-auto w-56"
            />
            <NuxtLink
              :to="card.link.url"
              class="my-2 mx-auto flex w-full justify-center rounded-lg bg-fp-blue-light py-2 font-medium text-white"
              >{{ card.link.text }}</NuxtLink
            >
          </article>
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

    <!-- Events -->
    <section>
      <div
        class="container my-12 mx-auto grid grid-cols-2 gap-4 lg:grid-cols-3 xl:gap-8"
      >
        <header
          class="container col-span-2 mx-auto flex flex-col justify-evenly"
        >
          <!-- Events Header -->
          <section class="xl-mx-0 mx-8 mb-8 text-center md:text-start">
            <h2 class="mb-4 text-fp-green xl:text-4xl">
              {{ data.sections[3].sectionTitle }}
            </h2>
            <p class="text-fp-gray-darkest">
              {{ data.sections[3].sectionDescription }}
            </p>
          </section>
          <!-- Flock Header -->
          <section class="xl-mx-0 mx-8 mb-8 flex flex-col self-center">
            <h3 class="text-center text-lg text-fp-blue-dark xl:text-xl">
              {{ data.sections[3].content[0].title }}
            </h3>
            <FpImage
              :image="data.sections[3].content[0].image"
              class="order-first mx-auto w-60 lg:max-w-lg"
            />
            <p class="my-0 text-fp-gray-darkest md:my-2">
              {{ data.sections[3].content[0].description }}
            </p>
            <div
              class="xl-mx-0 mt-6 w-full bg-pink-200 p-2 text-fp-gray-darkest lg:py-3 lg:pl-4"
            >
              <p>{{ data.sections[3].content[0].link.text }}</p>
            </div>
          </section>
        </header>

        <!-- Colur -->

        <figure
          class="col-start-3 row-start-1 hidden justify-self-start lg:block"
        >
          <FpImage
            :image="data.sections[3].content[1].image"
            class="w-48 lg:w-60"
          />
          <figcaption
            class="mt-2 text-center text-xs text-fp-gray-dark lg:mt-6"
          >
            {{ data.sections[3].content[1].description }}
          </figcaption>
        </figure>

        <!-- Flock and Hatch -->
        <div
          class="items-between xl-mx-0 col-span-2 mt-6 flex flex-wrap justify-center lg:justify-start"
        >
          <article
            v-for="card in data.sections[3].content.slice(3, 5)"
            :key="card.id"
            class="container my-4 mx-auto flex w-fit flex-col gap-y-4 md:w-1/2"
          >
            <h4 class="text-base text-fp-blue xl:text-lg">
              {{ card.title }}
            </h4>
            <p class="max-w-sm">{{ card.description }}</p>
            <div class="xl-mx-0 order-first">
              <FpImage :image="card.image" class="h-16" />
            </div>
          </article>
        </div>

        <!-- Recap Message -->
        <figure class="container col-start-3 mt-6 hidden lg:block">
          <NuxtLink
            to="https://www.youtube.com/watch?v=u9f4Oetofxk&list=PL0x39xti0_64ohxFQSqwTMCm2vX4r6IGr"
          >
            <FpImage :image="data.sections[3].content[2].image" class="w-72" />
          </NuxtLink>
          <figcaption class="mt-4 max-w-xs text-sm text-fp-gray-dark">
            {{ data.sections[3].content[2].description }}
          </figcaption>
        </figure>

        <!-- Fedora Release Parties -->
        <section
          class="col-span-full my-8 mx-8 flex flex-col items-center sm:mx-0 md:items-start"
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
          class="col-span-full flex w-full justify-center gap-8 self-center bg-gradient-to-r from-fp-green-light/40 to-fp-blue-light/40 p-12 lg:gap-16 xl:my-6 xl:py-20"
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

        <!-- become a fedora contributor -->
        <section class="col-span-full flex">
          <div>
            <h4 class="mb-2 text-sm font-medium text-fp-blue-light">
              {{ data.sections[3].content[7].title }}
            </h4>
            <p class="text-xs text-fp-gray-dark">
              {{ data.sections[3].content[7].description }}
            </p>
          </div>
          <FpImage
            :image="data.sections[3].content[7].image"
            class="order-first max-h-4"
          />
        </section>
      </div>
    </section>
    <!-- Blog and Magazine -->
    <section class="bg-fp-gray-lightest">
      <div
        class="container mx-auto grid grid-cols-1 gap-4 py-12 lg:grid-cols-2 lg:gap-10"
      >
        <header class="hidden">
          <h2>{{ data.sections[4].sectionTitle }}</h2>
        </header>

        <!-- Loop through publications -->
        <article
          v-for="card in data.sections[4].content.slice(0, 2)"
          :key="card.id"
          class="my-10 flex flex-col items-center justify-between lg:my-8"
        >
          <header class="xl-mx-0 mx-4 flex flex-col justify-end">
            <h3 class="hidden">{{ card.title }}</h3>
            <p class="mt-7 mb-1 max-w-prose text-fp-gray-darkest">
              {{ card.description }}
            </p>
            <FpBtn :url="card.link.url" class="mx-auto mt-10 px-4">{{
              card.link.text
            }}</FpBtn>
          </header>
          <div class="order-first mx-4 lg:mx-auto">
            <FpImage :image="card.image" class="mx-auto w-5/6" />
          </div>
        </article>
      </div>
    </section>
  </main>
</template>
