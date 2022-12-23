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

let showMobile = useState("mobileToggle", () => false);

// TODO: Fix switch while active and crossing threshold
function onResize() {
  showMobile.value = window.innerWidth > 1024;
}
onMounted(() => {
  onResize();
  window.addEventListener("resize", onResize, { passive: true });
});

function menuToggle() {
  showMobile.value = !showMobile.value;
}
</script>
<template>
  <header
    class="bg-gradient-to-tr from-fp-blue-light to-fp-blue dark:from-fp-blue dark:to-fp-blue-dark"
  >
    <!-- TODO Fix up Padding and Alignment -->
    <div class="mx-4 grid grid-cols-2 items-center py-2 lg:pt-4 lg:pb-2">
      <TheHeaderLogo />
      <!-- TODO: Make each category click emit an event to open each drop down -->
      <LazyFpNav
        :navLinks="categories"
        class="col-span-full justify-self-center py-4 lg:col-span-1 lg:justify-self-end"
        :global="true"
        :class="showMobile ? 'block' : 'hidden'"
      />
      <LazyFpToggle
        :iconToggle="showMobile"
        @emitToggle="menuToggle"
        class="col-start-2 row-start-1 justify-self-end lg:hidden"
      />
    </div>
    <!-- Dropdown Nav Menu -->
    <LazyTheNav :class="showMobile ? 'block' : 'hidden'" />
  </header>
</template>
