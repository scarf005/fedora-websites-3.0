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
    class="bg-gradient-to-tr from-fp-blue-light to-fp-blue dark:from-fp-blue dark:to-fp-blue-dark"
  >
    <!-- layout div-->
    <div class="flex items-center justify-between gap-4 px-6 py-2 lg:py-4">
      <!-- Logo -->
      <NuxtLink to="/" class="flex items-center gap-2 text-white">
        <Icon name="fa6-brands:fedora" size="48" />
        <!-- This needs to extract from the metadata-->
        <p class="text-2xl font-medium">Fedora</p>
      </NuxtLink>
      <!-- Navigation Links -->
      <!-- Hamburger Toggle-->
      <div class="justify-self-end text-white md:hidden">
        <button @click.prevent="">
          <Icon name="fa6-solid:bars" class="text-xl" size="32" />
        </button>
      </div>
      <!-- Category Menu -->
      <div class="hidden lg:block">
        <ul class="flex gap-3">
          <li
            v-for="category in categories"
            :key="category.id"
            class="text-lg font-medium text-white lg:text-xl xl:text-2xl"
          >
            <!--  -->
            <button class="">
              <span>{{ category.icon }}</span>
              <span>{{ category.label }}</span>
            </button>
          </li>
        </ul>
      </div>
      <!-- Language Selector -->
    </div>
  </nav>
</template>
