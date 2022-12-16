<script setup>
// Temporarily use this to build out the nav menu content on click
defineProps({
  navItems: {
    type: Object,
  },
});
let isOpen = ref(false);
</script>
<template>
  <!-- Mobile Open List Below Title-->
  <!-- Desktop Open List Beside Title-->
  <section
    class="mx-auto h-screen rounded-b-lg bg-gradient-to-br from-fp-blue-light to-fp-blue dark:from-fp-blue dark:to-fp-blue-dark lg:h-2/3 lg:w-5/6"
  >
    <div class="grid">
      <!-- Active Category Title -->
      <div class="m-4 hidden lg:block">
        <h3 class="font-semibold uppercase text-fp-blue-dark dark:text-white">
          {{ navItems.label }}
        </h3>
      </div>
      <!-- Sub Categories-->
      <div class="mx-4">
        <ul class="w-full list-none">
          <li
            v-for="category in navItems.categories"
            class="my-4 text-2xl text-white"
          >
            <button
              @click.prevent="isOpen = !isOpen"
              class="flex w-full justify-between"
            >
              <span>{{ category.label }} </span>
              <Icon
                name="fa6-solid:angle-right"
                size="32"
                :class="isOpen ? 'rotate-90' : 'rotate-0'"
              />
            </button>
            <!-- Active Category Group Mobile -->
            <ul class="my-4 list-none" :class="isOpen ? 'block' : 'hidden'">
              <li v-for="link in category.links" :key="link.id">
                <NuxtLink
                  :to="link.path || link.href"
                  class="block py-2 pl-8 font-display text-2xl hover:bg-fp-blue"
                  >{{ link.label }}</NuxtLink
                >
              </li>
            </ul>
          </li>
        </ul>
      </div>
      <!-- Active Category Group -->
      <div></div>
    </div>
  </section>
</template>
