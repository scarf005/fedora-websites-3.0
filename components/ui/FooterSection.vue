<script setup>
defineProps({
  title: {
    type: String,
    default: "Section Title",
  },
  links: {
    type: Object,
  },
});
</script>
<template>
  <section>
    <h4 class="text-xl font-semibold">{{ title }}</h4>
    <ul>
      <li v-for="link in links" :key="link.id">
        <NuxtLink :to="link.path">{{ link.label }}</NuxtLink>
      </li>
    </ul>
  </section>
</template>
