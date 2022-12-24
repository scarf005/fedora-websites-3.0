<script setup>
const props = defineProps({
  menuContent: {
    type: Object || Array,
  },
});

const emit = defineEmits(["emitClose"]);

function useToggle() {
  emit("emitClose");
}
function toggleCategories() {}
</script>
<template>
  <nav
    class="left-0 right-0 mx-auto h-screen px-8 lg:absolute lg:h-[40rem] lg:w-11/12 lg:rounded-b-lg lg:bg-white lg:shadow-md dark:lg:bg-fp-blue xl:h-[30rem]"
  >
    <div
      class="grid h-full gap-8 lg:grid-cols-[minmax(200px,300px)_1fr_180px] lg:grid-rows-[50px_1fr_60px]"
    >
      <header class="m-4 hidden w-fit lg:block">
        <h2
          class="text-xl font-semibold uppercase text-fp-blue-dark dark:text-white"
        >
          Fedora {{ menuContent.label }}
        </h2>
      </header>
      <!-- Categories and mobile drop downs -->
      <section class="col-start-1 w-full">
        <ul>
          <li v-for="group in menuContent.categories" :key="group.id">
            <TheNavItem :itemData="group" />
          </li>
        </ul>
      </section>
      <!-- Right Column List Items only show on desktop -->
      <section
        class="col-span-2 col-start-2 row-start-1 hidden dark:text-white lg:block"
      >
        <ul>
          <li>
            <header class="mb-6 mt-4">
              <h3 class="font-semibold">
                {{ menuContent.categories[0].label }}
              </h3>
              <p>{{ menuContent.categories[0].description }}</p>
            </header>
            <ul class="grid grid-cols-3 gap-4">
              <li
                v-for="link in menuContent.categories[0].links"
                :key="link.id"
                class="max-w-xs rounded-lg hover:bg-fp-blue-dark"
              >
                <NuxtLink :to="link.url">
                  <h4 class="mb-2 font-medium">{{ link.label }}</h4>
                  <!-- TOOD: evaluate str length with useWords and return ellipsed reduced list on lg screen size -->
                  <p>{{ link.description }}</p>
                </NuxtLink>
              </li>
            </ul>
          </li>
        </ul>
      </section>

      <div
        class="col-start-3 row-start-1 mr-8 hidden items-center justify-end text-white lg:flex"
      >
        <button @click="useToggle" class="hover:opacity-75">
          <Icon name="fa6-solid:x" size="24" />
        </button>
      </div>
      <div
        class="mr-8 mb-12 self-center justify-self-end lg:col-span-2 lg:col-start-2 lg:row-start-4 lg:mb-0 xl:row-start-3"
      >
        <FpImage src="assets/images/fedora_white.png" class="w-36" />
      </div>
    </div>
  </nav>
</template>
