<script setup>
const open = useState("navbaropen", () => false);
const switchLocalePath = useSwitchLocalePath();
const { locales } = useI18n();
const availableLocales = computed(() => {  return (locales.value).map(i => ({ name: i.name, href: switchLocalePath(i.code)}))});

</script>

<template>
  <nav class="bg-fp-blue fixed w-full z-50">
    <div class="max-w-7xl mx-auto px-2 sm:px-6 lg:px-8">
      <div class="relative flex items-center justify-between h-16">
        <div class="flex-1 flex items-center justify-center sm:items-stretch sm:justify-start">
          <div class="flex-shrink-0 flex items-center">
            <a :href="`${$config.app.baseURL + '/'}`">
              <FpImage class="h-8 w-auto" image="assets/images/fedora_white.png" />
            </a>
          </div>

          <div class="hidden sm:block sm:ml-auto">
            <div class="flex space-x-4">
              <a
                class="text-white text-sm px-4 rounded inline-flex items-center cursor-pointer"
                href="https://docs.fedoraproject.org/en-US/project/"
              >
                <span class="mr-1">{{ $t('About') }}</span>
              </a>

              <TheNavItem :title="$t('Desktops')" :items="desktops" icons="true" />

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
          <button @click="open = !open" type="button"
            class="inline-flex items-center justify-center p-2 rounded-md text-gray-400 hover:text-white"
            aria-controls="mobile-menu" aria-expanded="false">
            <span class="sr-only">Open main menu</span>

            <svg class="block h-6 w-6" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"
              stroke-width="2" stroke="currentColor" aria-hidden="true">
              <path stroke-linecap="round" stroke-linejoin="round" d="M4 6h16M4 12h16M4 18h16" />
            </svg>

            <svg class="hidden h-6 w-6" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"
              stroke-width="2" stroke="currentColor" aria-hidden="true">
              <path stroke-linecap="round" stroke-linejoin="round" d="M6 18L18 6M6 6l12 12" />
            </svg>
          </button>
        </div>
      </div>
    </div>

    <!-- Mobile menu, show/hide based on menu state. -->
    <div class="sm:hidden" id="mobile-menu" v-if="open">
      <div class="px-2 pt-2 pb-3 space-y-1">
        <div>
          <a class="text-white text-sm px-3 py-2 rounded inline-flex items-center cursor-pointer"
            href="https://docs.fedoraproject.org/en-US/project/">
            <span class="mr-1">About</span>
          </a>
        </div>
        <br />
        <div v-for="item in editions" :key="item.name">
          <a :href="`${$config.app.baseURL + '/' + item.href}`" :class="[
            item.current
              ? 'bg-gray-900 text-white'
              : 'text-white hover:text-fp-purple',
            'px-3 py-2 rounded-md text-sm font-medium',
          ]" :aria-current="item.current ? 'page' : undefined">{{ item.name }}</a>
        </div>
        <br />
        <div v-for="item in variants" :key="item.name">
          <a :href="item.href" :class="[
            item.current
              ? 'bg-gray-900 text-white'
              : 'text-white  hover:text-fp-purple',
            'px-3 py-2 rounded-md text-sm font-medium',
          ]" :aria-current="item.current ? 'page' : undefined">{{ item.name }}</a>
        </div>
        <br />
        <div v-for="item in community" :key="item.name">
          <a :href="item.href" :class="[
            item.current
              ? 'bg-gray-900 text-white'
              : 'text-white  hover:text-fp-purple',
            'px-3 py-2 rounded-md text-sm font-medium',
          ]" :aria-current="item.current ? 'page' : undefined">{{ item.name }}</a>
        </div>
        <br />
        <div v-for="item in support" :key="item.name">
          <a :href="item.href" :class="[
            item.current
              ? 'bg-gray-900 text-white'
              : 'text-white  hover:text-fp-purple',
            'px-3 py-2 rounded-md text-sm font-medium',
          ]" :aria-current="item.current ? 'page' : undefined">{{ item.name }}</a>
        </div>
      </div>
    </div>
  </nav>
</template>
