<script setup>
import {
  desktops,
  cloud,
  iot,
  support,
  community,
} from "../../config/navigation";
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
  <nav class="fixed z-50 w-full bg-fp-blue">
    <div class="mx-auto max-w-7xl px-2 sm:px-6 lg:px-8">
      <div class="relative flex h-16 items-center justify-between">
        <div
          class="flex flex-1 items-center justify-center sm:items-stretch sm:justify-start"
        >
          <div class="flex flex-shrink-0 items-center">
            <a :href="`${$config.app.baseURL + '/'}`">
              <FpImage
                class="h-8 w-auto"
                image="assets/images/fedora_white.png"
              />
            </a>
          </div>

          <div class="hidden sm:ml-auto sm:block">
            <div class="flex space-x-4">
              <a
                class="inline-flex cursor-pointer items-center rounded px-4 text-sm text-white"
                href="https://docs.fedoraproject.org/en-US/project/"
              >
                <span class="mr-1">{{ $t("About") }}</span>
              </a>

              <TheNavItem
                :title="$t('Desktops')"
                :items="desktops"
                icons="true"
              />

              <TheNavItem :title="$t('Server & Cloud')" :items="cloud" />

              <TheNavItem :title="$t('IoT & Edge')" :items="iot" />

              <TheNavItem :title="$t('Community')" :items="community" />

              <TheNavItem :title="$t('Support')" :items="support" />

              <TheNavItem :title="$t('Languages')" :items="availableLocales" />
            </div>
          </div>
        </div>

        <!-- Mobile menu button-->
        <div class="flex items-center sm:hidden">
          <button
            @click="open = !open"
            type="button"
            class="inline-flex items-center justify-center rounded-md p-2 text-gray-400 hover:text-white"
            aria-controls="mobile-menu"
            aria-expanded="false"
          >
            <span class="sr-only">Open main menu</span>

            <svg
              class="block h-6 w-6"
              xmlns="http://www.w3.org/2000/svg"
              fill="none"
              viewBox="0 0 24 24"
              stroke-width="2"
              stroke="currentColor"
              aria-hidden="true"
            >
              <path
                stroke-linecap="round"
                stroke-linejoin="round"
                d="M4 6h16M4 12h16M4 18h16"
              />
            </svg>

            <svg
              class="hidden h-6 w-6"
              xmlns="http://www.w3.org/2000/svg"
              fill="none"
              viewBox="0 0 24 24"
              stroke-width="2"
              stroke="currentColor"
              aria-hidden="true"
            >
              <path
                stroke-linecap="round"
                stroke-linejoin="round"
                d="M6 18L18 6M6 6l12 12"
              />
            </svg>
          </button>
        </div>
      </div>
    </div>

    <!-- Mobile menu, show/hide based on menu state. -->
    <div class="sm:hidden" id="mobile-menu" v-if="open">
      <div class="space-y-1 px-2 pt-2 pb-3">
        <div>
          <a
            class="inline-flex cursor-pointer items-center rounded px-3 py-2 text-sm text-white"
            href="https://docs.fedoraproject.org/en-US/project/"
          >
            <span class="mr-1">About</span>
          </a>
        </div>
        <br />
        <div v-for="item in editions" :key="item.name">
          <a
            :href="`${$config.app.baseURL + '/' + item.href}`"
            :class="[
              item.current
                ? 'bg-gray-900 text-white'
                : 'text-white hover:text-fp-purple',
              'rounded-md px-3 py-2 text-sm font-medium',
            ]"
            :aria-current="item.current ? 'page' : undefined"
            >{{ item.name }}</a
          >
        </div>
        <br />
        <div v-for="item in variants" :key="item.name">
          <a
            :href="item.href"
            :class="[
              item.current
                ? 'bg-gray-900 text-white'
                : 'text-white  hover:text-fp-purple',
              'rounded-md px-3 py-2 text-sm font-medium',
            ]"
            :aria-current="item.current ? 'page' : undefined"
            >{{ item.name }}</a
          >
        </div>
        <br />
        <div v-for="item in community" :key="item.name">
          <a
            :href="item.href"
            :class="[
              item.current
                ? 'bg-gray-900 text-white'
                : 'text-white  hover:text-fp-purple',
              'rounded-md px-3 py-2 text-sm font-medium',
            ]"
            :aria-current="item.current ? 'page' : undefined"
            >{{ item.name }}</a
          >
        </div>
        <br />
        <div v-for="item in support" :key="item.name">
          <a
            :href="item.href"
            :class="[
              item.current
                ? 'bg-gray-900 text-white'
                : 'text-white  hover:text-fp-purple',
              'rounded-md px-3 py-2 text-sm font-medium',
            ]"
            :aria-current="item.current ? 'page' : undefined"
            >{{ item.name }}</a
          >
        </div>
      </div>
    </div>
  </nav>
</template>
