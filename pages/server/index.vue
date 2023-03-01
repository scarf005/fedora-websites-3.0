<script setup>
const data = await getCMS("editions/server/home");
useContentHead(data);
</script>
<template>
  <FpHero
    :background="data.header_images[1].image"
    alignment="bg-bottom"
    class="relative z-0"
  >
    <TheLocalBar
      image="assets/images/fedora-server-logo.png"
      home="/server"
      :items="[
        { name: 'Download', link: '/server/download' },
        { name: 'Community', link: '/server/community' },
      ]"
    />
    <FpBanner
      :title="data.title"
      :subtitle="data.description"
      color="text-fp-blue"
      border="border border-fp-blue"
      background="text-white bg-fp-blue"
      :ctas="data.links"
    >
      <FpImage :src="data.header_images[0].image" />
    </FpBanner>
    <svg
      viewBox="0 0 236 36"
      version="1.1"
      xmlns="http://www.w3.org/2000/svg"
      xmlns:svg="http://www.w3.org/2000/svg"
      class="absolute -bottom-5 -z-10"
    >
      <g>
        <path
          class="fill-white dark:fill-neutral-800"
          d="M 0 0 L 62 26 L 236 0 L 236 36 L 0 36 L 0 10"
        />
      </g>
    </svg>
  </FpHero>

  <!-- Benefits Section -->
  <section class="pt-32 dark:bg-neutral-900">
    <h2
      class="mb-12 bg-gradient-to-r from-fp-green to-fp-orange bg-clip-text text-center text-5xl font-bold text-transparent"
    >
      {{ $t(data.sections[0].sectionTitle) }}
    </h2>
    <FpBenefit
      v-for="item in data.sections[0].content"
      v-bind="item"
      columns="2"
    />
  </section>

  <!-- Community Section -->
  <section class="relative z-0 dark:bg-neutral-800">
    <svg
      viewBox="0 0 209.9868 38.261421"
      width="100%"
      height="100%"
      preserveAspectRatio="none"
      version="1.1"
      id="svg4475"
      class="absolute top-0 z-10 h-40"
      xmlns="http://www.w3.org/2000/svg"
      xmlns:svg="http://www.w3.org/2000/svg"
    >
      <defs id="defs4472" />
      <g id="layer1" transform="translate(0.04450727,-135.47272)">
        <path
          class="fill-white dark:fill-neutral-900"
          d="M 209.94229,136.77754 -0.04450727,157.96768 V 135.47272 H 209.94229 Z"
          id="path6102"
        />
      </g>
    </svg>

    <FpCommunity :data="data.sections[1]" class="server-accent dark:!bg-none" />
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
      image="assets/images/fedora-server-full-logo.png"
    />
  </section>
</template>

<style>
ul.server-accent,
.server-accent ul {
  @apply marker:text-fp-orange-500 dark:marker:text-fp-orange-700;
}
</style>
