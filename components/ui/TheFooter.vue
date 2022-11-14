<script setup>
import { editions, others, support, community } from "~/composables/navigation";
</script>

<template>
  <footer class="min-w-full bg-gray-200 text-center text-gray-600 lg:text-left">
    <section class="mx-6 bg-red-500 py-10 text-center md:text-left">
      <div class="grid-1 grid gap-8 md:grid-cols-2 lg:grid-cols-4">
        <section class="bg-blue-500">
          <h6
            class="mb-4 flex justify-center font-semibold uppercase md:justify-start"
          >
            Editions
          </h6>
          <li v-for="item in editions" :key="item.id" class="mb-4 list-none">
            <NuxtLink
              :to="item.href"
              class="text-base font-medium text-gray-600"
            >
              {{ item.name }}
            </NuxtLink>
          </li>
        </section>
        <!-- Others -->
        <section class="">
          <h6
            class="mb-4 flex justify-center font-semibold uppercase md:justify-start"
          >
            Others
          </h6>
          <li v-for="item in others" :key="item.id" class="mb-4 list-none">
            <NuxtLink
              :to="item.href"
              class="text-base font-medium text-gray-600"
            >
              {{ item.name }}
            </NuxtLink>
          </li>
        </section>
        <!-- User Support -->
        <section class="">
          <h6
            class="mb-4 flex justify-center font-semibold uppercase md:justify-start"
          >
            User Support
          </h6>
          <li v-for="item in support" :key="item.id" class="mb-4 list-none">
            <NuxtLink
              to="item.href"
              class="text-base font-medium text-gray-600"
            >
              {{ item.name }}
            </NuxtLink>
          </li>
        </section>
        <!-- Community -->
        <section class="">
          <h6
            class="mb-4 flex justify-center font-semibold uppercase md:justify-start"
          >
            Community
          </h6>
          <li v-for="item in community" :key="item.id" class="mb-4 list-none">
            <NuxtLink
              :to="item.href"
              class="text-base font-medium text-gray-600"
            >
              {{ item.name }}
            </NuxtLink>
          </li>
        </section>
      </div>
    </section>

    <section class="py-10 text-center md:text-left">
      <div class="mx-6 grid md:grid-cols-2 lg:grid-cols-8">
        <div class="">
          <img
            src="~/assets/logos/fedora-blue.png"
            alt="Fedora Logo"
            class="ml-14 mb-4 w-1/2 lg:ml-1"
          />
        </div>

        <div class="mb-4">
          <a href="#!" class="text-gray-600">Privacy Statement</a>
        </div>
        <div class="mb-4">
          <a href="#!" class="text-gray-600">Legal</a>
        </div>
        <div class="mb-4">
          <a href="#!" class="text-gray-600">Code of Conduct</a>
        </div>
        <div class="mb-4">
          <a href="#!" class="text-gray-600">Sponsors</a>
        </div>
      </div>
    </section>

    <TheRedHatSponsoredBanner />
  </footer>
</template>
