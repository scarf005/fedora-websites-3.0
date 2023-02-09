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
const emits = ["menuToggle"];

// variables
const filteredTitle = computed(() => {
  let title = props.title;
  return title
    .split(" ")
    .filter((word) => word != "Deployment")
    .join(" ");
});
const fedoraLabel = computed(() => {
  let label = props.addLabel;
  return label === true ? "Fedora" : "";
});
</script>
<template>
  <section>
    <div class="flex items-center justify-between sm:block">
      <h4 class="text-2xl font-semibold">{{ filteredTitle }}</h4>
      <div class="sm:hidden">
        <Icon name="fa6-solid:chevron-right" />
      </div>
    </div>
    <ul>
      <li v-for="link in links" :key="link.id">
        <NuxtLink :to="link.path">{{ fedoraLabel }} {{ link.label }}</NuxtLink>
      </li>
    </ul>
  </section>
</template>
