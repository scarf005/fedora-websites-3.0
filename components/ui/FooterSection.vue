<script setup>
const props = defineProps({
  title: {
    type: String,
    default: "Section Title",
  },
  links: {
    type: Object,
  },
  addLabel: {
    type: Boolean,
  },
});
const fedoraLabel = computed(() => {
  let label = props.addLabel;
  return label === true ? "Fedora" : "";
});
</script>
<template>
  <section>
    <h4 class="text-xl font-semibold">{{ title }}</h4>
    <ul>
      <li v-for="link in links" :key="link.id">
        <NuxtLink :to="link.path">{{ fedoraLabel }} {{ link.label }}</NuxtLink>
      </li>
    </ul>
  </section>
</template>
