<script setup>
import { editions, others, support, community } from "../../config/navigation";
</script>

<template>
  <footer class="flex flex-col bg-gray-200 dark:bg-neutral-900">
    <nav class="container mx-auto py-10">
      <div class="container grid gap-2 md:grid-cols-2 lg:grid-cols-4 lg:gap-8">
        <FpCollapsibleSection
          title="Editions"
          :navItems="editions"
          use="footer"
        />
        <FpCollapsibleSection title="Others" :navItems="others" use="footer" />
        <FpCollapsibleSection
          title="User Support"
          :navItems="support"
          use="footer"
        />
        <FpCollapsibleSection
          title="Community"
          :navItems="community"
          use="footer"
        />
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
    <section class="bg-black py-10 text-center md:text-left">
      <div class="container mx-auto flex flex-col lg:flex-row">
        <div class="mx-auto lg:mx-0 lg:basis-3/12">
          <FpImage
            src="assets/images/logo-sponsored-by-red-hat.png"
            alt="Sponsored by Red Hat Logo"
            class="mb-4 xl:mb-0"
          />
        </div>

        <div class="container text-center lg:text-left">
          <p class="text-white">
            Fedora is sponsored by Red Hat.
            <span class="block text-fp-gray xl:ml-2 xl:inline">
              Learn more about the relationship between Red Hat and Fedora.
            </span>
          </p>
        </div>
      </div>
    </section>
  </footer>
</template>
