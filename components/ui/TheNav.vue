<script setup>
const { data } = await useAsyncData("navigation", () =>
  queryContent("_navigation").findOne()
);
const categories = {
  downloads: data._value.downloads,
  community: data._value.community,
  contributors: data._value.contributors,
  support: data._value.support,
};
</script>
<template>
  <nav
    class="left-0 right-0 mx-auto h-screen lg:absolute lg:h-[30rem] lg:w-[64rem] lg:rounded-b-lg lg:bg-white lg:shadow-md dark:lg:bg-fp-blue xl:w-[100rem]"
  >
    <div
      class="grid gap-8 lg:grid-cols-[minmax(200px,300px)_1fr] lg:grid-rows-[20px_1fr]"
    >
      <header class="m-4 hidden w-fit lg:block">
        <h2
          class="text-xl font-semibold uppercase text-fp-blue-dark dark:text-white"
        >
          Fedora {{ categories.downloads.label }}
        </h2>
      </header>
      <!-- Categories and mobile drop downs -->
      <section class="w-full">
        <ul>
          <li v-for="group in categories.downloads.categories" :key="group.id">
            <TheNavItem :itemData="group" />
          </li>
        </ul>
      </section>
      <!-- Right Column List Items only show on desktop -->
      <section class="col-start-2 row-start-1 hidden dark:text-white lg:block">
        <ul>
          <li
            v-for="group in categories.downloads.categories"
            :key="group.id"
            class=""
          >
            <header class="mb-6 mt-4">
              <h3 class="font-semibold">{{ group.label }}</h3>
              <p>{{ group.description }}</p>
            </header>
            <ul class="grid grid-cols-3 gap-4">
              <li
                v-for="link in group.links"
                class="max-w-xs rounded-lg hover:bg-fp-blue-dark"
              >
                <NuxtLink :to="link.url">
                  <h4 class="mb-2 font-medium">{{ link.label }}</h4>
                  <p>{{ link.description }}</p>
                </NuxtLink>
              </li>
            </ul>
          </li>
        </ul>
      </section>
    </div>
  </nav>
</template>
