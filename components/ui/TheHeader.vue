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

function onResize() {
  showMobile.value = window.innerWidth > 1024;
  if (window.innerWidth > 1024) {
    showMenu.value = false;
  }
}

onMounted(() => {
  onResize();
  window.addEventListener("resize", onResize, { passive: true });
});

function mobileToggle() {
  showMobile.value = !showMobile.value;
  showMenu.value = !showMenu.value;
}

function menuToggle(mobile = false) {
  if (mobile == true) {
    showMobile.value = !showmobile.value;
  }
  showMenu.value = !showMenu.value;
}

let showMobile = useState("mobileToggle", () => false);

let showMenu = useState("menuToggle", () => false);

let menuContent = ref({});

function updateMenuContent(obj) {
  menuContent.value = obj;
  if (showMenu.value == false) {
    showMenu.value = true;
  }
}
</script>

<template>
  <header
    class="bg-gradient-to-tr from-fp-blue-light to-fp-blue dark:from-fp-blue dark:to-fp-blue-dark"
  >
    <div class="mx-4 grid grid-cols-2 items-center py-2 lg:pt-4 lg:pb-2">
      <TheHeaderLogo />

      <FpNav
        class="col-span-full flex gap-4 justify-self-center py-4 font-medium text-white lg:col-span-1 lg:justify-self-end"
        :class="showMobile ? 'block' : 'hidden'"
      >
        <button
          v-for="category in categories"
          :key="category.id"
          @click.prevent="updateMenuContent(category)"
        >
          <div class="lg:hidden">
            <Icon :name="category.icon" size="32" />
          </div>
          <p>{{ category.label }}</p>
        </button>
      </FpNav>
      <LazyFpToggle
        :iconToggle="showMobile"
        @emitToggle="mobileToggle"
        class="col-start-2 row-start-1 justify-self-end lg:hidden"
      />
    </div>
    <TheNav
      :menuContent="menuContent"
      :class="showMenu ? 'block' : 'hidden'"
      @emitClose="menuToggle"
    />
  </header>
</template>
