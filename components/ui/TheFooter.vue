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

// TODO: recursive helper function to find all required list items-center

// TODO: function for populating list entries

// TODO: computed properties for each list category
const desktops = computed(() => {
  const labels = ["workstation", "silverblue", "kde", "kinoite"];
  return;
});
const cloud = computed(() => {
  const labels = ["server", "coreos", "cloud", "container"];
  return;
});
const edge = computed(() => {
  const labels = ["iot", "arm"];
  return;
});
const support = computed(() => {
  const labels = ["ask", "bugs", "magazine", "developer"];
  return;
});
const community = computed(() => {
  const labels = ["join", "blog", "matrix", "discussion", "fas"];
  return;
});
</script>

<template>
  <footer class="flex flex-col bg-gray-200 dark:bg-neutral-900">
    <nav class="container mx-auto py-10">
      <div class="container grid grid-cols-5">
        <!-- TODO: make each category stand alone using -->
        <div
          v-for="category in categories"
          class="col-span-4 px-3 md:col-span-1"
        >
          <div v-for="section in category.sections">
            <p class="mt-5 text-lg font-bold text-gray-500 dark:text-gray-300">
              {{ $t(section.label) }}
            </p>
            <p
              class="text-gray-800 dark:text-gray-500"
              v-for="item in section.links"
            >
              <FpLink :href="item.path" class="w-100">{{ item.label }}</FpLink>
            </p>
          </div>
        </div>
        <div class="col-span-5 px-3 md:col-span-1">
          <p class="mt-5 text-lg font-bold text-gray-500 dark:text-gray-300">
            {{ $t("Languages") }}
          </p>
          <p
            class="text-gray-800 dark:text-gray-500"
            v-for="item in availableLocales"
          >
            <FpLink :href="item.href" class="w-100">{{ item.name }}</FpLink>
          </p>
        </div>
      </div>
    </nav>
    <!-- Privacy Links -->
    <section class="container mx-auto py-10">
      <div class="flex flex-wrap items-center gap-4">
        <div class="">
          <FpImage
            src="assets/images/logos/fedora-blue.png"
            :alt="$t('Fedora Logo')"
            class="ml-6 w-1/3 xl:ml-0"
          />
        </div>
        <ul
          class="mx-4 flex grow justify-center gap-4 lg:mx-0 lg:gap-8 xl:justify-start"
        >
          <li class="list-none underline underline-offset-1">
            <NuxtLink
              to="#"
              class="text-fp-gray-darkest transition duration-300 ease-in-out hover:text-fp-gray"
              >{{ $t("Privacy Statement") }}</NuxtLink
            >
          </li>
          <li class="list-none underline underline-offset-1">
            <NuxtLink
              to="#"
              class="text-fp-gray-darkest transition duration-300 ease-in-out hover:text-fp-gray"
              >{{ $t("Legal") }}</NuxtLink
            >
          </li>
          <li class="list-none underline underline-offset-1">
            <NuxtLink
              to="#"
              class="text-fp-gray-darkest transition duration-300 ease-in-out hover:text-fp-gray"
              >{{ $t("Code of Conduct") }}</NuxtLink
            >
          </li>
          <li class="list-none underline underline-offset-1">
            <NuxtLink
              to="#"
              class="text-fp-gray-darkest transition duration-300 ease-in-out hover:text-fp-gray"
              >{{ $t("Sponsors") }}</NuxtLink
            >
          </li>
        </ul>
      </div>
    </section>

    <!-- Red Hat Sponsorship Section -->
    <section class="bg-black py-10 text-center md:text-left">
      <div class="container mx-auto flex flex-col lg:flex-row">
        <div class="mx-auto lg:mx-0 lg:basis-3/12">
          <FpImage
            src="assets/images/logo-sponsored-by-red-hat.png"
            :alt="$t('Sponsored by Red Hat Logo')"
            class="mb-4 xl:mb-0"
          />
        </div>

        <div class="container text-center lg:text-left">
          <p class="text-white">
            {{ $t("Fedora is sponsored by Red Hat.") }}
            <span class="block text-fp-gray xl:ml-2 xl:inline">
              {{
                $t(
                  "Learn more about the relationship between Red Hat and Fedora."
                )
              }}
            </span>
          </p>
        </div>
      </div>
    </section>
  </footer>
</template>
