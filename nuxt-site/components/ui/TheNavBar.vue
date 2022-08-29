<script setup>
const editions = [
  { name: "Workstation", href: "editions/workstation", icon: "fa fa-desktop" },
  { name: "IoT", href: "editions/iot", icon: "fa fa-microchip" },
  { name: "Server", href: "editions/server", icon: "fa fa-server" },
];
const events = [
  { name: "Flock To Fedora", href: "flocktofedora", icon: "fa fa-egg" },
];

const flavors = [
  { name: "Spins", href: "https://spins.fedoraproject.org/" },
  { name: "Labs", href: "https://labs.fedoraproject.org/" },
  { name: "Arm", href: "https://arm.fedoraproject.org/" },
  { name: "Silverblue", href: "https://silverblue.fedoraproject.org/" },
  { name: "Kinoite", href: "https://kinoite.fedoraproject.org/" },
];
const open = useState("counter", () => false);
</script>

<template>
  <nav class="bg-blue fixed w-full z-50">
    <div class="max-w-7xl mx-auto px-2 sm:px-6 lg:px-8">
      <div class="relative flex items-center justify-between h-16">
        <div class="absolute inset-y-0 left-0 flex items-center sm:hidden">
          <!-- Mobile menu button-->
          <button
            @click="open = !open"
            type="button"
            class="inline-flex items-center justify-center p-2 rounded-md text-gray-400 hover:text-white hover:bg-gray-700 focus:outline-none focus:ring-2 focus:ring-inset focus:ring-white"
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
        <div
          class="flex-1 flex items-center justify-center sm:items-stretch sm:justify-start"
        >
          <div class="flex-shrink-0 flex items-center">
            <a :href="`${$config.app.baseURL + '/'}`">
              <FpImage
                class="h-8 w-auto"
                image="assets/images/fedora_white.png"
              />
            </a>
          </div>
          <div class="hidden sm:block sm:ml-auto">
            <div class="flex space-x-4">
              <div class="group inline-block relative">
                <a
                  class="text-white text-sm px-4 rounded inline-flex items-center cursor-pointer"
                >
                  <span class="mr-1">Official</span>
                  <svg
                    class="fill-white h-4"
                    xmlns="http://www.w3.org/2000/svg"
                    viewBox="0 0 20 20"
                  >
                    <path
                      d="M9.293 12.95l.707.707L15.657 8l-1.414-1.414L10 10.828 5.757 6.586 4.343 8z"
                    />
                  </svg>
                </a>
                <ul
                  class="absolute hidden text-gray-700 py-2 border border-blue w-48 bg-white group-hover:block rounded"
                >
                  <li v-for="item in editions" :key="item.name">
                    <a
                    :href="`${$config.app.baseURL + '/' + item.href}`"
                      :class="[
                        item.current
                          ? 'bg-gray-900 text-gray-500'
                          : 'text-gray-500 hover:bg-gray-700 hover:text-purple',
                        'px-3 py-4 rounded-md text-base font-medium',
                      ]"
                      :aria-current="item.current ? 'page' : undefined"
                    >
                      <!-- <font-awesome-icon :icon="item.icon" /> -->
                      {{ item.name }}</a
                    >
                  </li>
                </ul>
              </div>

              <div class="group inline-block relative">
                <a
                  class="text-white text-sm px-4 rounded inline-flex items-center cursor-pointer"
                >
                  <span class="mr-1">Community</span>
                  <svg
                    class="fill-white h-4"
                    xmlns="http://www.w3.org/2000/svg"
                    viewBox="0 0 20 20"
                  >
                    <path
                      d="M9.293 12.95l.707.707L15.657 8l-1.414-1.414L10 10.828 5.757 6.586 4.343 8z"
                    />
                  </svg>
                </a>
                <ul
                  class="absolute hidden text-gray-700 py-2 border border-blue w-48 bg-white group-hover:block rounded"
                >
                  <li v-for="item in flavors" :key="item.name">
                    <a
                      :href="item.href"

                      :class="[
                        item.current
                          ? 'bg-gray-900 text-gray-500'
                          : 'text-gray-500 hover:bg-gray-700 hover:text-purple',
                        'px-3 py-4 rounded-md text-base font-medium',
                      ]"
                      :aria-current="item.current ? 'page' : undefined"
                    >
                      <!-- <font-awesome-icon :icon="item.icon" /> -->
                      {{ item.name }}</a
                    >
                  </li>
                </ul>
              </div>

              <div class="group inline-block relative">
                <a
                  class="text-white text-sm px-4 rounded inline-flex items-center cursor-pointer"
                >
                  <span class="mr-1">Events</span>
                  <svg
                    class="fill-white h-4"
                    xmlns="http://www.w3.org/2000/svg"
                    viewBox="0 0 20 20"
                  >
                    <path
                      d="M9.293 12.95l.707.707L15.657 8l-1.414-1.414L10 10.828 5.757 6.586 4.343 8z"
                    />
                  </svg>
                </a>
                <ul
                  class="absolute hidden text-gray-700 py-2 border border-blue bg-white w-48 group-hover:block rounded"
                >
                  <li v-for="item in events" :key="item.name">
                    <a
                      :href="`${$config.app.baseURL + '/' + item.href}`"
                      :class="[
                        item.current
                          ? 'bg-gray-900 text-gray-500'
                          : 'text-gray-500 hover:bg-gray-700 hover:text-purple',
                        'px-3 py-4 rounded-md text-base font-medium',
                      ]"
                      :aria-current="item.current ? 'page' : undefined"
                    >
                      <!-- <font-awesome-icon :icon="item.icon" /> -->
                      {{ item.name }}</a
                    >
                  </li>
                </ul>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- Mobile menu, show/hide based on menu state. -->
    <div class="sm:hidden" id="mobile-menu" v-if="open">
      <div class="px-2 pt-2 pb-3 space-y-1">
        <a
          v-for="item in editions"
          :key="item.name"
          :href="`${$config.app.baseURL + '/' + item.href}`"
          :class="[
            item.current
              ? 'bg-gray-900 text-white'
              : 'text-white hover:bg-gray-700 hover:text-purple',
            'px-3 py-2 rounded-md text-sm font-medium',
          ]"
          :aria-current="item.current ? 'page' : undefined"
          >{{ item.name }}</a
        >
        <a
          v-for="item in events"
          :key="item.name"
          :href="`${$config.app.baseURL + '/' + item.href}`"
          :class="[
            item.current
              ? 'bg-gray-900 text-white'
              : 'text-white hover:bg-gray-700 hover:text-purple',
            'px-3 py-2 rounded-md text-sm font-medium',
          ]"
          :aria-current="item.current ? 'page' : undefined"
          >{{ item.name }}</a
        >
      </div>
    </div>
  </nav>
</template>
