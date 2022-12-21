<script setup>
const { data } = await useAsyncData("navigation", () =>
  queryContent("_navigation").findOne()
);
// bundle into emit more effectively to reduce code duplication
// or create a useToggle composable to reduce duplication
let showMobile = ref(false);

const menuToggle = () => {
  showMobile.value = !showMobile.value;
};

const categories = {
  downloads: data._value.downloads,
  community: data._value.community,
  contributors: data._value.contributors,
  support: data._value.support,
};
</script>
<template>
  <header
    class="bg-gradient-to-tr from-fp-blue-light to-fp-blue dark:from-fp-blue dark:to-fp-blue-dark"
  >
    <!-- TODO Fix up Padding and Alignment -->
    <div class="mx-4 grid grid-cols-2 items-center pt-2 pb-1 lg:pt-4 lg:pb-2">
      <TheHeaderLogo />
      <!-- Category Menu -->
      <!-- <AppNav
        hidden
        lg:block
      /> -->
      <!-- Mobile Button -->
      <FpToggle @emitToggle="menuToggle" />
    </div>
  </header>
  <!-- Dropdown Nav Menu -->
  <LazyTheNav v-show="showMobile" />
</template>
