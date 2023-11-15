<script setup>
defineProps({
  background: String,
});
</script>

<template>
  <section class="group relative z-0 overflow-hidden dark:bg-neutral-900">
    <svg
      viewBox="0 0 209.9868 38.261421"
      width="100%"
      height="100%"
      preserveAspectRatio="none"
      version="1.1"
      id="svg4475"
      class="absolute top-0 z-10 h-20 transition delay-200 duration-700 ease-out group-hover:-translate-y-24 group-hover:opacity-75 md:h-40"
      xmlns="http://www.w3.org/2000/svg"
      xmlns:svg="http://www.w3.org/2000/svg"
    >
      <defs id="defs4472" />
      <g id="layer1" transform="translate(0.04450727,-135.47272)">
        <path
          class="fill-fp-newblue-100 dark:fill-neutral-800"
          d="M 209.94229,136.77754 -0.04450727,157.96768 V 135.47272 H 209.94229 Z"
          id="path6102"
        />
      </g>
    </svg>
    <img
      :src="`${
        $config.app.baseURL.replace(new RegExp('/$'), '') +
        '/' +
        background.replace('public/', '')
      }`"
      class="z-0 w-full scale-110 transition duration-1000 ease-in-out hover:scale-90"
    />
    <svg
      viewBox="0 0 209.98682 22.494961"
      width="100%"
      height="100%"
      preserveAspectRatio="none"
      version="1.1"
      id="svg4475"
      class="absolute bottom-0 z-10 h-10 transition delay-200 duration-700 ease-out group-hover:translate-y-20 group-hover:opacity-75 sm:h-20"
      xmlns="http://www.w3.org/2000/svg"
      xmlns:svg="http://www.w3.org/2000/svg"
    >
      <defs id="defs4472" />
      <g id="layer1" transform="matrix(1,0,0,-1,0.04450727,157.96768)">
        <path
          class="fill-fp-newblue-100 dark:fill-neutral-800"
          d="M 209.94229,136.77754 -0.04450727,157.96768 V 135.47272 H 209.94229 Z"
          id="path6102"
        />
      </g>
    </svg>
  </section>
</template>
