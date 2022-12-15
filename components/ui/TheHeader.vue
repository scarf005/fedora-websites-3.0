<script setup>
// logic for mobile detection

import TheMenuButton from "./TheMenuButton.vue";

// open menu function

// close menu function
</script>
<template>
  <header
    class="bg-gradient-to-tr from-fp-blue-light to-fp-blue dark:from-fp-blue dark:to-fp-blue-dark"
  >
    <div class="flex items-center justify-between py-2 px-4 lg:px-12">
      <TheHeaderLogo class="" />
      <TheNav class="hidden md:block" />
      <!-- Language, Darkmode, Search -->
      <!-- Hamburger Menu -->
      <TheMenuButton class="md:hidden" />
    </div>
  </header>
</template>
