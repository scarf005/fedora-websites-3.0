<script setup>
import { editions, others, support, community } from "../../config/navigation";

let isOpen = ref(false);
</script>

<template>
  <footer class="flex flex-col bg-gray-200">
    <nav class="container mx-auto py-10">
      <div class="container grid gap-2 md:grid-cols-2 lg:grid-cols-4 lg:gap-8">
        <!-- Editions -->
        <TheFooterSection title="Editions" :navItems="editions" />
        <!-- Others -->
        <TheFooterSection title="Others" :navItems="others" />
        <!-- User Support -->
        <TheFooterSection title="User Support" :navItems="support" />
        <!-- Community -->
        <TheFooterSection title="Community" :navItems="community" />
      </div>
    </nav>
    <!-- Privacy Links -->
    <section class="container mx-auto py-10">
      <div class="flex flex-wrap items-center gap-4">
        <div class="">
          <img
            src="~/assets/logos/fedora-blue.png"
            alt="Fedora Logo"
            class="ml-6 w-1/3 xl:ml-0"
          />
        </div>
        <ul
          class="mx-4 flex grow justify-center gap-4 lg:mx-0 lg:gap-8 xl:justify-start"
        >
          <li class="list-none underline underline-offset-1">
            <NuxtLink
              to="#"
              class="text-fp-gray-darkest transition duration-300 ease-in-out hover:text-fp-gray"
              >Privacy Statement</NuxtLink
            >
          </li>
          <li class="list-none underline underline-offset-1">
            <NuxtLink
              to="#"
              class="text-fp-gray-darkest transition duration-300 ease-in-out hover:text-fp-gray"
              >Legal</NuxtLink
            >
          </li>
          <li class="list-none underline underline-offset-1">
            <NuxtLink
              to="#"
              class="text-fp-gray-darkest transition duration-300 ease-in-out hover:text-fp-gray"
              >Code of Conduct</NuxtLink
            >
          </li>
          <li class="list-none underline underline-offset-1">
            <NuxtLink
              to="#"
              class="text-fp-gray-darkest transition duration-300 ease-in-out hover:text-fp-gray"
              >Sponsors</NuxtLink
            >
          </li>
        </ul>
      </div>
    </section>
    <!-- Red Hat Sponsorship Section -->
    <TheRedHatSponsoredBanner />
  </footer>
</template>
