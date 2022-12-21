<script setup>
import { onMounted } from "vue";

const { data } = await useAsyncData("navigation", () =>
  queryContent("_navigation").findOne()
);
const categories = {
  downloads: data._value.downloads,
  community: data._value.community,
  contributors: data._value.contributors,
  support: data._value.support,
};

let showMobile = ref(false);

function onResize() {
  showMobile.value = window.innerWidth > 1024;
}
onMounted(() => {
  onResize();
  window.addEventListener("resize", onResize, { passive: true });
});

// bundle into emit more effectively to reduce code duplication
// or create a useToggle composable to reduce duplication
const menuToggle = () => {
  showMobile.value = !showMobile.value;
};
</script>
<template>
  <header
    class="bg-gradient-to-tr from-fp-blue-light to-fp-blue dark:from-fp-blue dark:to-fp-blue-dark"
  >
    <!-- TODO Fix up Padding and Alignment -->
    <div class="mx-4 grid grid-cols-2 items-center pt-2 pb-1 lg:pt-4 lg:pb-2">
      <TheHeaderLogo />

      <LazyAppNav
        :navLinks="categories"
        class="col-span-full justify-self-center py-4 lg:col-span-1 lg:justify-self-end"
        :global="true"
        :class="showMobile ? 'block' : 'hidden'"
      />
      <LazyFpToggle
        @emitToggle="menuToggle"
        class="col-start-2 justify-self-end lg:hidden"
      />
    </div>
  </header>
</template>
