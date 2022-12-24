<script setup>
const props = defineProps({
  menu: {
    type: Object || Array,
  },
});
</script>
<template>
  <div>
    <header class="mb-6 mt-4">
      <h3 class="font-semibold">
        {{ menu.label }}
      </h3>
      <p>{{ menu.description }}</p>
    </header>
    <ul class="grid grid-cols-3 gap-4">
      <li
        v-for="link in menu.links"
        :key="link.id"
        class="max-w-xs rounded-lg hover:bg-fp-blue-dark"
      >
        <NuxtLink :to="link.url">
          <h4 class="mb-2 font-medium">{{ link.label }}</h4>
          <p>{{ link.description }}</p>
        </NuxtLink>
      </li>
    </ul>
  </div>
</template>
