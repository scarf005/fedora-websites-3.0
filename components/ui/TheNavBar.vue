<script setup>
import {
  editions,
  others,
  support,
  community,
  about,
} from "../../config/navigation";
const switchLocalePath = useSwitchLocalePath();
const { locales } = useI18n();
const availableLocales = computed(() => {
  return locales.value.map((i) => ({
    name: i.name,
    href: switchLocalePath(i.code),
  }));
});

const open = useState("navopen", () => false);
</script>

<template>
  <nav class="fixed z-50 w-full bg-fp-blue dark:bg-neutral-900">
    <div class="mx-auto px-2 sm:px-6 lg:px-8">
      <div class="relative flex h-16 items-center justify-between">
        <div
          class="flex flex-1 items-center justify-center sm:items-stretch sm:justify-start"
        >
          <div class="flex flex-shrink-0 items-center">
            <FpLink href="/">
              <FpImage
                class="h-8 w-auto"
                src="assets/images/fedora_white.png"
              />
            </FpLink>
          </div>

          <div class="hidden sm:ml-auto sm:block">
            <div class="flex space-x-4">
              <FpLink
                :href="about"
                class="inline-flex cursor-pointer items-center rounded px-4 text-sm text-white"
              >
                <span class="mr-1">{{ $t("About") }}</span>
              </FpLink>

              <TheNavItem
                :title="$t('Editions')"
                :items="editions"
                :icons="true"
              />

              <TheNavItem :title="$t('Others')" :items="others" />

              <TheNavItem :title="$t('Community')" :items="community" />

              <TheNavItem :title="$t('Support')" :items="support" />

              <TheNavItem :title="$t('Languages')" :items="availableLocales" />
              <TheNavThemeSelector />
            </div>
          </div>
        </div>

        <!-- Mobile menu button-->
        <div class="flex items-center sm:hidden">
          <button
            @click="open = !open"
            type="button"
            class="inline-flex items-center justify-center rounded-md p-2 text-white"
          >
            <Icon name="fa6-solid:bars" />
          </button>
        </div>
      </div>
    </div>

    <!-- Mobile menu, show/hide based on mobile menu state. -->
    <div :class="`mb-2 ${!open && 'hidden'} h-screen overflow-scroll`">
      <div class="flex flex-col pb-4">
        <div class="ml-6 mb-4 md:ml-0 md:mr-0 lg:mb-4">
          <a
            class="font-semibold text-fp-gray-lightest dark:text-fp-gray-light lg:font-bold"
            :href="about"
          >
            About
          </a>
        </div>

        <div
          class="container grid gap-2 md:grid-cols-2 lg:grid-cols-4 lg:gap-8"
        >
          <FpCollapsibleSection
            title="Editions"
            :navItems="editions"
            use="nav"
          />
          <FpCollapsibleSection title="Others" :navItems="others" use="nav" />
          <FpCollapsibleSection
            title="User Support"
            :navItems="support"
            use="nav"
          />
          <FpCollapsibleSection
            title="Community"
            :navItems="community"
            use="nav"
          />
        </div>
      </div>
    </div>
  </nav>
</template>
