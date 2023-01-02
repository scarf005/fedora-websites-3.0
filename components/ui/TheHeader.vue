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

// Menu Toggles
const showMobileMenu = useState("mobileMenu", () => false);
const showNavMenu = useState("navMenu", () => false);

const toggleMobileMenu = () => {
  showMobileMenu.value = !showMobileMenu.value;
  showNavMenu.value = !showNavMenu.value;
};
const toggleNavMenu = () => {
  return (showNavMenu.value = !showNavMenu.value);
};

// Data to pass to right side of the menu
const menuContent = useState(() => categories.downloads);
function updateMenuContent(category) {
  menuContent.value = category;
  toggleNavMenu();
}
</script>

<template>
  <header
    class="bg-gradient-to-tr from-fp-blue-light to-fp-blue dark:from-fp-blue dark:to-fp-blue-dark"
  >
    <div class="mx-4 grid grid-cols-2 items-center py-2 lg:pt-4 lg:pb-2">
      <TheHeaderLogo />
      <!-- Switch back to showMobile -->
      <FpNav
        class="col-span-full hidden gap-4 justify-self-center py-4 font-medium text-white lg:col-span-1 lg:flex lg:justify-self-end"
      >
        <button
          v-for="category in categories"
          :key="category.id"
          @click.prevent="updateMenuContent(category)"
          role="navigation"
        >
          <div class="lg:hidden">
            <Icon :name="category.icon" size="32" />
          </div>
          <p>{{ category.label }}</p>
        </button>
      </FpNav>

      <LazyFpToggle
        :iconToggle="showMobileMenu"
        @emitToggle="toggleMobileMenu"
        class="col-start-2 row-start-1 justify-self-end lg:hidden"
      />
    </div>
    <TheNav
      :menuContent="menuContent"
      :class="showNavMenu ? 'block' : 'hidden'"
      @emitClose="toggleNavMenu"
    />
  </header>
</template>
