<script setup>
import { editions, others, support, community } from "../../config/navigation";
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
    <div class="mx-auto px-2 sm:px-6 lg:px-8">
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
                :title="$t('Editions')"
                :items="editions"
                icons="true"
              />

              <TheNavItem :title="$t('Others')" :items="others" />

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
            class="inline-flex items-center justify-center rounded-md p-2 text-white"
          >
            <font-awesome-icon icon="hamburger" />
          </button>
        </div>
      </div>
    </div>

    <!-- Mobile menu, show/hide based on menu state. -->
    <div class="sm:hidden" id="mobile-menu" v-if="open">
      <div class="space-y-1 px-2 pt-2 pb-3">
        <a
          class="inline-flex cursor-pointer items-center rounded px-3 py-2 text-sm text-white"
          href="https://docs.fedoraproject.org/en-US/project/"
        >
          <span class="mr-1">About</span>
        </a>
      </div>
    </div>
  </nav>
</template>
