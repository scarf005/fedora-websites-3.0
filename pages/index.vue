<script setup>
let typeValue = ref("");
let typeStatus = false;
const arr = [
  "Workspace.",
  "Server.",
  "Game Center.",
  "Studio.",
  "Community.",
  "Operating System.",
  "Cloud.",
];
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
      typeValue.value = arr[4];
    }
  }
}

onMounted(() => {
  setTimeout(writeText, newTextDelay + 200);
});

const data = await getCMS("index");
useContentHead(data);
const release_data = await getCMS("release");
</script>
<template>
  <main class="w-full">
    <header
      class="flex min-h-screen flex-col bg-gradient-to-b from-fp-blue to-fp-blue-light pt-16 text-white"
    >
      <section
        class="container mx-auto flex max-w-7xl flex-col items-center text-center"
      >
        <!-- Main Info -->
        <div>
          <h1 class="mx-auto mb-8 text-3xl font-semibold md:text-9xl">
            It's your <br />&nbsp;<span>{{ typeValue }} </span>
          </h1>
          <p class="mx-auto mb-6 w-4/6 text-3xl">
            An innovative platform for hardware, clouds, and containers, built
            with love by <strong>you</strong>
          </p>
          <p class="uppercase">100% Free & Open Source</p>
        </div>
        <!-- Circle -->
        <div class="mt-8 h-56 w-56 rounded-full bg-blue-400 p-12">
          <p>Latest release</p>
          <p class="text-8xl font-bold">{{ release_data.ga.releasever }}</p>
        </div>
      </section>
      <!-- pop out announcements -->
      <aside
        v-if="data.sections[0].sectionDescription === 'active'"
        class="order-first mb-8 flex w-1/4 items-center self-end rounded-l-md bg-fp-blue p-4"
      >
        <p>{{ data.sections[0].sectionTitle }}</p>
      </aside>

      <!-- hero bottom content-->
      <section class="align-end mx-auto flex w-full justify-between px-16">
        <div>
          <h3 class="text-xl font-semibold uppercase">
            {{ data.sections[1].sectionTitle }}
          </h3>
          <FpLink class="max-w-sm" :href="data.sections[1].url">
            {{ data.sections[1].sectionDescription }} >
          </FpLink>
        </div>
        <div class="hidden md:flex">
          <h3 class="mr-5 w-56 text-right text-2xl">
            {{ data.sections[2].sectionTitle }}
          </h3>
          <FpImage :src="data.sections[2].image" />
        </div>
      </section>
    </header>
    <div class="w-full bg-gray-100 dark:bg-gray-900">
      <div class="mx-auto grid max-w-5xl grid-cols-2 py-5">
        <FpLink v-for="item in data.sections[3].content" :href="item.url">
          <div
            class="shadows-lg m-5 rounded-3xl bg-white p-5 pt-8 dark:bg-gray-800"
          >
            <h2
              class="mb-12 bg-gradient-to-r from-fp-green to-fp-blue-light bg-clip-text text-center text-xl font-bold text-transparent lg:text-5xl"
            >
              {{ $t(item.title) }}
            </h2>
          </div>
        </FpLink>
      </div>
    </div>
  </main>
</template>
