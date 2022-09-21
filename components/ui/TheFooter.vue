<script setup>
import {
  desktops,
  cloud,
  iot,
  support,
  community,
} from "../../config/navigation";
</script>

<template>
  <footer class="min-w-full bg-gray-200 text-center text-gray-600 lg:text-left">
    <div class="mx-6 py-10 text-center md:text-left">
      <div class="grid-1 grid gap-8 md:grid-cols-2 lg:grid-cols-4">
        <div class="">
          <h6
            class="mb-4 flex justify-center font-semibold uppercase md:justify-start"
          >
            Desktops
          </h6>
          <li
            style="list-style-type: none"
            v-for="item in desktops"
            :key="item.name"
            class="mb-4"
          >
            <a
              :href="`${
                item.href.includes('https')
                  ? item.href
                  : $config.app.baseURL + item.href
              }`"
              :class="['text-gray-600', 'text-base font-medium']"
            >
              {{ item.name }}
            </a>
          </li>
        </div>

        <div class="">
          <h6
            class="mb-4 flex justify-center font-semibold uppercase md:justify-start"
          >
            Server / Cloud Deployment
          </h6>
          <li
            style="list-style-type: none"
            v-for="item in cloud"
            :key="item.name"
            class="mb-4"
          >
            <a
              :href="`${
                item.href.includes('https')
                  ? item.href
                  : $config.app.baseURL + item.href
              }`"
              :class="['text-gray-600', 'text-base font-medium']"
            >
              {{ item.name }}
            </a>
          </li>

          <h6
            class="mb-4 flex justify-center font-semibold uppercase md:justify-start"
          >
            IoT / Edge Deployment
          </h6>
          <li
            style="list-style-type: none"
            v-for="item in iot"
            :key="item.name"
            class="mb-4"
          >
            <a
              :href="`${
                item.href.includes('https')
                  ? item.href
                  : $config.app.baseURL + item.href
              }`"
              :class="['text-gray-600', 'text-base font-medium']"
            >
              {{ item.name }}
            </a>
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
            <a
              :href="`${
                item.href.includes('https')
                  ? item.href
                  : $config.app.baseURL + item.href
              }`"
              :class="['text-gray-600', 'text-base font-medium']"
            >
              {{ item.name }}
            </a>
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
            <a
              :href="`${
                item.href.includes('https')
                  ? item.href
                  : $config.app.baseURL + item.href
              }`"
              :class="['text-gray-600', 'text-base font-medium']"
            >
              {{ item.name }}
            </a>
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
    </div>

    <TheRedHatSponsoredBanner />
  </footer>
</template>
