<script setup>
</script>

<template>
  <footer class="text-center lg:text-left bg-gray-200 text-gray-600 min-w-full">
    <div class="mx-6 py-10 text-center md:text-left">
      <div class="grid grid-1 md:grid-cols-2 lg:grid-cols-4 gap-8">
        <div class="">
          <h6 class="uppercase font-semibold mb-4 flex justify-center md:justify-start">
            Desktops
          </h6>
          <li style="list-style-type: none" v-for="item in desktops" :key="item.name" class="mb-4">
            <a :href="`${
              item.href.includes('https')
                ? item.href
                : $config.app.baseURL + item.href
            }`" :class="['text-gray-600', 'text-base font-medium']">
              {{ item.name }}
            </a>
          </li>
        </div>

        <div class="">
          <h6 class="uppercase font-semibold mb-4 flex justify-center md:justify-start">
            Server / Cloud Deployment
          </h6>
          <li style="list-style-type: none" v-for="item in cloud" :key="item.name" class="mb-4">
            <a :href="`${
              item.href.includes('https')
                ? item.href
                : $config.app.baseURL + item.href
            }`" :class="['text-gray-600', 'text-base font-medium']">
              {{ item.name }}
            </a>
          </li>

          <h6 class="uppercase font-semibold mb-4 flex justify-center md:justify-start">
            IoT / Edge Deployment
          </h6>
          <li style="list-style-type: none" v-for="item in iot" :key="item.name" class="mb-4">
            <a :href="`${
              item.href.includes('https')
                ? item.href
                : $config.app.baseURL + item.href
            }`" :class="['text-gray-600', 'text-base font-medium']">
              {{ item.name }}
            </a>
          </li>
        </div>

        <div class="">
          <h6 class="uppercase font-semibold mb-4 flex justify-center md:justify-start">
            User Support
          </h6>
          <li style="list-style-type: none" v-for="item in support" :key="item.name" class="mb-4">
            <a :href="`${
              item.href.includes('https')
                ? item.href
                : $config.app.baseURL + item.href
            }`" :class="['text-gray-600', 'text-base font-medium']">
              {{ item.name }}
            </a>
          </li>
        </div>

        <div class="">
          <h6 class="uppercase font-semibold mb-4 flex justify-center md:justify-start">
            Community
          </h6>
          <li style="list-style-type: none" v-for="item in community" :key="item.name" class="mb-4">
            <a :href="`${
              item.href.includes('https')
                ? item.href
                : $config.app.baseURL + item.href
            }`" :class="['text-gray-600', 'text-base font-medium']">
              {{ item.name }}
            </a>
          </li>
        </div>
      </div>
    </div>

    <div class="py-10 text-center md:text-left">
      <div class="mx-6 grid md:grid-cols-2 lg:grid-cols-8">
        <div class="">
          <img src="~/assets/logos/fedora-blue.png" alt="Fedora Logo" class="w-1/2 ml-14 lg:ml-1 mb-4" />
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
