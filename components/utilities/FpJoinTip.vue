<script setup>
defineProps({
  title: {
    type: String,
    default: "Become a Fedora Contributor",
  },
  description: {
    type: String,
    default: "Contact the Join SIG to start contributing",
  },
  link: {
    type: "Object",
  },
});
</script>
<template>
  <aside class="flex gap-2">
    <div>
      <h4 class="mb-2 text-lg font-semibold text-fp-blue-light">{{ title }}</h4>
      <p class="text-sm text-fp-gray-dark">
        {{ description }}
        <NuxtLink
          v-if="link"
          :to="link.url"
          class="ml-2 text-sm text-fp-blue-light transition duration-100 ease-in-out hover:opacity-75"
          >{{ link.text }}</NuxtLink
        >
        <NuxtLink
          v-else
          to="https://docs.fedoraproject.org/en-US/fedora-join/"
          class="ml-2 text-sm text-fp-blue-light transition duration-100 ease-in-out hover:opacity-75"
          >Learn More</NuxtLink
        >
      </p>
    </div>
    <Icon
      name="fa6-solid:door-open"
      class="order-first text-fp-blue-light"
      size="1.5rem"
    />
  </aside>
</template>
