<script setup>
import navigation from "../../config/navigation.json";

const switchLocalePath = useSwitchLocalePath();
const { locales } = useI18n();
const availableLocales = computed(() => {
  return locales.value.map((i) => ({
    label: i.name,
    path: switchLocalePath(i.code),
    i18n: true,
  }));
});
</script>

<template>
  <footer class="bg-gray-200 dark:bg-neutral-900">
    <!-- Footer Navigation -->
    <nav class="p-4 sm:px-[4em] sm:py-[1.5em]">
      <div
        class="mx-auto grid max-w-screen-xl gap-x-[4em] gap-y-2 sm:grid-cols-2 sm:gap-y-[1.5em] md:grid-cols-3 lg:grid-cols-4"
      >
        <FooterSection
          v-for="category in navigation.downloads.sections"
          :title="category.label"
          :links="category.links"
        />
        <FooterSection
          class="md:hidden"
          title="Languages"
          :links="availableLocales"
        />
      </div>
    </nav>
    <!-- Fedora Section -->
    <section class="container mx-auto py-10">
      <div class="flex flex-wrap items-center gap-4 md:flex-nowrap">
        <div class="pb-6 ltr:ml-4 rtl:mr-4 md:ml-0 md:w-1/5 md:pb-0">
          <FpImage
            src="assets/images/logos/fedora-blue.png"
            :alt="$t('Fedora Logo')"
            class="h-12 xl:ml-0"
          />
        </div>
        <!-- privacy etc links -->
        <ul
          class="mx-4 flex grow flex-wrap justify-center gap-4 lg:mx-0 lg:gap-8 xl:justify-start"
        >
          <li class="list-none underline underline-offset-1">
            <FpLink
              href="https://docs.fedoraproject.org/en-US/legal/privacy/"
              class="text-fp-gray-darkest transition duration-300 ease-in-out hover:text-fp-gray dark:text-fp-gray-light dark:hover:text-fp-gray-dark"
              >{{ $t("Privacy Statement") }}</FpLink
            >
          </li>
          <li class="list-none underline underline-offset-1">
            <FpLink
              href="https://docs.fedoraproject.org/en-US/legal/"
              class="text-fp-gray-darkest transition duration-300 ease-in-out hover:text-fp-gray dark:text-fp-gray-light dark:hover:text-fp-gray-dark"
              >{{ $t("Legal") }}</FpLink
            >
          </li>
          <li class="list-none underline underline-offset-1">
            <FpLink
              href="https://docs.fedoraproject.org/en-US/project/code-of-conduct/"
              class="text-fp-gray-darkest transition duration-300 ease-in-out hover:text-fp-gray dark:text-fp-gray-light dark:hover:text-fp-gray-dark"
              >{{ $t("Code of Conduct") }}</FpLink
            >
          </li>
          <li class="list-none underline underline-offset-1">
            <FpLink
              href="/sponsors"
              class="text-fp-gray-darkest transition duration-300 ease-in-out hover:text-fp-gray dark:text-fp-gray-light dark:hover:text-fp-gray-dark"
              >{{ $t("Sponsors") }}</FpLink
            >
          </li>
          <li class="list-none text-fp-gray-darkest">
            {{ $t("Help improve this website on the ") }}
            <FpLink
              href="https://fedora.gitlab.io/websites-apps/fedora-websites/fedora-websites-3.0/admin/"
              class="underline underline-offset-1 transition duration-300 ease-in-out hover:text-fp-gray dark:text-fp-gray-light dark:hover:text-fp-gray-dark"
              >{{ $t("CMS") }}</FpLink
            >
            {{ $t("or the ") }}
            <FpLink
              href="https://gitlab.com/fedora/websites-apps/fedora-websites/fedora-websites-3.0"
              class="underline underline-offset-1 transition duration-300 ease-in-out hover:text-fp-gray dark:text-fp-gray-light dark:hover:text-fp-gray-dark"
              >{{ $t("Gitlab Repo") }}</FpLink
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
            <FpLink
              href="https://docs.fedoraproject.org/en-US/quick-docs/fedora-and-red-hat-enterprise-linux/"
              class="block text-fp-gray underline underline-offset-1 xl:ml-2 xl:inline"
              >{{
                $t(
                  "Learn more about the relationship between Red Hat and Fedora."
                )
              }}</FpLink
            >
          </p>
        </div>
      </div>
    </section>
  </footer>
</template>
