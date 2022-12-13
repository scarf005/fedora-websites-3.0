<script setup>
const { data } = await useAsyncData("navigation", () =>
  queryContent("_navigation").findOne()
);
const downloads = data._value.downloads;
const community = data._value.community;
const contributors = data._value.contributors;
const support = data._value.support;
</script>
<template>
  <nav
    class="bg-gradient-to-tr from-fp-blue-light to-fp-blue dark:from-fp-blue dark:to-fp-blue-dark"
  >
    <!-- layout div-->
    <div class="flex items-center justify-between gap-4 px-6 py-2 lg:py-4">
      <!-- Logo-->
      <div class="flex items-center gap-2 text-white">
        <Icon name="fa6-brands:fedora" size="48" />
        <!-- render fedora on desktop and take page category on mobile-->
        <span class="font-sans text-2xl font-semibold lg:text-3xl">Fedora</span>
      </div>
      <!-- Navigation Links -->
      <div>
        <ul></ul>
      </div>

      <!-- Hamburger Toggle-->
      <div class="text-white md:hidden">
        <button @click.prevent="">
          <Icon name="fa6-solid:bars" class="text-xl" size="32" />
        </button>
      </div>
    </div>
  </nav>
</template>
