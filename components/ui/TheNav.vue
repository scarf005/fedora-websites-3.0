<script setup>
import navigation from "../../config/navigation.js";
const switchLocalePath = useSwitchLocalePath();
</script>

<template>
  <!-- DESKTOP NAVBAR -->
  <nav id="desktop" class="hidden md:flex h-[var(--nh)]">
    <div class="w-full h-[var(--nh)] px-2">
      <FpNavLogo />
    </div>
    <div
      class="section-headers h-full px-4 flex flex-none justify-end text-white"
    >
      <!-- note: 4px border reduces available height by 8px -->
      <div
        v-for="(category, level0index) in Object.keys(navigation)"
        :key="category"
        class="section-header relative flex items-center h-full rounded-2xl hover:bg-fp-blue-500 bg-clip-padding border-4 border-transparent"
      >
        <!-- DESKTOP HEADER -->
        <input
          :id="`button-${category}`"
          type="radio"
          name="lock"
          class="section-button absolute left-0 w-full top-0 h-full rounded-2xl block"
        />
        <label
          :for="`button-${category}`"
          class="relative z-10 px-2 text-sm text-white select-none block pointer-events-none"
          >{{ $t(navigation[category].label) }}</label
        >
        <!-- DESKTOP MENU -->
        <div
          :id="`section-menu-${category}`"
          class="section-menu fixed top-[var(--nh)] h-[var(--mhmd)] lg:h-[var(--mhlg)] xl:h-[var(--mhxl)] left-0 right-0 lg:px-[10vw] bg-neutral-100 dark:bg-neutral-900 overflow-hidden hidden"
        >
          <!-- DESKTOP SUBSECTIONS (LEFT COLUMN) -->
          <div class="py-2 w-[20vw]">
            <div
              class="px-2 text-base font-semibold uppercase text-fp-blue mb-2 select-none"
            >
              {{ $t(navigation[category].label) }}
            </div>
            <div
              v-for="(subsection, level1index) in navigation[category].sections"
              :key="`${category}-${level1index}`"
              :class="`subsection-header subsection-header-${level1index} relative`"
            >
              <input
                :id="`button-${category}-${level1index}`"
                type="radio"
                name="lock"
                class="subsection-button absolute left-0 w-full top-0 h-full z-10 rounded-2xl block hover:bg-gray-200 dark:hover:bg-gray-700 bg-clip-padding border-4 border-transparent duration-150 ease-in-out"
              />
              <label
                :for="`button-${category}-${level1index}`"
                class="relative w-[20vw] z-20 p-2 text-2xl leading-[30px] block text-gray-700 dark:text-gray-200 font-semibold select-none overflow-hidden"
                >{{ $t(subsection.label) }}</label
              >
              <!-- DESKTOP SUBSECTIONS (RIGHT COLUMN) -->
              <div
                :class="`subsection-menu subsection-menu-${level1index} fixed top-[var(--nh)] left-0 right-0 text-white bg-neutral-100 dark:bg-neutral-900 border-neutral-400 dark:border-neutral-600 ltr:left-[20vw] ltr:lg:left-[30vw] ltr:border-l rtl:right-[20vw] rtl:lg:right-[30vw] rtl:border-r ltr:lg:pr-[10vw] rtl:lg:pl-[10vw]`"
              >
                <div
                  class="p-4 h-[var(--mhmd)] lg:h-[var(--mhlg)] xl:h-[var(--mhxl)] overflow-y-auto"
                >
                  <div class="mb-6">
                    <div
                      class="text-3xl font-semibold text-gray-700 dark:text-gray-200 select-none"
                    >
                      {{ $t(subsection.label) }}
                    </div>
                    <div class="text-gray-500 dark:text-gray-400">
                      {{ $t(subsection.description) }}
                    </div>
                  </div>
                  <div class="grid grid-cols-3 gap-2">
                    <FpLink
                      v-for="link in subsection.links"
                      :key="link.id"
                      class="col-span-1 p-4 cursor-default rounded-xl hover:bg-gray-200 dark:hover:bg-gray-700"
                      :i18n="link.code ? true : false"
                      :href="
                        link.code ? switchLocalePath(link.code) : link.path
                      "
                    >
                      <span class="font-medium text-fp-blue">
                        <Icon
                          v-if="link.icon"
                          :name="link.icon"
                          size="32"
                          class="text-fp-blue"
                        />
                        {{ link.code ? link.name : $t(link.label) }}
                      </span>
                      <div
                        v-if="!link.code"
                        class="translate-y-2 text-base text-gray-700 dark:text-gray-400"
                      >
                        {{ $t(link.description) }}
                      </div>
                    </FpLink>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div class="px-2 inline-block flex items-center">
        <FpThemeSelector />
      </div>
    </div>
  </nav>

  <!-- MOBILE NAVBAR -->
  <nav id="mobile" class="flex flex-wrap md:hidden">
    <div class="w-[calc(100%-62px)] h-[var(--nh)] flex-none px-2">
      <FpNavLogo />
    </div>
    <input
      id="expander"
      type="checkbox"
      name="expander"
      class="w-[62px] h-[var(--nh)] flex-none block"
    />
    <div
      class="section-headers w-full h-0 overflow-hidden flex justify-around px-4 text-white"
    >
      <div
        v-for="(category, level0index) in Object.keys(navigation).slice(0, 4)"
        :key="category"
        :id="`section-header-${level0index}`"
        class="section-header relative h-[calc(var(--eh)-16px)] py-2"
      >
        <!-- MOBILE HEADER -->
        <div
          class="m-icon relative h-8 z-10 w-full py-1 flex justify-center pointer-events-none"
        >
          <Icon :name="navigation[category].icon" size="24" />
        </div>
        <input
          :id="`m-button-${category}`"
          type="radio"
          name="lock"
          class="section-button block absolute left-0 w-full top-2 h-[calc(100%-16px)] py-2 rounded-2xl"
        />
        <label
          :for="`m-button-${category}`"
          class="block relative z-10 px-2 text-sm text-white leading-none whitespace-nowrap select-none pointer-events-none"
          >{{ $t(navigation[category].label) }}</label
        >
        <!-- MOBILE MENU -->
        <div
          :id="`section-menu-${category}`"
          class="section-menu fixed left-0 right-0 top-[calc(var(--nh)+var(--eh))] bottom-0 bg-neutral-100 dark:bg-neutral-900 hidden"
        >
          <!-- MOBILE SUBSECTIONS -->
          <div
            v-for="(subsection, level1index) in navigation[category].sections"
            :key="`${category}-${level1index}`"
            :id="`subsection-header-${category}-${level1index}`"
            :class="`subsection-header subsection-header-${level1index} relative flex flex-wrap bg-neutral-100 dark:bg-neutral-900 font-semibold text-gray-700 dark:text-gray-200`"
          >
            <input
              :id="`m-button-${category}-${level1index}`"
              type="radio"
              :name="`${category}-lock`"
              class="subsection-button block absolute left-0 w-full top-0 h-[var(--shh)]"
            />
            <label
              :for="`m-button-${category}-${level1index}`"
              class="block relative w-[calc(100%-48px)] z-10 pointer-events-none flex-none px-2 text-2xl leading-[var(--shh)] select-none overflow-hidden whitespace-nowrap"
              >{{ $t(subsection.label) }}</label
            >
            <div
              class="relative w-[48px] z-10 pointer-events-none px-4 flex-none leading-[var(--shh)] select-none"
            >
              <Icon
                name="fa6-solid:chevron-right"
                class="rotate-90"
                size="16"
              />
            </div>
            <!-- MOBILE SUBSECTIONS (ACCORDION) -->
            <div
              :id="`subsection-menu-${category}-${level1index}`"
              :class="`subsection-menu subsection-menu-${level1index} w-full h-[var(--sah)] px-4 py-2 text-white overflow-y-auto`"
            >
              <FpLink
                v-for="link in subsection.links"
                :key="link.id"
                class="block mb-2 cursor-default rounded-xl select-none"
                :href="link.path"
              >
                <span class="font-medium text-fp-blue">
                  <Icon
                    v-if="link.icon"
                    :name="link.icon"
                    size="32"
                    class="text-fp-blue"
                  />
                  {{ $t(link.label) }}
                </span>
              </FpLink>
            </div>
          </div>
        </div>
      </div>
    </div>
  </nav>
</template>

<style scoped>
/* common desktop/mobile styling */

nav {
  --nh: 54px; /* navbar height */
  @apply fixed z-40 w-full from-fp-newblue-500 to-fp-blue ltr:bg-gradient-to-r rtl:bg-gradient-to-l dark:from-fp-darkblue-500 dark:to-fp-blue;
}

input {
  appearance: none;
  -webkit-appearance: none;
  outline-style: none;
}

/* desktop nav styling */

#desktop {
  --mhxl: 60vh; /* menu height for extra-large screen sizes */
  --mhlg: 70vh; /* menu height for large screen sizes */
  --mhmd: 80vh; /* menu height for medium screen sizes */

  /* primary buttons and menus (categories) */

  .section-header:hover .section-menu {
    @apply block shadow-xl;
  }

  .section-headers:hover .section-button:checked {
    @apply bg-fp-darkblue-700;

    & ~ .section-menu {
      @apply block z-50;
    }
  }

  /* secondary buttons and menus (subsections) */

  .subsection-menu:not(.subsection-menu-0) {
    @apply hidden;
  }

  .subsection-header:hover .subsection-menu {
    @apply block;
  }

  /*
    Safari is excluded because it locks the selection to the first submenu item on iPad.
    (https://twitter.com/simevidas/status/1434843473241329668)
  */
  @supports not (background: -webkit-named-image(i)) {
    .subsection-button:checked {
      @apply bg-gray-400 dark:bg-gray-800;

      & ~ .subsection-menu {
        @apply block z-50;
      }
    }
  }
}

/* mobile nav styling */

#mobile {
  --eh: 86px; /* expansion height */
  --shh: 46px; /* subsection header height */
  --sah: 240px; /* subsection accordion height */

  #expander {
    /*
      bars (classic, solid)
      Font Awesome Free 6.5.0 by @fontawesome - https://fontawesome.com
      License - https://fontawesome.com/license/free
      Copyright 2023 Fonticons, Inc.
    */
    background-image: url("data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCA0NDggNTEyIiA+PHBhdGggZmlsbD0iI0ZGRkZGRiIgZD0iTTAgOTZDMCA3OC4zIDE0LjMgNjQgMzIgNjRINDE2YzE3LjcgMCAzMiAxNC4zIDMyIDMycy0xNC4zIDMyLTMyIDMySDMyQzE0LjMgMTI4IDAgMTEzLjcgMCA5NnpNMCAyNTZjMC0xNy43IDE0LjMtMzIgMzItMzJINDE2YzE3LjcgMCAzMiAxNC4zIDMyIDMycy0xNC4zIDMyLTMyIDMySDMyYy0xNy43IDAtMzItMTQuMy0zMi0zMnpNNDQ4IDQxNmMwIDE3LjctMTQuMyAzMi0zMiAzMkgzMmMtMTcuNyAwLTMyLTE0LjMtMzItMzJzMTQuMy0zMiAzMi0zMkg0MTZjMTcuNyAwIDMyIDE0LjMgMzIgMzJ6Ii8+PC9zdmc+Cg==");
    background-size: 24px;
    background-repeat: no-repeat;
    background-position: center;

    &:checked + .section-headers {
      @apply h-[var(--eh)] py-2; /* note: py-2 reduces available height by 16px */

      .subsection-menu:not(
          .subsection-button:indeterminate ~ .subsection-menu-0
        ) {
        @apply hidden;
      }

      #section-header-0 .section-button:indeterminate {
        @apply bg-fp-darkblue-700;

        & ~ #section-menu-downloads {
          @apply block;

          .subsection-button:focus ~ .subsection-menu {
            @apply block;
          }
        }
      }

      .section-button {
        & ~ .section-menu .subsection-button:checked ~ .subsection-menu {
          @apply block;
        }

        &:checked {
          @apply bg-fp-darkblue-700;

          & ~ .section-menu,
          &:focus
            ~ .section-menu
            .subsection-button:indeterminate
            ~ .subsection-menu-0,
          & ~ .section-menu .subsection-button:focus ~ .subsection-menu {
            @apply block;
          }
        }
      }
    }

    &:checked:focus + .section-headers {
      .section-button:checked ~ .section-menu {
        .subsection-button:indeterminate ~ .subsection-menu-0 {
          @apply block;
        }
      }
    }
  }
}
</style>
