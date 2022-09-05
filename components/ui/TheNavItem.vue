<script setup>
defineProps({
  title: String,
  items: Array,
  icons: Boolean
});
</script>
<template>
  <div class="group inline-block relative">
    <a
      class="text-white text-sm px-4 rounded inline-flex items-center cursor-pointer"
    >
      <span class="mr-1">{{title}}</span>
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
      class="absolute hidden text-gray-700 py-2 border border-fp-blue w-56 bg-white group-hover:block rounded"
    >
      <li v-for="item in items" :key="item.name" class="mb-2">
        <a
          :href="`${item.href.includes('https') ? item.href : $config.app.baseURL + item.href}`"
          :class="[
            'text-gray-500  hover:text-fp-purple',
            'px-3 py-4 rounded-md text-base font-medium',
          ]"
          :aria-current="item.current ? 'page' : undefined"
        >
          <font-awesome-icon v-if="icons" :icon="item.icon" />
          {{ item.name }}
        </a>
      </li>
    </ul>
  </div>
</template>
