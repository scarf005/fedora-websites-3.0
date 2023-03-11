<script setup>
// TODO: Move typewriter code into a composable and make it reusable
let typeValue = ref("");
let typeStatus = false;
const arr = ["Server.", "Workstation.", "Community.", "Operating System."];
const speed = 150;
const newTextDelay = 1000;
let arrIndex = 0;
let charIndex = 0;

function writeText() {
  if (charIndex < arr[arrIndex].length) {
    if (!typeStatus) typeStatus = true;
    typeValue.value += arr[arrIndex].charAt(charIndex);
    charIndex += 1;
    setTimeout(writeText, speed);
  } else {
    typeStatus = false;
    setTimeout(eraseText, newTextDelay);
  }
}
function eraseText() {
  if (charIndex > 0) {
    if (!typeStatus) typeStatus = true;
    typeValue.value = arr[arrIndex].substring(0, charIndex - 1);
    charIndex -= 1;
    setTimeout(eraseText, speed);
  } else {
    typeStatus = false;
    arrIndex += 1;
    if (arrIndex < arr.length) {
      setTimeout(writeText, speed + 1000);
    } else {
      typeValue.value = arr.slice(-1).join();
    }
  }
}

const supportCardIcon = (cardTitle) => {
  switch (cardTitle) {
    case "Documentation":
      return "fa6-solid:book";
      break;
    case "Support":
      return "fa6-solid:envelope";
      break;
    case "Chat":
      return "fa6-solid:comments";
      break;
  }
};

onMounted(() => {
  setTimeout(writeText, newTextDelay + 200);
});

const data = await getCMS("index");
useContentHead(data);
const release_data = await getCMS("release");

useHead({
  title: "Fedora Linux",
});
</script>
<template>
  <main class="w-full dark:bg-slate-900">
    <header
      class="min-h-5/6 -mb-1 flex flex-col bg-gradient-to-b from-fp-blue to-fp-newblue-500 pt-4 text-white md:pt-16"
    >
      <section
        class="container mx-auto flex max-w-7xl flex-col items-center text-center"
      >
        <!-- Main Info -->
        <div>
          <!-- TODO: Set up the typewriter to work with translation -->
          <h1
            class="mx-auto mb-4 text-4xl font-semibold md:text-7xl lg:mb-8 xl:text-9xl"
          >
            {{ $t("It's your") }}<br />&nbsp;<span>{{ typeValue }} </span>
          </h1>
          <p class="mx-auto mb-2 w-4/6 lg:mb-6 lg:text-3xl">
            {{ $t(data.description) }}
          </p>
          <p class="uppercase">{{ $t("100% Free & Open Source") }}</p>
        </div>
        <!-- Circle -->
        <div
          class="my-4 flex h-48 w-48 flex-col items-center justify-center rounded-full bg-blue-400 p-10 md:my-8 md:h-56 md:w-56 lg:p-12"
        >
          <p>{{ $t("Latest release") }}</p>
          <p class="text-8xl font-bold">{{ release_data.ga.releasever }}</p>
        </div>
      </section>
      <!-- pop out announcements -->
      <aside
        v-if="data.sections[0].sectionDescription === 'active'"
        class="order-first mb-8 flex items-center self-end rounded-l-md bg-fp-blue p-4 lg:w-1/4"
      >
        <p>{{ $t(data.sections[0].sectionTitle) }}</p>
      </aside>

      <!-- hero bottom content-->
      <section
        class="align-end mx-auto mb-2 flex w-full max-w-screen-2xl justify-between px-8 lg:mb-4 xl:px-20"
      >
        <div
          class="flex w-48 flex-col justify-center sm:justify-start md:max-w-sm lg:w-auto"
        >
          <FpLink
            :href="data.sections[1].url"
            class="transition duration-150 ease-in hover:text-fp-gray-lighter"
            v-if="data.sections[1].sectionDescription"
          >
            <h3
              class="text-base font-semibold uppercase sm:mt-6 md:text-xl lg:mt-8 xl:text-2xl 2xl:mb-2"
            >
              {{ $t(data.sections[1].sectionTitle) }}
            </h3>
            <p class="max-w-sm text-sm sm:text-base lg:text-xl">
              {{ $t(data.sections[1].sectionDescription) }} &gt;
            </p>
          </FpLink>
        </div>
        <div class="flex items-center gap-4">
          <h3 class="hidden w-56 text-right text-2xl md:block">
            {{ $t(data.sections[2].sectionTitle) }}
          </h3>
          <FpImage :src="data.header_images[0].image" class="w-28 lg:w-auto" />
        </div>
      </section>
      <svg
        xmlns="http://www.w3.org/2000/svg"
        fill="none"
        style="-webkit-print-color-adjust: exact"
        viewBox="3047 814.969 1200.032 142.328"
      >
        <path
          d="M3047 915v42.297h1200.032V814.969L3047 915Z"
          class="fill-gray-100 dark:fill-gray-900"
        />
      </svg>
    </header>

    <!-- 5 MAIN EDITIONS-->
    <section class="w-full bg-gray-100 dark:bg-gray-900">
      <header class="hidden">
        <h2 class="text-center">
          {{ $t(data.sections[3].sectionTitle) }}
        </h2>
      </header>
      <div
        class="container mx-auto flex flex-wrap justify-center gap-4 py-8 px-2 md:px-4 lg:gap-16"
      >
        <div
          class="relative my-4 w-full rounded-xl bg-white p-4 shadow-lg dark:bg-gray-800 lg:max-w-sm"
          v-for="item in data.sections[3].content"
        >
          <FpImage :src="item.image" class="-mt-16 mb-5" />
          <FpLink :href="item.url">
            <h3
              class="bg-gradient-to-r from-fp-green to-fp-newblue-500 bg-clip-text text-xl font-bold text-transparent lg:mb-4 lg:text-4xl"
            >
              {{ $t(item.title) }}
            </h3>
            <p class="mb-16 text-gray-700 dark:text-gray-300">
              {{ $t(item.description) }}
            </p>
          </FpLink>
          <div class="absolute bottom-6 right-4">
            <FpBtn :href="item.url">Learn More</FpBtn>
          </div>
        </div>
      </div>
    </section>
    <section
      class="container mx-auto my-8 bg-gradient-to-b from-fp-green/25 to-fp-blue/25 dark:from-fp-green-300/25 dark:to-fp-newblue/25 md:bg-gradient-to-r lg:my-16"
    >
      <header class="mx-4 pt-12 pb-4 lg:mx-auto lg:pb-8">
        <h2
          class="text-center font-semibold text-fp-darkblue dark:text-fp-newblue"
        >
          {{ $t(data.sections[4].sectionTitle) }}
        </h2>
      </header>

      <!-- WANT MORE FEDORA OPTIONS -->
      <div class="flex flex-wrap justify-center gap-4 pb-8 lg:gap-8">
        <article
          v-for="card in data.sections[4].content"
          :key="card.id"
          class="m-4 max-w-sm"
        >
          <div class="mb-2">
            <h3 class="font-semibold text-fp-darkblue dark:text-fp-newblue">
              {{ $t(card.title) }}
            </h3>
          </div>
          <div class="max-w-xs">
            <p class="mb-2 text-gray-900 dark:text-gray-300">
              {{ $t(card.description) }}
            </p>
            <FpLink
              :href="card.link.url"
              class="font-semibold text-fp-darkblue underline-offset-4 transition duration-150 ease-in hover:text-fp-newblue hover:underline dark:text-gray-300"
              >{{ $t(card.link.text) }}</FpLink
            >
          </div>
        </article>
      </div>
    </section>
    <section class="container mx-auto pb-8 lg:pb-12">
      <header class="mx-4 pt-12 pb-4 lg:mx-auto lg:pb-8">
        <h2
          class="text-center font-semibold text-fp-darkblue dark:text-fp-newblue"
        >
          {{ $t(data.sections[5].sectionTitle) }}
        </h2>
      </header>
      <div class="flex flex-wrap justify-center gap-4 pb-8 lg:gap-8">
        <article
          v-for="card in data.sections[5].content"
          :key="card.id"
          class="flex max-w-sm flex-col items-center rounded-md bg-gray-400 p-8 dark:bg-gray-800"
        >
          <div class="mb-2 flex gap-4">
            <h3 class="font-semibold text-fp-darkblue dark:text-fp-newblue">
              {{ $t(card.title) }}
            </h3>

            <Icon
              :name="supportCardIcon(card.title)"
              size="36"
              class="order-first text-fp-darkblue dark:text-fp-newblue"
            />
          </div>
          <div class="text-center">
            <p class="mb-2">{{ $t(card.description) }}</p>
            <NuxtLink
              :to="card.link.url"
              class="font-semibold underline-offset-1 transition duration-150 ease-in-out hover:text-fp-darkblue hover:underline hover:dark:text-fp-newblue"
              >{{ $t(card.link.text) }}</NuxtLink
            >
          </div>
        </article>
      </div>
    </section>
  </main>
</template>
