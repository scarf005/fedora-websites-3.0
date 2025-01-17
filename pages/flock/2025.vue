<script setup>
const data = await getCMS("events/flock/2025");
useContentHead(data);

function formatDate(dateStr) {
  const options = { month: "long", day: "2-digit" };
  return new Date(dateStr).toLocaleDateString("en-US", options);
}

function getImportantDateColor(status) {
  if (status == "pending") return "#b9daf0";
  if (status == "current") return "#c5eac0";
  if (status == "elapsed") return "#dedede";
  // default
  return "#dedede";
}

function getAttributions(items) {
  return items.filter((value) => value.attribution);
}

// the size units here are css classes from tailwind css
// https://tailwindcss.com/docs/width
// https://tailwindcss.com/docs/height
const sponsorLevels = [
  {
    id: "platinum",
    text: "Platinum Sponsors",
    imageStyle: "h-28",
    containerStyle: "w-[18rem] h-36",
  },
  {
    id: "gold",
    text: "Gold Sponsors",
    imageStyle: "h-20",
    containerStyle: "w-[17rem] h-28",
  },
  {
    id: "silver",
    text: "Silver Sponsors",
    imageStyle: "h-16",
    containerStyle: "w-[16rem] h-24",
  },
  {
    id: "bronze",
    text: "Bronze Sponsors",
    imageStyle: "h-10",
    containerStyle: "w-[15rem] h-20",
  },
  {
    id: "media",
    text: "Media Sponsors",
    imageStyle: "h-10",
    containerStyle: "w-[15rem] h-20",
  },
];
</script>
<template>
  <FlHero
    :background_image="data.header_images[1].image"
    :logo_image="data.header_images[0].image"
    :title="data.title"
    :description="data.description"
    :cta_links="data.links"
  >
    <template #location>
      <div
        class="mx-auto sm:-mt-10 max-w-xs text-right text-lg font-semibold uppercase text-white -mt-8 sm:max-w-lg sm:text-2xl"
      >
        {{ $t(data.location) }}
      </div>
    </template>
  </FlHero>

  <main class="flex flex-col items-center dark:bg-black">
    <!--Important Dates -->
    <section
      class="mx-auto w-full py-10 dark:bg-slate-900 bg-slate-200"
      id="dates"
    >
      <h2
        class="mx-auto mb-8 max-w-max bg-gradient-to-r from-fp-purple via-fp-newblue-500 to-fp-purple bg-clip-text text-center text-3xl font-bold text-transparent sm:text-5xl lg:text-7xl"
      >
        {{ $t(data.importantDates.title) }}
      </h2>
      <div
        class="mx-0 mb-16 text-center text-lg text-fp-darkblue-500 dark:text-gray-300 sm:mx-20"
      >
        {{ $t(data.importantDates.description) }}
      </div>
      <div
        class="container my-12 mx-auto grid grid-cols-2 gap-2 lg:grid-cols-4"
      >
        <FlFigure
          v-if="data.importantDates.leftImage.path"
          :path="data.importantDates.leftImage.path"
          :alt="data.importantDates.leftImage.alt"
          :caption="data.importantDates.leftImage.caption"
        />

        <section class="col-span-2">
          <div
            v-for="date in data.importantDates.content"
            class="mx-auto mb-10 flex justify-center gap-5 rounded-xl p-2"
            :style="{ backgroundColor: getImportantDateColor(date.status) }"
          >
            <div class="my-auto w-28 text-center">
              <h3 class="text-4xl font-semibold text-fp-blue">
                {{ formatDate(date.startDate) }}
              </h3>
            </div>
            <div class="text-center">
              <h3 class="text-2xl font-bold text-fp-blue">
                {{ $t(date.name) }}
              </h3>
              <p v-if="date.endDate" class="mb-2 text-fp-gray-darkest">
                {{ $t("Deadline:") }} {{ formatDate(date.endDate) }}
              </p>
              <p v-if="date.description" class="mb-2 text-fp-gray-darkest">
                {{ $t(date.description) }}
              </p>
              <div class="flex justify-evenly gap-4">
                <template v-for="link in date.link">
                  <FpLink
                    v-if="date.status != 'elapsed'"
                    :href="link.url"
                    class="font-bold dark:text-black underline"
                  >
                    {{ $t(link.text) }}
                  </FpLink>
                  <a
                    v-else="date.status != 'elapsed'"
                    class="text-gray-600 line-through"
                  >
                    {{ $t(link.text) }}
                  </a>
                </template>
              </div>
            </div>
          </div>
          <p
            class="text-center text-sm dark:text-fp-gray text-gray-600"
            v-if="data.importantDates.footerText"
          >
            {{ $t(data.importantDates.footerText) }}
          </p>
        </section>

        <FlFigure
          v-if="data.importantDates.rightImage.path"
          :path="data.importantDates.rightImage.path"
          :alt="data.importantDates.rightImage.alt"
          :caption="data.importantDates.rightImage.caption"
        />
      </div>
    </section>

    <!-- CFP -->

    <section class="w-10/12 mx-auto my-10" v-if="data.cfp.enabled" id="cfp">
      <header class="my-10 mx-auto w-10/12 max-w-screen-xl">
        <h2
          class="text-5xl text-center mb-12 font-bold bg-clip-text text-transparent bg-gradient-to-r from-fp-green to-fp-newblue-500"
        >
          {{ $t(data.cfp.sectionTitle) }}
        </h2>
      </header>

      <div class="mx-auto max-w-prose text-center">
        <!-- <div
        class="mx-auto max-w-lg text-center font-normal text-gray-600 dark:text-gray-300"
      > -->
        <div class="p-2">
          <FlSectionDescription
            :isMarkdown="true"
            v-if="data.cfp.sectionDescription"
            :content="data.cfp.sectionDescription"
          />
        </div>
        <div class="my-8" v-if="data.cfp.link.url">
          <FpLink
            :href="data.cfp.link.url"
            class="mx-auto block max-w-fit rounded-md bg-fp-purple px-8 py-3 text-2xl font-medium text-white"
          >
            {{ $t(data.cfp.link.text) }}
          </FpLink>
        </div>
      </div>
    </section>

    <!-- Event Schedule -->

    <section
      class="w-10/12 mx-auto my-10 w-full"
      v-if="data.schedule.enabled"
      id="schedule"
    >
      <header class="my-10 mx-auto w-10/12 max-w-screen-xl">
        <h2
          class="text-5xl text-center mb-12 font-bold bg-clip-text text-transparent bg-gradient-to-r from-fp-green to-fp-newblue-500"
        >
          {{ $t(data.schedule.sectionTitle) }}
        </h2>
      </header>

      <div class="mx-auto max-w-prose text-center">
        <!-- <div
        class="mx-auto max-w-lg text-center font-normal text-gray-600 dark:text-gray-300"
      > -->
        <div class="p-2">
          <FlSectionDescription
            v-if="data.schedule.sectionDescription"
            :content="data.schedule.sectionDescription"
          />
        </div>
      </div>
      <FlEventSchedule :activities="data.schedule.dates" />
      <div class="flex justify-center">
        <FpBtn :href="link.link.url" v-for="link in data.schedule.links">
          {{ link.link.text }}
        </FpBtn>
      </div>
    </section>

    <!-- Venue -->

    <!-- <section
      class="w-10/12 mx-auto my-10 w-full bg-slate-100 dark:bg-slate-800"
      v-if="data.venue.enabled"
    >
      <header class="my-10 mx-auto w-10/12 max-w-screen-xl">
        <h2
          class="text-5xl text-center mb-12 font-bold bg-clip-text text-transparent bg-gradient-to-r from-fp-green to-fp-newblue-500"
        >
          {{ $t(data.venue.sectionTitle) }}
        </h2>
      </header>

      <div class="mx-auto max-w-prose text-center">
        <!-- <div
        class="mx-auto max-w-lg text-center font-normal text-gray-600 dark:text-gray-300"
      > --
        <div class="p-2">
          <FlSectionDescription
            :isMarkdown="true"
            v-if="data.venue.sectionDescription"
            :content="data.venue.sectionDescription"
          />
        </div>
        <div class="p-2">
          {{ $t("The Venue is located at:") }}
          <AddressBlock
            :name="data.venue.name"
            :street1="data.venue.address.street1"
            :street2="data.venue.address.street2"
            :city="data.venue.address.city"
            :state="data.venue.address.state"
            :postcode="data.venue.address.postcode"
            :country="data.venue.address.country"
          />
        </div>
      </div>
    </section> -->

    <!-- Logistics -->

    <section
      class="w-10/12 mx-auto my-10 w-full"
      v-if="data.logistics.enabled"
      id="logistics"
    >
      <header class="my-10 mx-auto w-10/12 max-w-screen-xl">
        <h2
          class="text-5xl text-center mb-12 font-bold bg-clip-text text-transparent bg-gradient-to-r from-fp-green to-fp-newblue-500"
        >
          {{ $t(data.logistics.sectionTitle) }}
        </h2>
      </header>

      <div class="mx-auto max-w-prose text-center">
        <!-- <div
        class="mx-auto max-w-lg text-center font-normal text-gray-600 dark:text-gray-300"
      > -->
        <div class="p-2">
          <FlSectionDescription
            :isMarkdown="true"
            v-if="data.logistics.sectionDescription"
            :content="data.logistics.sectionDescription"
          />
        </div>
        <div class="p-2">
          <AddressBlock
            :name="data.logistics.hotel.name"
            :street1="data.logistics.hotel.address.street1"
            :street2="data.logistics.hotel.address.street2"
            :city="data.logistics.hotel.address.city"
            :state="data.logistics.hotel.address.state"
            :postcode="data.logistics.hotel.address.postcode"
            :country="data.logistics.hotel.address.country"
            :url="data.logistics.hotel.contact.url"
            :phone="data.logistics.hotel.contact.phone"
            :phone_e164="data.logistics.hotel.contact.phone_e164"
          />
        </div>
        <div class="my-8" v-if="data.logistics.hotel.booking_url">
          <FpLink
            :href="data.logistics.hotel.booking_url"
            class="mx-auto block max-w-fit rounded-md bg-fp-purple px-8 py-3 text-2xl font-medium text-white"
            >{{ $t("Book Now") }}</FpLink
          >
        </div>
      </div>
    </section>

    <!-- Explore -->
    <!-- <section class="w-full bg-slate-100 pb-10 dark:bg-slate-900" v-if="data.explore.enabled">
      <div class="my-20 mx-auto w-10/12 max-w-screen-xl">
        <h2
          class="mx-auto mb-4 max-w-screen-md bg-gradient-to-r from-fp-purple via-fp-newblue-500 to-fp-purple bg-clip-text text-center text-3xl font-bold text-transparent sm:text-5xl md:mb-12 lg:text-7xl"
        >
          {{ $t(explore.sectionTitle) }}
        </h2>
        <div
          class="flex flex-wrap justify-between gap-4 text-center text-fp-darkblue-500 dark:text-gray-300 xl:gap-20"
        >
          <FpCard
            v-for="card in explore.content"
            :title="card.title"
            :description="card.description"
            :variants="['event']"
            class="h-80 grow basis-64"
          >
            <template #prepend>
              <FpCardImage slot="prepend" :src="card.image" />
            </template>
            <template #footer>
              <FpLink
                :href="card.link.url"
                class="underline underline-offset-1"
                >{{ $t(card.link.text) }}</FpLink
              >
            </template>
          </FpCard>
        </div>

        <h3
          class="mt-20 text-center text-2xl font-semibold text-fp-darkblue-500 dark:text-fp-newblue-500 sm:text-4xl"
        >
          {{ $t(watch.sectionTitle) }}
        </h3>

        <FpCard
          class="mt-8 rounded-lg bg-white p-8 dark:bg-slate-800"
          variant="wide"
        >
          <div class="flex flex-wrap justify-between gap-8">
            <FpCardImage
              slot="prepend"
              class="flex-grow basis-24 lg:max-w-prose"
              src="public/assets/images/flock_youtube.png"
            />
            <div class="my-auto">
              <FpCardTitle :title="watch.content[0].title" />
              <p
                class="text-fp-gray-darkest dark:text-slate-200 2xl:max-w-prose"
              >
                {{ $t(watch.content[0].description) }}
              </p>
              <FpLink
                :href="watch.content[0].image"
                class="text-fp-blue ltr:after:content-['→'] rtl:after:content-['←'] dark:text-fp-newblue-500"
                >{{ $t("Visit Fedora Youtube") }}&nbsp;
              </FpLink>
            </div>
          </div>
        </FpCard>
      </div>
    </section> -->

    <!-- <section class="mx-auto w-full py-10 dark:bg-slate-800" v-if="data.showcase.enabled">
      <header class="my-10 mx-auto w-10/12 max-w-screen-xl">
        <h2
          class="mx-auto mb-12 max-w-max bg-gradient-to-r from-fp-purple via-fp-newblue-500 to-fp-purple bg-clip-text text-center text-3xl font-bold text-transparent sm:text-5xl md:leading-normal lg:text-7xl"
        >
          {{ $t(hybrid.sectionTitle) }}
        </h2>
        <p class="mx-auto max-w-prose text-center">
          {{ $t(hybrid.sectionDescription) }}
        </p>
      </header>
      <div
        class="container mx-auto my-8 grid grid-flow-row-dense gap-8 md:grid-cols-2 xl:my-16 xl:grid-cols-3 xl:gap-8"
      >
        <div
          class="col-start-1 place-self-center lg:row-start-2 xl:row-start-3"
        >
          <article class="flex max-w-sm flex-col p-6">
            <h3 class="my-2 font-sans text-xl font-bold text-fp-blue">
              {{ $t(hybrid.content[0].title) }}
            </h3>
            <FpImage
              :src="hybrid.content[0].image"
              class="order-first w-full"
            />
            <p class="my-2 w-72">
              {{ $t(hybrid.content[0].description) }}
            </p> -->
    <!-- Content will need to be dynamic-->
    <!-- <div class="mt-2 flex gap-4 text-xl">
              <FpLink
                href="#"
                class="rounded-md bg-fp-newblue-500 px-3 py-2 font-medium text-white duration-300 ease-in-out hover:bg-fp-blue"
                >{{ $t("Destination") }}</FpLink
              >
              <FpLink
                href="#"
                class="px-3 py-2 font-medium text-fp-blue underline underline-offset-1 duration-300 ease-in-out hover:text-fp-darkblue-500"
                >{{ $t("Learn More") }}</FpLink
              >
            </div>
          </article>
        </div>
        <div class="col-start-2 row-span-2 row-start-2 hidden xl:block">
          <FpImage
            src="public/assets/images/people-presenting.png"
            class="rounded-md object-cover"
          />
        </div>
        <div
          class="xl:col-span-2 xl:col-start-1 xl:row-start-3 xl:place-self-center"
        >
          <FpImage
            src="public/assets/images/two-people-at-conf.png"
            class="mx-auto rounded-md object-cover xl:w-48"
          />
        </div>
        <div
          class="place-self-center md:col-start-2 lg:row-start-2 xl:col-start-3 xl:row-span-2 xl:justify-self-start"
        >
          <article class="flex max-w-sm flex-col p-6">
            <h3 class="my-2 font-sans text-xl font-bold text-fp-blue">
              {{ $t(hybrid.content[1].title) }}
            </h3>
            <FpImage
              :src="hybrid.content[1].image"
              class="order-first -ml-3 w-5/6"
            />
            <p class="my-2 w-72">
              {{ $t(hybrid.content[1].description) }}
            </p> -->
    <!-- Content will need to be dynamic-->
    <!-- <div class="mt-2 flex gap-4 text-xl">
              <FpLink
                href="#"
                class="rounded-md bg-fp-newblue-500 px-3 py-2 font-medium text-white duration-300 ease-in-out hover:bg-fp-blue"
                >{{ $t("Destination") }}</FpLink
              >
              <FpLink
                href="#"
                class="px-3 py-2 font-medium text-fp-blue underline underline-offset-1 duration-300 ease-in-out hover:text-fp-darkblue-500"
                >{{ $t("Learn More") }}</FpLink
              >
            </div>
          </article>
        </div>
        <div
          class="m-4 place-self-center md:m-0 xl:row-start-2 xl:justify-self-start"
        >
          <div
            class="mx-auto grid h-96 w-96 place-items-center rounded-md bg-black text-white xl:h-60 xl:w-80"
          >
            <p>{{ $t("placeholder") }}</p>
          </div>
        </div>

        <div
          class="col-start-1 row-span-2 row-start-1 hidden place-self-end xl:block"
        >
          <FpImage
            src="public/assets/images/people-posing-destination-bg.png"
            class="h-1/2 w-fit rounded-md object-cover"
          />
        </div>

        <div class="col-span-2 hidden md:block xl:order-first xl:col-start-2">
          <FpImage
            src="public/assets/images/bridge.png"
            class="w-full rounded-md object-cover xl:w-10/12"
          />
        </div>
      </div>
      <div class="my-8">
        <FpLink
          href="#"
          class="mx-auto block max-w-fit rounded-md bg-fp-purple px-8 py-3 text-2xl font-medium text-white"
          >{{ $t("Registration") }}</FpLink
        >
      </div>
    </section>-->

    <!-- Community Section -->
    <!-- <section class="max-w-full py-10 dark:bg-slate-900">
      <FpHero
        :background="community.image"
        alignment="bg-top"
        class="dark:!bg-none"
      >
        <section class="mx-auto w-10/12 max-w-screen-xl py-24">
          <h2
            class="mx-auto mb-12 max-w-max bg-gradient-to-r from-fp-purple via-fp-newblue-500 to-fp-purple bg-clip-text text-center text-3xl font-bold text-transparent sm:text-5xl lg:text-7xl"
          >
            {{ $t(community.sectionTitle) }}
          </h2>
          <div
            class="mx-0 mb-20 text-center text-lg text-fp-darkblue-500 dark:text-gray-300 sm:mx-20"
          >
            {{ $t(community.sectionDescription) }}
          </div>

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
    </section> -->

    <!-- Social Activities -->
    <section
      class="mx-auto w-full py-10 dark:bg-slate-800 bg-slate-50"
      v-if="data.social.enabled"
      id="social-activities"
    >
      <header class="my-10 mx-auto w-10/12 max-w-screen-xl">
        <h2
          class="mx-auto mb-12 max-w-max bg-gradient-to-r from-fp-purple via-fp-newblue-500 to-fp-purple bg-clip-text text-center text-3xl font-bold text-transparent sm:text-5xl md:leading-normal lg:text-7xl"
        >
          {{ $t(data.social.sectionTitle) }}
        </h2>
        <FlSectionDescription
          :content="data.social.sectionDescription"
          v-if="data.social.sectionDescription"
        />
      </header>
      <FlEventSchedule :activities="data.social.dates" />
    </section>

    <!-- FAQ -->
    <section class="my-10 w-10/12" v-if="data.faq.enabled" id="faq">
      <header
        class="mx-auto max-w-screen-xl text-center md:w-11/12 md:text-left"
      >
        <h2 class="mb-4 text-center text-5xl font-bold text-fp-blue">
          {{ $t(data.faq.sectionTitle) }}
        </h2>
        <FlSectionDescription
          :content="data.faq.sectionDescription"
          v-if="data.faq.sectionDescription"
        />
      </header>
      <FpList columns="sm:grid-cols-1" :disableDots="true">
        <FpListItemDetails v-for="item in data.faq.content" v-bind="item" />
      </FpList>
    </section>

    <!-- Our Sponsors -->
    <section
      class="mx-auto w-full py-10 dark:bg-slate-900 bg-slate-200"
      id="sponsors"
    >
      <h2
        class="mx-auto mb-12 max-w-max bg-gradient-to-r from-fp-purple via-fp-newblue-500 to-fp-purple bg-clip-text text-center text-3xl font-bold text-transparent sm:text-5xl lg:text-7xl"
      >
        {{ $t(data.sponsors.title) }}
      </h2>
      <!-- TODO: separate out into a new component -->
      <FlSectionDescription :content="data.sponsors.description" />
      <template v-for="sponsorLevel in sponsorLevels">
        <template
          v-if="
            data.sponsors.content.filter((s) => s.level === sponsorLevel.id)
              .length > 0
          "
        >
          <h3 class="mx-auto mb-12 max-w-max mt-10">
            {{ $t(sponsorLevel.text) }}
          </h3>

          <div class="mx-auto flex flex-wrap justify-center max-w-screen-xl">
            <div
              v-for="sponsor in data.sponsors.content.filter(
                (s) => s.level === sponsorLevel.id,
              )"
              class="rounded-lg bg-black/70 p-4 m-4 bg-gray-100 dark:bg-neutral-300 flex flex-col justify-center"
              :class="sponsorLevel.containerStyle"
            >
              <FpLink
                :href="sponsor.link"
                :title="'Visit the ' + sponsor.name + ' website'"
              >
                <FpImage
                  class="inline mx-auto w-full object-contain"
                  :class="sponsorLevel.imageStyle"
                  :src="sponsor.image"
                  :alt="sponsor.alt || 'Logo for ' + sponsor.name"
                />
              </FpLink>
            </div>
          </div>
        </template>
      </template>
    </section>

    <!-- Benefits of Sponsoring -->
    <section
      class="my-10 w-10/12"
      v-if="data.sponsoring.enabled"
      id="sponsoring"
    >
      <header
        class="mx-auto max-w-screen-xl text-center md:w-11/12 md:text-left"
      >
        <h3 class="text-4xl mb-4 text-center font-bold text-fp-blue">
          {{ $t(data.sponsoring.sectionTitle) }}
        </h3>
      </header>

      <div
        class="mx-auto max-w-lg text-center font-normal text-gray-600 dark:text-gray-300"
      >
        <div class="p-2">
          <FlSectionDescription
            :isMarkdown="true"
            v-if="data.sponsoring.sectionDescription"
            :content="data.sponsoring.sectionDescription"
          />
        </div>
      </div>

      <FpList columns="sm:grid-cols-2 mt-10">
        <FpListItem v-for="item in data.sponsoring.content" v-bind="item" />
      </FpList>

      <div class="my-8" v-if="data.sponsoring.prospectus.text">
        <a
          :href="
            $config.app.baseURL.replace(new RegExp('/$'), '') +
            '/' +
            data.sponsoring.prospectus.url.replace('public/', '')
          "
          class="mx-auto block max-w-fit rounded-md bg-fp-purple px-8 py-3 text-2xl font-medium text-white"
        >
          {{ $t(data.sponsoring.prospectus.text) }}
        </a>
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
