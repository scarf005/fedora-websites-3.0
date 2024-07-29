<script setup>
const data = await getCMS("events/flock");
useContentHead(data);

function getAttributions(items) {
  return items.filter((value) => value.attribution);
}
</script>
<template>
  <FlHero
    :background_image="data.header_images[1].image"
    :logo_image="data.header_images[0].image"
    :title="data.title"
    :description="data.description"
    :cta_links="data.links"
  >
    <template #herocontent>
      <div class="mx-auto flex max-w-screen-xl p-12" v-if="data.events.enabled">
        <div
          v-for="card in data.events.content"
          class="max-w-[17rem] rounded-lg dark:bg-black/70 bg-white/70 p-4 m-4"
        >
          <div class="text-lg font-semibold leading-none text-fp-blue">
            <FpImage
              class="inline h-10 max-w-none align-baseline ltr:mr-1 rtl:ml-1"
              :src="card.image"
            />
            {{ $t(card.title) }}
          </div>
          <p class="text-sm text-slate-300">{{ $t(card.description) }}</p>
        </div>
      </div>
    </template>
  </FlHero>

  <main class="flex flex-col items-center dark:bg-black">
    <!-- Explore -->
    <section
      class="w-full bg-slate-100 pb-10 dark:bg-slate-900"
      v-if="data.explore.enabled"
    >
      <div class="my-20 mx-auto w-10/12 max-w-screen-xl">
        <h2
          class="mx-auto mb-4 max-w-screen-md bg-gradient-to-r from-fp-purple via-fp-newblue-500 to-fp-purple bg-clip-text text-center text-3xl font-bold text-transparent sm:text-5xl md:mb-12 lg:text-7xl"
        >
          {{ $t(data.explore.sectionTitle) }}
        </h2>
        <div
          class="flex flex-wrap justify-between gap-4 text-center text-fp-darkblue-500 xl:gap-20"
        >
          <FpCard
            v-for="card in data.explore.content"
            :title="card.title"
            :description="card.description"
            :variants="['event']"
            class="grow basis-64"
          >
            <template #prepend>
              <FpCardImage slot="prepend" :src="card.image" />
            </template>
            <template #footer>
              <FpLink
                :href="card.link.url"
                v-if="card.link.url"
                class="underline underline-offset-1"
                >{{ $t(card.link.text) }}</FpLink
              >
            </template>
          </FpCard>
        </div>
      </div>
    </section>

    <!-- Showcase Section -->
    <section
      class="mx-auto w-full py-10 dark:bg-slate-800"
      v-if="data.showcase.enabled"
    >
      <header class="my-10 mx-auto w-10/12 max-w-screen-xl">
        <h2
          class="mx-auto mb-12 max-w-max bg-gradient-to-r from-fp-purple via-fp-newblue-500 to-fp-purple bg-clip-text text-center text-3xl font-bold text-transparent sm:text-5xl md:leading-normal lg:text-7xl"
        >
          {{ $t(data.showcase.sectionTitle) }}
        </h2>
        <p class="mx-auto max-w-prose text-center">
          {{ $t(data.showcase.sectionDescription) }}
        </p>
      </header>
      <div
        class="container mx-auto my-8 grid grid-flow-row-dense gap-8 md:grid-cols-2 xl:my-16 xl:grid-cols-3 xl:gap-8"
      >
        <div
          class="col-start-1 place-self-center lg:row-start-2 xl:row-start-3"
        >
          <article
            class="flex max-w-sm flex-col p-6"
            v-if="data.showcase.content[0]"
          >
            <h3 class="my-2 font-sans text-xl font-bold text-fp-blue">
              {{ $t(data.showcase.content[0].title) }}
            </h3>
            <FpImage
              :src="data.showcase.content[0].image"
              class="order-first w-full"
            />
            <p class="my-2 w-72">
              {{ $t(data.showcase.content[0].description) }}
            </p>
            <div
              class="mt-2 flex gap-4 text-xl"
              v-if="data.showcase.content[0].link.url"
            >
              <FpLink
                :href="data.showcase.content[0].link.url"
                class="rounded-md bg-fp-newblue-500 px-3 py-2 font-medium text-white duration-300 ease-in-out hover:bg-fp-blue"
              >
                {{ $t(data.showcase.content[0].link.text) }}
              </FpLink>
            </div>
          </article>
        </div>
        <div class="col-start-2 row-span-2 row-start-2 hidden xl:block">
          <FpImage
            :src="data.showcase.images[0].path"
            v-if="data.showcase.images[0]"
            :alt="$t(data.showcase.images[0].alt)"
            class="rounded-md object-cover"
          />
          <p v-else="data.showcase.images[0]">{{ $t("placeholder") }}</p>
        </div>
        <div
          class="xl:col-span-2 xl:col-start-1 xl:row-start-3 xl:place-self-center"
        >
          <FpImage
            :src="data.showcase.images[1].path"
            :alt="$t(data.showcase.images[1].alt)"
            v-if="data.showcase.images[1]"
            class="mx-auto rounded-md object-cover xl:w-48"
          />
          <p v-else="data.showcase.images[1]">{{ $t("placeholder") }}</p>
        </div>
        <div
          class="place-self-center md:col-start-2 lg:row-start-2 xl:col-start-3 xl:row-span-2 xl:justify-self-start"
        >
          <article
            class="flex max-w-sm flex-col p-6"
            v-if="data.showcase.content[1]"
            :alt="$t(data.showcase.content[1].alt)"
          >
            <h3 class="my-2 font-sans text-xl font-bold text-fp-blue">
              {{ $t(data.showcase.content[1].title) }}
            </h3>
            <FpImage
              :src="data.showcase.content[1].image"
              class="order-first -ml-3 w-5/6"
            />
            <p class="my-2 w-72">
              {{ $t(data.showcase.content[1].description) }}
            </p>
            <div
              class="mt-2 flex gap-4 text-xl"
              v-if="data.showcase.content[1].link.url"
            >
              <FpLink
                :href="data.showcase.content[1].link.url"
                class="rounded-md bg-fp-newblue-500 px-3 py-2 font-medium text-white duration-300 ease-in-out hover:bg-fp-blue"
              >
                {{ $t(data.showcase.content[1].link.text) }}
              </FpLink>
            </div>
          </article>
        </div>
        <div
          class="m-4 place-self-center md:m-0 xl:row-start-2 xl:justify-self-start"
        >
          <div
            class="mx-auto grid h-96 w-96 place-items-center rounded-md bg-black text-white xl:h-60 xl:w-80"
          >
            <FpImage
              :src="data.showcase.images[2].path"
              v-if="data.showcase.images[2]"
              :alt="$t(data.showcase.images[2].alt)"
              class="mx-auto rounded-md object-cover xl:w-48"
            />
            <p v-else="data.showcase.images[2]">{{ $t("placeholder") }}</p>
          </div>
        </div>

        <div
          class="col-start-1 row-span-2 row-start-1 hidden place-self-end xl:block"
        >
          <FpImage
            :src="data.showcase.images[3].path"
            v-if="data.showcase.images[3]"
            :alt="$t(data.showcase.images[3].alt)"
            class="h-1/2 w-fit rounded-md object-cover"
          />
          <p v-else="data.showcase.images[2]">{{ $t("placeholder") }}</p>
        </div>

        <div class="col-span-2 hidden md:block xl:order-first xl:col-start-2">
          <FpImage
            :src="data.showcase.images[4].path"
            v-if="data.showcase.images[4]"
            :alt="$t(data.showcase.images[4].alt)"
            class="w-full rounded-md object-cover xl:w-10/12"
          />
        </div>
      </div>
      <!-- <div class="my-8">
        <FpLink
          href="#"
          class="mx-auto block max-w-fit rounded-md bg-fp-purple px-8 py-3 text-2xl font-medium text-white"
          >{{ $t("Registration") }}</FpLink
        >
      </div> -->
    </section>

    <!-- Watch -->
    <section
      class="w-full bg-slate-100 pb-10 dark:bg-slate-900"
      v-if="data.watch.enabled"
    >
      <div class="my-20 mx-auto w-10/12 max-w-screen-xl">
        <h2
          class="mx-auto mb-4 max-w-screen-md bg-gradient-to-r from-fp-purple via-fp-newblue-500 to-fp-purple bg-clip-text text-center text-3xl font-bold text-transparent sm:text-5xl md:mb-12 lg:text-7xl"
        >
          {{ $t(data.watch.sectionTitle) }}
        </h2>

        <template v-for="channel in data.watch.content">
          <FpCard
            class="mt-8 rounded-lg bg-white p-8 dark:bg-slate-800"
            variant="wide"
          >
            <div class="flex flex-wrap justify-between gap-4">
              <FpCardImage
                slot="prepend"
                class="flex-grow basis-24 lg:max-w-prose"
                :src="channel.image.path"
              />
              <div class="my-auto">
                <FpCardTitle :title="channel.title" />
                <p
                  class="text-fp-gray-darkest dark:text-slate-200 2xl:max-w-prose"
                >
                  {{ $t(channel.description) }}
                </p>
                <FpLink
                  :href="channel.link.url"
                  class="text-fp-blue ltr:after:content-['→'] rtl:after:content-['←'] dark:text-fp-newblue-500"
                  >{{ $t(channel.link.text) }}&nbsp;
                </FpLink>
              </div>
            </div>
          </FpCard>
        </template>
      </div>
    </section>

    <!-- Community Section -->
    <section
      class="max-w-full py-10 dark:bg-slate-900"
      v-if="data.community.enabled"
    >
      <FpHero
        :background="data.community.image"
        alignment="bg-top"
        class="dark:!bg-none"
      >
        <section class="mx-auto w-10/12 max-w-screen-xl py-24">
          <h2
            class="mx-auto mb-12 max-w-max bg-gradient-to-r from-fp-purple via-fp-newblue-500 to-fp-purple bg-clip-text text-center text-3xl font-bold text-transparent sm:text-5xl lg:text-7xl"
          >
            {{ $t(data.community.sectionTitle) }}
          </h2>
          <div
            class="mx-0 mb-20 text-center text-lg text-fp-darkblue-500 dark:text-gray-300 sm:mx-20"
          >
            {{ $t(data.community.sectionDescription) }}
          </div>

          <FpList columns="sm:grid-cols-2">
            <FpListItem
              v-for="item in data.community.content"
              v-bind="item"
              :iconURI="item.image"
              :image="null"
            />
          </FpList>
        </section>
      </FpHero>
    </section>

    <!-- FAQ -->
    <section class="my-10 w-10/12" v-if="data.faq.enabled">
      <header
        class="mx-auto max-w-screen-xl text-center md:w-11/12 md:text-left"
      >
        <h2 class="mb-4 text-center text-5xl font-bold text-fp-blue">
          {{ $t(data.faq.sectionTitle) }}
        </h2>
      </header>
      <FpList columns="sm:grid-cols-1" :disableDots="true">
        <FpListItemDetails v-for="item in data.faq.content" v-bind="item" />
      </FpList>
    </section>

    <!-- Previous Sponsors -->
    <section class="mx-auto w-full py-10 dark:bg-slate-900">
      <h2
        class="mx-auto mb-12 max-w-max bg-gradient-to-r from-fp-purple via-fp-newblue-500 to-fp-purple bg-clip-text text-center text-3xl font-bold text-transparent sm:text-5xl lg:text-7xl"
      >
        {{ $t(data.sponsors.title) }}
      </h2>
      <FlSectionDescription :content="data.sponsors.description" />
      <div class="mx-auto flex flex-wrap justify-center max-w-screen-xl p-12">
        <div
          v-for="card in data.sponsors.content"
          class="max-w-[17rem] rounded-lg p-4 m-4 bg-gray-100 dark:bg-neutral-300"
        >
          <div class="text-lg font-semibold leading-none text-fp-blue">
            <FpImage
              class="inline mx-auto h-10 w-full object-contain"
              :src="card.image"
              :alt="'Logo for ' + card.name"
            />
          </div>
          <!-- <p class="text-sm text-slate-300">{{ $t(card.description) }}</p> -->
        </div>
        <!-- Benefits of Sponsoring -->
        <!-- <section class="my-10 w-10/12">
      <header
        class="mx-auto max-w-screen-xl text-center md:w-11/12 md:text-left"
      >
        <h3 class="mb-4 text-center font-medium text-fp-blue">
          {{ $t(sponsorsBenefits.sectionTitle) }}
        </h3>
      </header>
      <FpList columns="sm:grid-cols-2">
        <FpListItem v-for="item in sponsorsBenefits.content" v-bind="item" />
      </FpList>
    </section> -->
      </div>
    </section>

    <section
      class="py-12 px-4 dark:bg-black"
      v-if="getAttributions(data.header_images)"
    >
      <AdditionalLegalInformationSection
        :legal-notices="getAttributions(data.header_images)"
        :isMarkdown="true"
      />
    </section>
  </main>
</template>
