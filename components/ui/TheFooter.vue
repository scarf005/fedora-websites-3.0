<script setup>
import navigation from "../../config/navigation.json";

const path = {
  community: navigation.community.sections,
  contributors: navigation.contributors.sections,
  support: navigation.support.sections,
};

const support = computed(() => {
  return {
    ask: path.support[0].links[0],
    bugs: path.support[2].links[1],
    magazine: path.community[1].links[0],
    developer: path.support[3].links[1],
  };
});
const community = computed(() => {
  return {
    join: path.contributors[3].links[0],
    blog: path.community[1].links[1],
    matrix: path.community[0].links[1],
    discussion: path.community[0].links[0],
  };
});
</script>

<template>
  <footer class="bg-gray-200 dark:bg-neutral-900">
    <!-- Footer Navigation -->
    <nav class="flex w-full py-9 md:justify-center xl:block">
      <div
        class="mx-4 grid max-w-screen-xl gap-3 sm:mx-auto sm:w-auto sm:grid-cols-2 md:grid-cols-3 md:gap-x-20 lg:grid-cols-4 xl:gap-10"
      >
        <FooterSection
          title="Editions"
          :links="navigation.downloads.sections[0].links"
        />
        <!-- <FooterSection
          title="Emerging Editions"
          :links="navigation.downloads.sections[1].links"
        /> -->
        <FooterSection
          title="Spins"
          :links="navigation.downloads.sections[2].links"
        />
        <FooterSection
          title="Labs"
          :links="navigation.downloads.sections[3].links"
        />

        <FooterSection
          title="User Support"
          :links="support"
          class="sm:col-start-2 sm:row-start-1 md:col-auto md:row-auto"
        />
        <FooterSection title="Community" :links="community" />
      </div>
    </nav>
    <!-- Fedora Section -->
    <section class="container mx-auto py-10">
      <div class="flex flex-wrap items-center gap-4 md:flex-nowrap">
        <div class="ml-4 pb-6 md:ml-0 md:w-1/4 md:pb-0">
          <FpImage
            src="assets/images/logos/fedora-blue.png"
            :alt="$t('Fedora Logo')"
            class="h-12 xl:ml-0"
          />
        </div>
        <!-- language selector -->
        <div
          class="mx-auto cursor-pointer pb-4 md:pb-0"
          @click="
            footerLanguageOpen = !footerLanguageOpen;
            categoryOpen = null;
            sectionOpen = null;
          "
        >
          <a
            class="inline-flex items-center rounded text-fp-gray-darkest underline underline-offset-1 transition duration-300 ease-in-out hover:text-fp-gray dark:text-fp-gray-light dark:hover:text-fp-gray-dark"
          >
            <span class="hidden md:block">{{ $t("Languages") }}</span
            ><span class="md:hidden"
              ><Icon name="fa6-solid:language" size="48" />
            </span>
          </a>
          <FpLanguageSelector :open="footerLanguageOpen" />
        </div>
        <!-- privacy etc links -->
        <ul
          class="mx-4 flex grow justify-center gap-4 lg:mx-0 lg:gap-8 xl:justify-start"
        >
          <li class="list-none underline underline-offset-1">
            <NuxtLink
              to="#"
              class="text-fp-gray-darkest transition duration-300 ease-in-out hover:text-fp-gray dark:text-fp-gray-light dark:hover:text-fp-gray-dark"
              >{{ $t("Privacy Statement") }}</NuxtLink
            >
          </li>
          <li class="list-none underline underline-offset-1">
            <NuxtLink
              to="#"
              class="text-fp-gray-darkest transition duration-300 ease-in-out hover:text-fp-gray dark:text-fp-gray-light dark:hover:text-fp-gray-dark"
              >{{ $t("Legal") }}</NuxtLink
            >
          </li>
          <li class="list-none underline underline-offset-1">
            <NuxtLink
              to="#"
              class="text-fp-gray-darkest transition duration-300 ease-in-out hover:text-fp-gray dark:text-fp-gray-light dark:hover:text-fp-gray-dark"
              >{{ $t("Code of Conduct") }}</NuxtLink
            >
          </li>
          <li class="list-none underline underline-offset-1">
            <NuxtLink
              to="#"
              class="text-fp-gray-darkest transition duration-300 ease-in-out hover:text-fp-gray dark:text-fp-gray-light dark:hover:text-fp-gray-dark"
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
