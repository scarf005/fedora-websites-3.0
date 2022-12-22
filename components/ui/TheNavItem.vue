<script setup>
defineProps({
  itemData: {
    type: Object,
  },
});
const mobileMenuToggle = ref(false);
</script>
<template>
  <!-- Use onMounted() approach to switch function between showing the mobile and showing the desktop layouts -->
  <div
    class="mx-2 mt-4 flex cursor-pointer justify-between rounded-md py-4 px-2 text-white duration-150 ease-in-out hover:bg-fp-blue-dark lg:py-2"
    role="button"
    @click.prevent="mobileMenuToggle = !mobileMenuToggle"
  >
    <h3 class="font-medium">
      {{ itemData.label }}
    </h3>
    <div class="lg:hidden">
      <Icon name="fa6-solid:chevron-right" size="32" />
    </div>
  </div>
  <ul
    class="ml-10 text-lg text-white"
    :class="mobileMenuToggle ? 'block' : 'hidden'"
  >
    <li v-for="link in itemData.links" :key="link.id" class="py-1">
      <NuxtLink
        :to="link.path.length > 0 ? link.path : link.url"
        class="underline-offset-4 hover:underline"
        >{{ link.label }}</NuxtLink
      >
    </li>
  </ul>
</template>
