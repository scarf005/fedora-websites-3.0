<script setup>
let typeValue = ref("");
let typeStatus = false;
const arr = [
  "Workspace",
  "Game Center",
  "Studio",
  "Community",
  "Operating System",
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
</script>
<template>
  <main class="w-full">
    <header
      class="flex min-h-screen flex-col bg-gradient-to-tl from-fp-blue to-fp-blue-light pt-16 text-white"
    >
      <section
        class="container mx-auto flex max-w-7xl flex-col items-center text-center"
      >
        <!-- Main Info -->
        <div>
          <!-- TODO: Add dynamic changing of text in the span -->
          <h1 class="mx-auto mb-8 text-3xl font-semibold md:text-9xl">
            It's your <br /><span>{{ typeValue }} </span>.
          </h1>
          <p class="mx-auto mb-6 w-4/6 text-3xl">
            An innovative platform for hardware, clouds, and containers, built
            with love by <strong>you</strong>
          </p>
          <p class="uppercase">100% Free & Open Source</p>
        </div>
        <!-- Circle -->
        <div class="mt-8 h-56 w-56 rounded-full bg-blue-400 p-8">
          <p>Latest release</p>
          <p class="text-8xl font-bold">37</p>
          <NuxtLink to="#" class="underline underline-offset-4"
            >Release Notes</NuxtLink
          >
        </div>
      </section>
      <!-- pop out announcements -->
      <aside
        class="order-first mb-8 flex h-16 w-1/4 items-center self-end rounded-md bg-fp-blue px-4"
      >
        <p>placeholder text</p>
      </aside>

      <!-- hero bottom content-->
      <section class="align-end mx-auto flex w-full justify-between px-16">
        <div>
          <h3 class="text-xl font-semibold uppercase">Next Upcoming Event</h3>
          <p class="max-w-sm">
            Lorem ipsum dolor sit amet consectetur adipisicing >
          </p>
        </div>
        <div>
          <h3 class="w-56 text-right text-2xl">
            A Registered Digital Public Good
          </h3>
        </div>
      </section>
    </header>
  </main>
</template>
