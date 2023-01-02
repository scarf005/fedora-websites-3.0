<script setup>
const { data } = await useAsyncData("navigation", () =>
  queryContent("/_navigation").findOne()
);
const categories = {
  downloads: data._value.downloads,
  community: data._value.community,
  contributors: data._value.contributors,
  support: data._value.support,
};

const switchLocalePath = useSwitchLocalePath();
const { locales } = useI18n();
const availableLocales = computed(() => {
  return locales.value.map((i) => ({
    name: i.name,
    href: switchLocalePath(i.code),
  }));
});

// Menu Toggles
const categoryOpen = useState("category", () => null);
const sectionOpen = useState("section", () => null);
</script>

<template>
  <header
    class="fixed z-50 w-full bg-gradient-to-tr from-fp-blue-light to-fp-blue dark:from-fp-blue dark:to-fp-blue-dark"
  >
    <div class="mx-4 flex justify-between py-2 lg:py-1">
      <TheNavLogo />
      <FpNav
        class="flex gap-4 justify-self-end justify-self-center py-4 font-medium text-white"
      >
        <button
          v-for="category in categories"
          :key="category.id"
          role="navigation"
          class="hidden lg:block"
          @click="
            if (categoryOpen && category.label === categoryOpen.label) {
              categoryOpen = null;
              sectionOpen = null;
            } else {
              categoryOpen = category;
              sectionOpen = category.sections[0];
            }
          "
        >
          <div class="lg:hidden">
            <Icon :name="category.icon" size="32" />
          </div>
          <p>{{ category.label }}</p>
        </button>

        <button
          @click="
            if (categoryOpen) {
              categoryOpen = null;
              sectionOpen = null;
            } else {
              categoryOpen = categories.downloads;
              sectionOpen = categories.downloads;
            }
          "
          type="button"
          class="col-start-2 row-start-1 justify-self-end lg:hidden"
        >
          <Icon name="fa6-solid:bars" />
        </button>

        <TheNavThemeSelector />
        <NavBarItem :title="$t('Languages')" :items="availableLocales" />
      </FpNav>
    </div>

    <nav
      v-if="categoryOpen"
      class="left-0 right-0 mx-auto h-screen px-8 lg:absolute lg:h-[40rem] lg:w-11/12 lg:rounded-b-lg lg:bg-white lg:shadow-md dark:lg:bg-fp-blue xl:h-[30rem]"
    >
      <div
        class="grid h-full gap-8 lg:grid-cols-[minmax(200px,300px)_1fr_180px] lg:grid-rows-[50px_1fr_60px]"
      >
        <header class="m-4 hidden w-fit lg:block">
          <h2
            class="text-xl font-semibold uppercase text-fp-blue-dark dark:text-white"
          >
            Fedora {{ categoryOpen.label }}
          </h2>
        </header>

        <!-- Categories and mobile drop downs -->
        <section class="col-start-1 w-full">
          <ul>
            <li
              v-for="section in categoryOpen.sections"
              :key="section.id"
              role="button"
            >
              <!-- category for both desktop & mobile -->
              <div
                :class="`mx-2 mt-4 flex cursor-pointer justify-between rounded-md py-4 px-2 text-fp-blue duration-150 ease-in-out hover:bg-fp-blue-dark dark:text-white lg:py-2 ${
                  sectionOpen === section && 'bg-blue-300'
                }`"
                role="button"
                @click="sectionOpen = section"
              >
                <h3 class="font-medium">
                  {{ section.label }}
                </h3>
                <div class="lg:hidden">
                  <Icon name="fa6-solid:chevron-right" size="32" />
                </div>
              </div>

              <!-- Sections List Mobile -->
              <ul class="ml-10 block text-lg text-white sm:hidden">
                <li v-for="link in section.links" :key="link.id" class="py-1">
                  <FpLink
                    :href="link.path"
                    class="underline-offset-4 hover:underline"
                    >{{ link.label }}</FpLink
                  >
                </li>
              </ul>
            </li>
          </ul>
        </section>

        <!-- Section List Desktop -->
        <section
          class="col-span-2 col-start-2 row-start-1 hidden dark:text-white lg:block"
          v-if="sectionOpen"
        >
          <div>
            <header class="mb-6 mt-4">
              <h3 class="font-semibold text-fp-blue dark:text-white">
                {{ sectionOpen.label }}
              </h3>
              <p class="text-fp-blue dark:text-white">
                {{ sectionOpen.description }}
              </p>
            </header>
            <ul class="grid grid-cols-3 gap-4">
              <li
                v-for="link in sectionOpen.links"
                :key="link.id"
                class="max-w-xs rounded-lg p-2 hover:bg-fp-blue-dark"
              >
                <FpLink :href="link.path">
                  <h4 class="mb-2 font-medium text-fp-blue dark:text-white">
                    {{ link.label }}
                  </h4>
                  <p class="text-fp-blue dark:text-white">
                    {{ link.description }}
                  </p>
                </FpLink>
              </li>
            </ul>
          </div>
        </section>

        <!-- close button -->
        <div
          class="col-start-3 row-start-1 mr-8 hidden items-center justify-end text-white lg:flex"
        >
          <button @click="categoryOpen = null" class="hover:opacity-75">
            <Icon name="fa6-solid:x" size="24" />
          </button>
        </div>
      </div>
    </nav>
  </header>
</template>
