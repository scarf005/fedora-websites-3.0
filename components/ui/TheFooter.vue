<script setup>
import { editions, others, support, community } from "../../config/navigation";
</script>

<template>
  <footer
    class="min-w-full bg-gray-200 text-center text-gray-600 dark:bg-neutral-800 dark:text-gray-100 lg:text-left"
  >
    <div class="mx-6 py-10 text-center md:text-left">
      <div class="grid-1 grid gap-8 md:grid-cols-2 lg:grid-cols-4">
        <div class="">
          <h6
            class="mb-4 flex justify-center font-semibold uppercase md:justify-start"
          >
            Editions
          </h6>
          <li
            style="list-style-type: none"
            v-for="item in editions"
            :key="item.name"
            class="mb-4"
          >
            <FpLink
              :href="item.href"
              class="text-base font-medium text-gray-600 dark:text-gray-300"
            >
              {{ item.name }}
            </FpLink>
          </li>
        </div>

        <div class="">
          <h6
            class="mb-4 flex justify-center font-semibold uppercase md:justify-start"
          >
            Others
          </h6>
          <li
            style="list-style-type: none"
            v-for="item in others"
            :key="item.name"
            class="mb-4"
          >
            <FpLink
              :href="item.href"
              class="text-base font-medium text-gray-600 dark:text-gray-300"
            >
              {{ item.name }}
            </FpLink>
          </li>
        </div>

        <div class="">
          <h6
            class="mb-4 flex justify-center font-semibold uppercase md:justify-start"
          >
            User Support
          </h6>
          <li
            style="list-style-type: none"
            v-for="item in support"
            :key="item.name"
            class="mb-4"
          >
            <FpLink
              :href="item.href"
              class="text-base font-medium text-gray-600 dark:text-gray-300"
            >
              {{ item.name }}
            </FpLink>
          </li>
        </div>

        <div class="">
          <h6
            class="mb-4 flex justify-center font-semibold uppercase md:justify-start"
          >
            Community
          </h6>
          <li
            style="list-style-type: none"
            v-for="item in community"
            :key="item.name"
            class="mb-4"
          >
            <FpLink
              :href="item.href"
              class="text-base font-medium text-gray-600 dark:text-gray-300"
            >
              {{ item.name }}
            </FpLink>
          </li>
        </div>
      </div>
    </div>

    <div class="py-10 text-center md:text-left">
      <div class="mx-6 grid md:grid-cols-2 lg:grid-cols-8">
        <div class="">
          <img
            src="~/assets/logos/fedora-blue.png"
            alt="Fedora Logo"
            class="ml-14 mb-4 w-1/2 lg:ml-1"
          />
        </div>

        <div class="mb-4">
          <a href="#!" class="text-gray-600 dark:text-gray-300"
            >Privacy Statement</a
          >
        </div>
        <div class="mb-4">
          <a href="#!" class="text-gray-600 dark:text-gray-300">Legal</a>
        </div>
        <div class="mb-4">
          <a href="#!" class="text-gray-600 dark:text-gray-300"
            >Code of Conduct</a
          >
        </div>
        <div class="mb-4">
          <a href="#!" class="text-gray-600 dark:text-gray-300">Sponsors</a>
        </div>
      </div>
    </div>

    <TheRedHatSponsoredBanner />
  </footer>
</template>
