<script setup>
const data = await getCMS("atomic-desktops/kinoite/home");
useContentHead(data);
</script>
<template>
  <section
    class="fp-banner to-fp-white relative bg-gradient-to-b from-teal-700 pt-6 dark:to-neutral-900"
  >
    <TheLocalBar
      :image="{
        light: 'assets/images/fedora-kinoite-logo-dark.png',
        dark: 'assets/images/fedora-kinoite-logo-dark.png',
      }"
      home="/kinoite"
      :items="[
        { name: 'Download', link: '/atomic-desktops/kinoite/download' },
        { name: 'Community', link: '/atomic-desktops/kinoite/community' },
      ]"
    />
    <FpBanner
      :title="data.title"
      :subtitle="data.leadin"
      :ctas="data.links"
      color="text-fp-blue"
      border="border border-fp-blue dark:border-fp-blue-700"
      background="text-white bg-fp-blue dark:bg-fp-blue-700"
    >
      <div class="hero-laptop-container">
        <div class="px-auto mb-20 max-w-sm sm:max-w-2xl">
          <div class="laptop-with-overlay relative mt-2 mb-3">
            <FpImage
              class="img-fluid relative mt-3"
              :src="data.header_images[0].image"
              :alt="data.header_images[0].text"
            />
            <div class="absolute top-0 left-0 ml-[10%] mt-[2%] w-[80%]">
              <FpImage
                class="img-fluid"
                :src="data.header_images[1].image"
                :alt="data.header_images[1].text"
              />
            </div>
          </div>
        </div>
      </div>
    </FpBanner>
  </section>

  <!-- why fedora kinoite -->
  <section class="mx-auto max-w-screen-xl px-6 py-12">
    <header
      class="mx-auto grid max-w-screen-xl gap-4 p-2 text-center md:grid-cols-2 md:p-0 md:text-left"
    >
      <h3
        class="mb-4 font-medium text-fp-green md:col-span-2 xl:col-span-1 xl:mb-6"
      >
        {{ $t(data.sections[0].sectionTitle) }}
      </h3>
    </header>
    <FpList columns="sm:grid-cols-2 gap-12 lg:gap-4 workstation-accent">
      <FpListItem v-for="item in data.sections[0].content" v-bind="item" />
    </FpList>
  </section>

  <svg
    width="614.927"
    height="101.23"
    class="absolute right-0 -z-10 dark:hidden"
    id="screenshot-00734247-430e-11ed-8d85-8fd7de2f268d"
    viewBox="961 1746 614.92701 101.23"
    style="-webkit-print-color-adjust: exact"
    fill="none"
    version="1.1"
    xmlns="http://www.w3.org/2000/svg"
    xmlns:svg="http://www.w3.org/2000/svg"
  >
    <defs id="defs2340"></defs>
    <g
      id="shape-00734247-430e-11ed-8d85-8fd7de2f268d"
      transform="translate(0,-1.659)"
    >
      <g class="fills" id="fills-00734247-430e-11ed-8d85-8fd7de2f268d">
        <path
          rx="0"
          ry="0"
          d="m 961,1796.942 614.927,-49.283 v 101.23 z"
          style="opacity: 1; fill: #51a2da; fill-opacity: 0.1"
          id="path2328"
        ></path>
      </g>
      <g id="strokes-00734247-430e-11ed-8d85-8fd7de2f268d" class="strokes">
        <g class="stroke-shape" id="g2333">
          <path
            rx="0"
            ry="0"
            d="m 961,1796.942 614.927,-49.283 v 101.23 z"
            style="opacity: 1; fill: none"
            id="path2331"
          ></path>
        </g>
      </g>
    </g>
  </svg>

  <!-- Benefits Section -->
  <section class="mt-3 pt-24 pb-12 dark:bg-neutral-900">
    <h2
      class="mb-12 bg-gradient-to-r from-fp-green to-fp-newblue-500 bg-clip-text text-center text-5xl font-bold text-transparent"
    >
      {{ $t(data.sections[1].sectionTitle) }}
    </h2>
    <FpBenefit
      v-for="item in data.sections[1].content"
      v-bind="item"
      columns="3"
    />
  </section>

  <!-- Features Section -->
  <section
    class="relative z-0 space-y-24 bg-gradient-to-b from-fp-newblue-100 to-fp-purple-100 pt-16 pb-32 dark:bg-neutral-800 dark:bg-none"
  >
    <div
      class="mx-auto max-w-7xl rounded-lg bg-white px-12 pt-6 pb-10 dark:bg-neutral-900"
      v-for="section in [data.sections[2]]"
    >
      <h2
        class="mb-8 text-center text-4xl font-semibold text-fp-blue-500 dark:text-gray-200"
      >
        {{ $t(section.sectionTitle) }}
      </h2>
      <div
        class="flex flex-wrap justify-between gap-4 text-center text-fp-darkblue-500 xl:gap-10"
      >
        <FpCard
          v-for="card in section.content"
          :title="card.title"
          :description="card.description"
          class="mx-auto grow basis-64"
        >
          <template #prepend>
            <FpLink :href="card.url">
              <FpCardImage slot="prepend" :src="card.image" class="max-h-16" />
            </FpLink>
          </template>
        </FpCard>
      </div>
    </div>
  </section>

  <!-- Call To Action -->
  <section class="relative z-0 dark:bg-black">
    <svg
      viewBox="185 3538 1202.8086 213"
      width="100%"
      height="100%"
      class="md:h-54 absolute -top-20 -z-10 h-36 fill-[url(#light)] dark:fill-black"
      preserveAspectRatio="none"
      xmlns="http://www.w3.org/2000/svg"
      xmlns:svg="http://www.w3.org/2000/svg"
    >
      <g transform="translate(-145.0957)">
        <defs>
          <linearGradient
            x1="185"
            y1="3495"
            x2="185"
            y2="3699"
            gradientUnits="userSpaceOnUse"
            id="light"
          >
            <stop style="stop-color: #e0f2ff; stop-opacity: 1" offset="0" />
            <stop style="stop-color: #ffffff; stop-opacity: 1" offset="1" />
          </linearGradient>
        </defs>
        <g class="fills">
          <path
            rx="0"
            ry="0"
            d="m 931.5,3538 c -246.60668,0 -465.44392,34.1944 -601.4043,86.8574 3e-4,75.3984 0,126.1426 0,126.1426 H 906.66992 931.5 956.33008 1532.9043 c 0,0 -3e-4,-50.7442 0,-126.1426 C 1396.9439,3572.1944 1178.1067,3538 931.5,3538 Z"
          />
        </g>
      </g>
    </svg>
    <FpCallToAction
      :cta="data.links"
      :image="{
        light: 'assets/images/fedora-kinoite-light.png',
        dark: 'assets/images/fedora-kinoite-dark.png',
      }"
    />
  </section>
</template>
