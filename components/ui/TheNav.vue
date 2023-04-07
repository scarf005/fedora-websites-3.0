<script setup>
import navigation from "../../config/navigation.json";

const switchLocalePath = useSwitchLocalePath();
const { locales } = useI18n();

let categories = {
  downloads: navigation.downloads,
  contributors: navigation.contributors,
  connections: navigation.connections,
  help: navigation.help,
  languages: navigation.languages,
};

locales.value.map((i) => {
  categories.languages.sections[0].links.push({
    label: i.name,
    path: switchLocalePath(i.code),
    i18n: true,
  });
});

// hack to duplicate the ask fedora section in the help menu
if (categories.help.sections[0].label != "Ask Fedora") {
  categories.help.sections = [
    navigation.connections.sections[1],
    ...navigation.help.sections,
  ];
}

const categoryOpen = useState("category", () => null);
const sectionOpen = useState("section", () => null);
let languageOpen = useState("languageOpen", () => null);
</script>

<template>
  <!-- BACKDROP, MAINLY TO CLOSE ON BLUR -->
  <div
    v-if="categoryOpen || languageOpen"
    class="fixed inset-0"
    @click="
      categoryOpen = null;
      languageOpen = null;
    "
  ></div>

  <div
    class="fixed z-50 w-full bg-gradient-to-r from-fp-newblue-500 to-fp-blue dark:from-fp-darkblue-500 dark:to-fp-blue"
  >
    <!-- NAVBAR  -->
    <div class="grid grid-cols-2">
      <a
        href="#main"
        class="sr-only !fixed top-0 !h-[54px] bg-fp-blue-700 !py-4 !px-6 text-sm text-white focus:not-sr-only"
        >Skip to content</a
      >
      <div
        class="col-span-2 my-1 flex items-center justify-between px-4 md:col-span-1 md:mt-0 md:justify-start"
      >
        <!-- LOGO -->
        <FpNavLogo />
        <!-- MOBILE EXPANDER -->
        <button
          @click="
            languageOpen = null;
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
        :class="`col-span-2 justify-center gap-2 py-4 text-white md:col-span-1 md:flex md:justify-end md:px-4 md:py-1 ${
          categoryOpen ? 'flex' : 'hidden'
        }`"
      >
        <button
          v-for="category in categories"
          :key="category.id"
          role="navigation"
          :class="`rounded-xl p-1 hover:bg-fp-darkblue-500 md:p-3 ${
            categoryOpen?.label === category.label && 'bg-fp-darkblue-500'
          }`"
          @click="
            languageOpen = null;
            if (categoryOpen && category.label === categoryOpen.label) {
              categoryOpen = null;
              sectionOpen = null;
            } else {
              categoryOpen = category;
              sectionOpen = category.sections[0];
            }
          "
        >
          <div
            :class="`${category.label == 'Languages' ? 'hidden' : 'md:hidden'}`"
          >
            <Icon :name="category.icon" size="24" />
          </div>
          <p
            :class="`text-sm text-white ${
              category.label == 'Languages'
                ? 'hidden md:inline-block'
                : 'inline-block'
            }`"
          >
            {{ $t(category.label) }}
          </p>
        </button>

        <!-- LANGUAGE & THEME SELECTOR (HIDDEN ON MOBILE) -->
        <div class="hidden items-center justify-end md:flex">
          <FpThemeSelector />
        </div>
      </FpNav>
    </div>

    <!-- MENU -->
    <nav
      v-if="categoryOpen"
      class="left-0 right-0 mx-auto h-screen shadow-xl md:absolute md:h-[43rem] md:bg-neutral-100 md:dark:bg-neutral-900"
    >
      <div class="grid md:grid-cols-12">
        <!-- LEFT COLUMN DESKTOP, HAS EXPANDERS ON MOBILE -->
        <section class="col-span-3 pl-2 pt-5 lg:col-start-2">
          <header class="hidden w-fit md:block">
            <h2
              class="px-2 text-base font-semibold uppercase text-white md:text-fp-blue"
            >
              {{ $t(categoryOpen.label) }}
            </h2>
          </header>
          <ul>
            <li
              v-for="section in categoryOpen.sections"
              :key="section.id"
              role="button"
            >
              <!-- CATEGORIES -->
              <div
                :class="`flex cursor-pointer justify-between px-2 py-2 text-white duration-150 ease-in-out hover:bg-gray-300 hover:dark:bg-gray-700 md:mt-4 md:py-4 md:py-2 md:text-gray-700 md:dark:text-gray-200 ${
                  sectionOpen === section &&
                  'bg-fp-darkblue-500 md:bg-gray-200 dark:md:bg-gray-800'
                } mr-2 rounded-xl`"
                role="button"
                @click="sectionOpen = section"
              >
                <h3 class="font-medium">
                  {{ $t(section.label) }}
                </h3>
                <div class="md:hidden">
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

              <!-- SECTIONS MOBILE (HIDDEN ON DESKTOP) -->
              <ul
                v-if="sectionOpen.label === section.label"
                class="block text-lg text-white ltr:ml-10 rtl:mr-10 md:hidden"
              >
                <li v-for="link in section.links" :key="link.id" class="py-1">
                  <FpLink :href="link.path" v-if="!link.i18n">
                    <Icon
                      :name="link.icon"
                      size="24"
                      class="ltr:mr-2 rtl:ml-2"
                    />
                    {{ $t(link.label) }}
                  </FpLink>

                  <a
                    v-if="link.i18n"
                    :href="`${
                      $config.app.baseURL.replace(new RegExp('/$'), '') +
                      link.path
                    }`"
                  >
                    {{ $t(link.label) }}
                  </a>
                </li>
              </ul>
            </li>
          </ul>
        </section>

        <!-- SECTIONS DESKTOP (RIGHT COLUMN, HIDDEN ON MOBILE) -->
        <section
          class="col-span-9 mt-2 hidden h-[42rem] overflow-hidden overflow-scroll border-neutral-400 p-5 text-white ltr:border-l rtl:border-r dark:border-neutral-600 md:block lg:col-span-7"
          v-if="sectionOpen"
        >
          <div>
            <header class="mb-6">
              <h3 class="font-semibold text-gray-700 dark:text-gray-200">
                {{ $t(sectionOpen.label) }}
              </h3>
              <p class="text-gray-500 dark:text-gray-500">
                {{ $t(sectionOpen.description) }}
              </p>
            </header>
            <ul class="grid grid-cols-3 gap-2">
              <li
                v-for="link in sectionOpen.links"
                :key="link.id"
                class="rounded-xl p-4 hover:bg-gray-200 dark:hover:bg-gray-800"
              >
                <FpLink :href="link.path" v-if="!link.i18n" :rel="link.rel">
                  <h4 class="mb-2 font-medium text-fp-blue">
                    <Icon :name="link.icon" size="32" class="text-fp-blue" />
                    {{ $t(link.label) }}
                  </h4>
                  <p class="text-base text-gray-700 dark:text-gray-500">
                    {{ $t(link.description) }}
                  </p>
                </FpLink>

                <a
                  v-if="link.i18n"
                  class="mb-2 font-medium text-fp-blue"
                  :href="`${
                    $config.app.baseURL.replace(new RegExp('/$'), '') +
                    link.path
                  }`"
                >
                  {{ $t(link.label) }}
                </a>
              </li>
            </ul>
          </div>
        </section>
      </div>
    </nav>
  </div>
</template>
