<script setup>
import navigation from "../../config/navigation.json";

let footerLanguageOpen = useState("footerLanguageOpen", () => null);
</script>

<template>
  <footer class="bg-gray-200 dark:bg-neutral-900">
    <!-- Footer Navigation -->
    <nav class="flex w-full py-9 md:justify-center xl:block">
      <div
        class="mx-4 grid w-full max-w-screen-xl gap-3 sm:mx-auto sm:w-auto sm:grid-cols-2 md:grid-cols-3 md:gap-x-20 lg:grid-cols-4 xl:gap-10"
      >
        <FooterSection
          title="Editions"
          :links="navigation.downloads.sections[0].links"
        />
        <FooterSection
          title="Spins"
          :links="navigation.downloads.sections[2].links"
        />
        <FooterSection
          title="Labs"
          :links="navigation.downloads.sections[3].links"
        />
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
        <!-- privacy etc links -->
        <ul
          class="mx-4 flex grow justify-center gap-4 lg:mx-0 lg:gap-8 xl:justify-start"
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
