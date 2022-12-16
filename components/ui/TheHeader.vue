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
// open menu function
const showMobileMenu = ref(false);
// close menu function
</script>
<template>
  <header
    class="bg-gradient-to-tr from-fp-blue-light to-fp-blue dark:from-fp-blue dark:to-fp-blue-dark"
  >
    <!-- TODO Fix up Padding and Alignment -->
    <div class="mx-4 grid grid-cols-2 items-center pt-2 pb-1 lg:pt-4 lg:pb-2">
      <TheHeaderLogo class="" />

      <TheNav
        :categories="categories"
        class="hidden justify-self-end lg:block"
      />
      <!-- <TheMenuButton class="md:hidden" /> -->
      <div class="justify-self-end lg:hidden">
        <button
          @click.prevent="showMobileMenu = !showMobileMenu"
          class="text-white duration-300 ease-in-out hover:opacity-50"
        >
          <Icon v-if="showMobileMenu" name="line-md:close" size="32" />
          <Icon v-else name="fa6-solid:bars" size="32" />
        </button>
      </div>
      <!-- Wrap Transition around this Nav -->
      <TheNav
        :categories="categories"
        v-show="showMobileMenu"
        class="col-span-2 self-center lg:col-span-1 lg:hidden"
      />
    </div>
    <!-- Determine Best way to integrate this with the nav on mobile and desktop -->
  </header>

  <TheNavMenu :navItems="categories.downloads" />
</template>
