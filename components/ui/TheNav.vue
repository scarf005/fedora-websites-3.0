<script setup>
defineProps({
  categories: {
    type: [Array, Object],
  },
});
</script>
<template>
  <nav class="mx-auto">
    <!-- Category Menu -->
    <ul class="flex justify-center gap-5 pt-4 pb-4 md:gap-12 lg:pt-0">
      <li
        v-for="category in categories"
        :key="category.id"
        class="text-lg font-medium text-white lg:text-xl"
      >
        <button
          class="underline-offset-4 hover:opacity-75 active:underline active:opacity-75"
        >
          <div class="my-2 lg:hidden">
            <Icon :name="category.icon ? category.icon : ''" size="32" />
          </div>
          <p class="text-base md:text-xl">{{ category.label }}</p>
        </button>
      </li>
    </ul>
    <!-- Drop Down Hero Menu Activated by Top Level Categories -->
  </nav>
</template>
