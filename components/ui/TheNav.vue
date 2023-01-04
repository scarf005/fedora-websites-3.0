<script setup>
import navigation from "../../config/navigation.json";
const categories = {
  downloads: navigation.downloads,
  community: navigation.community,
  contributors: navigation.contributors,
  support: navigation.support,
};

const switchLocalePath = useSwitchLocalePath();
const { locales } = useI18n();
const availableLocales = computed(() => {
  return locales.value.map((i) => ({
    name: i.name,
    href: switchLocalePath(i.code),
  }));
});

const categoryOpen = useState("category", () => null);
const sectionOpen = useState("section", () => null);
</script>

<template>
  <header
    class="fixed z-50 w-full bg-gradient-to-tr from-fp-blue-light to-fp-blue dark:from-fp-blue dark:to-fp-blue-dark"
  >
    <!-- NAVBAR  -->
    <div class="grid grid-cols-2">
      <div
        class="col-span-2 my-1 flex items-center justify-between px-4 md:col-span-1 md:mt-0 md:justify-start"
      >
        <!-- LOGO -->
        <FpNavLogo />
        <!-- MOBILE EXPANDER -->
        <button
          @click="
            if (
              categoryOpen &&
              categories.downloads.label === categoryOpen.label
            ) {
              categoryOpen = null;
              sectionOpen = null;
            } else {
              categoryOpen = categories.downloads;
              sectionOpen = categories.downloads.sections[0];
            }
          "
          type="button"
          class="rounded-md p-2 text-white md:hidden"
        >
          <Icon v-if="categoryOpen == null" name="fa6-solid:bars" />
          <Icon v-else name="fa6-solid:x" />
        </button>
      </div>

      <!-- CATEGORY BUTTONS IN NAVBAR -->
      <FpNav
        :class="`col-span-2 justify-center gap-4 py-4 px-4 text-white md:col-span-1 md:flex md:justify-end xl:gap-2 ${
          categoryOpen ? 'flex' : 'hidden'
        }`"
      >
        <button
          v-for="category in categories"
          :key="category.id"
          role="navigation"
          :class="`rounded-xl p-1 hover:bg-fp-blue-dark md:p-3 ${
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
          <FpThemeSelector />
        </div>
      </FpNav>
    </div>

    <!-- MENU -->
    <nav
      v-if="categoryOpen"
      class="left-0 right-0 mx-auto h-screen bg-fp-blue px-8 md:absolute md:h-[40rem] md:w-11/12 md:rounded-b-lg md:shadow-md xl:w-10/12"
    >
      <!-- close button -->
      <div class="mt-3 mr-8 hidden items-center justify-end text-white md:flex">
        <FpLanguageSelector
          :title="$t('Languages')"
          :items="availableLocales"
        />
        <button @click="categoryOpen = null" class="hover:opacity-75">
          <Icon name="fa6-solid:x" size="24" />
        </button>
      </div>

      <div class="grid h-full gap-8 lg:grid-cols-12">
        <section class="col-span-3 w-full">
          <header class="m-4 hidden w-fit lg:block">
            <h2 class="text-xl font-semibold uppercase text-white">
              Fedora {{ categoryOpen.label }}
            </h2>
          </header>
          <ul>
            <li
              v-for="section in categoryOpen.sections"
              :key="section.id"
              role="button"
            >
              <!-- Category List -->
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
                  <Icon
                    name="fa6-solid:chevron-right"
                    :class="`${
                      sectionOpen.label === section.label &&
                      'rotate-90 duration-150 ease-in-out'
                    }`"
                    size="32"
                  />
                </div>
              </div>

              <!-- Sections List Mobile -->
              <ul
                v-if="sectionOpen.label === section.label"
                class="ml-10 block text-lg text-white lg:hidden"
              >
                <li v-for="link in section.links" :key="link.id" class="py-1">
                  <FpLink :href="link.path">
                    <Icon :name="link.icon" size="24" class="mr-2" />
                    {{ link.label }}
                  </FpLink>
                </li>
              </ul>
            </li>
          </ul>
        </section>

        <!-- Section List Desktop -->
        <section
          class="col-span-9 hidden text-white lg:block"
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
                    <Icon :name="link.icon" size="32" />
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
      </div>
    </nav>
  </header>
</template>
