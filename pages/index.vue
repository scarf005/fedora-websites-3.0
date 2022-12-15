<script setup>
definePageMeta({
  layout: "development",
});

// temporary  boolean
const announcement = true;
</script>
<template>
  <main class="">
    <header
      class="flex h-screen flex-col bg-gradient-to-tl from-fp-blue to-fp-blue-light pt-8 text-white lg:pt-12"
    >
      <section class="mx-auto flex max-w-7xl flex-col items-center text-center">
        <!-- Main Info -->
        <div class="container">
          <!-- TODO: Add dynamic changing of text in the span -->
          <h1 class="mx-auto mb-8 text-4xl font-semibold lg:text-9xl">
            It's your <span>operating</span> system.
          </h1>
          <p class="mx-auto mb-6 w-4/6 text-xl lg:text-3xl">
            An innovative platform for hardware, clouds, and containers, built
            with love by <strong>you</strong>
          </p>
          <p class="uppercase">100% Free & Open Source</p>
        </div>
        <!-- Circle -->
        <div class="mt-4 h-56 w-56 rounded-full bg-blue-400 p-8">
          <p>Latest release</p>
          <p class="text-8xl font-bold">37</p>
          <NuxtLink to="#" class="underline underline-offset-4"
            >Release Notes</NuxtLink
          >
        </div>
      </section>
      <!-- pop out announcements -->
      <aside
        v-if="announcement"
        class="order-first mb-3 flex h-12 items-center self-end rounded-md bg-fp-blue px-4 lg:w-1/4"
      >
        <p>placeholder text</p>
      </aside>

      <!-- hero bottom content-->
      <section
        class="mx-auto mt-16 flex w-full justify-center px-4 lg:mt-4 lg:justify-between lg:px-12"
      >
        <div class="container hidden lg:block">
          <h3 class="text-xl font-semibold uppercase">Next Upcoming Event</h3>
          <p class="max-w-sm">
            Lorem ipsum dolor sit amet consectetur adipisicing.
          </p>
        </div>
        <div class="container flex justify-end">
          <h3 class="text-center text-xl lg:w-56 lg:text-right lg:text-2xl">
            A Registered Digital Public Good
          </h3>
        </div>
      </section>
    </header>
  </main>
</template>
