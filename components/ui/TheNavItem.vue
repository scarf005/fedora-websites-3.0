<script setup>
defineProps({
  title: String,
  items: Array,
  icons: Boolean,
});
</script>
<template>
  <div class="group relative inline-block">
    <a
      class="inline-flex cursor-pointer items-center rounded px-4 text-sm text-white"
    >
      <span class="mr-1">{{ title }}</span>
      <svg
        class="h-4 fill-white"
        xmlns="http://www.w3.org/2000/svg"
        viewBox="0 0 20 20"
      >
        <path
          d="M9.293 12.95l.707.707L15.657 8l-1.414-1.414L10 10.828 5.757 6.586 4.343 8z"
        />
      </svg>
    </a>
    <ul
      class="absolute hidden w-56 rounded border border-fp-blue bg-white py-2 text-gray-700 group-hover:block"
    >
      <li v-for="item in items" :key="item.name" class="mb-2">
        <a
          :href="`${
            item.href.includes('https')
              ? item.href
              : $config.app.baseURL + item.href
          }`"
          :class="[
            'text-gray-500  hover:text-fp-purple',
            'rounded-md px-3 py-4 text-base font-medium',
          ]"
          :aria-current="item.current ? 'page' : undefined"
        >
          <Icon v-if="icons" :name="`fa6-solid:${item.icon}`" />
          {{ item.name }}
        </a>
      </li>
    </ul>
  </div>
</template>
