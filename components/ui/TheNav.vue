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
    <div class="mx-4 grid grid-cols-2">
      <div class="col-span-2 flex justify-between md:col-span-1">
        <TheNavLogo />
      </div>

      <FpNav
        class="col-span-2 flex gap-2 justify-self-end justify-self-center py-4 font-medium text-white md:col-span-1"
      >
        <button
          v-for="category in categories"
          :key="category.id"
          role="navigation"
          :class="`rounded-xl p-2 hover:bg-fp-blue-dark  ${
            categoryOpen === category && 'md:bg-fp-blue'
          }`"
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
          <div class="md:hidden">
            <Icon :name="category.icon" size="24" />
          </div>
          <p class="text-sm text-white">{{ category.label }}</p>
        </button>
        <div class="hidden items-center justify-end md:flex">
          <TheNavThemeSelector />
        </div>
      </FpNav>
    </div>

    <nav
      v-if="categoryOpen"
      class="left-0 right-0 mx-auto h-screen overflow-scroll bg-fp-blue px-8 md:overflow-hidden lg:absolute lg:h-[40rem] lg:w-11/12 lg:rounded-b-lg lg:shadow-md xl:h-[30rem]"
    >
      <div
        class="grid h-full gap-8 lg:grid-cols-[minmax(200px,300px)_1fr_180px] lg:grid-rows-[50px_1fr_60px]"
      >
        <header class="m-4 hidden w-fit lg:block">
          <h2 class="text-xl font-semibold uppercase text-white">
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
                :class="`mx-2 mt-4 flex cursor-pointer justify-between rounded-md py-4 px-2 text-white duration-150 ease-in-out hover:bg-fp-blue-dark lg:py-2 ${
                  sectionOpen === section && 'md:bg-fp-blue-dark'
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
          class="col-span-2 col-start-2 row-start-1 hidden text-white lg:block"
          v-if="sectionOpen"
        >
          <div>
            <header class="mb-6 mt-4">
              <h3 class="font-semibold text-white">
                {{ sectionOpen.label }}
              </h3>
              <p class="text-white">
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
                  <h4 class="mb-2 font-medium text-white">
                    {{ link.label }}
                  </h4>
                  <p class="text-white">
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
          <NavBarItem :title="$t('Languages')" :items="availableLocales" />
        </div>
      </div>
    </nav>
  </header>
</template>
