<script setup>
import { editions, others, support, community } from "../../config/navigation";
const about = "https://docs.fedoraproject.org/en-US/project/";
const open = useState("navbaropen", () => false);
const switchLocalePath = useSwitchLocalePath();
const { locales } = useI18n();
const availableLocales = computed(() => {
  return locales.value.map((i) => ({
    name: i.name,
    href: switchLocalePath(i.code),
  }));
});
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
                image="assets/images/fedora_white.png"
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

    <!-- Mobile menu, show/hide based on menu state. -->
    <div class="sm:hidden" id="mobile-menu" v-if="open">
      <div class="flex flex-col overflow-scroll pb-4">
        <a class="px-3 py-2 text-sm text-white" :href="about"> About </a>
        <div class="my-2 px-2">
          <div class="w-full border-t border-gray-300" />
        </div>

        <a
          v-for="item in editions"
          :key="item.name"
          class="rounded-md px-3 py-2 text-sm font-medium text-white dark:text-gray-300"
          :href="`${
            item.href.includes('https')
              ? item.href
              : $config.app.baseURL.replace(new RegExp('/$'), '') + item.href
          }`"
          :aria-current="item.current ? 'page' : undefined"
        >
          <Icon v-if="icons" :name="`fa6-solid:${item.icon}`" />
          {{ item.name }}
        </a>

        <div class="my-2 px-2">
          <div class="w-full border-t border-gray-300" />
        </div>

        <a
          v-for="item in community"
          :key="item.name"
          class="rounded-md px-3 py-2 text-sm font-medium text-white dark:text-gray-300"
          :href="`${
            item.href.includes('https')
              ? item.href
              : $config.app.baseURL.replace(new RegExp('/$'), '') + item.href
          }`"
          :aria-current="item.current ? 'page' : undefined"
        >
          <Icon v-if="icons" :name="`fa6-solid:${item.icon}`" />
          {{ item.name }}
        </a>

        <div class="my-2 px-2">
          <div class="w-full border-t border-gray-300" />
        </div>

        <FpLink
          v-for="item in support"
          :key="item.name"
          class="rounded-md px-3 py-2 text-sm font-medium text-white dark:text-gray-300"
          :href="item.href"
          :current="item.current"
        >
          <Icon v-if="icons" :name="`fa6-solid:${item.icon}`" />
          {{ item.name }}
        </FpLink>
      </div>
    </div>
  </nav>
</template>
