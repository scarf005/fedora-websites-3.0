<script setup>
defineProps({
  title: {
    type: String,
    default: "Nav Section Title",
  },
  navItems: {
    type: Array,
  },
});

const isOpen = ref(false);
onMounted(() => {
  onResize();
  window.addEventListener("resize", onResize, { passive: true });
});

function onResize() {
  isOpen.value = window.innerWidth < 640;
}
</script>
<template>
  <section>
    <div
      class="ml-6 mb-2 mr-6 flex items-start justify-between md:ml-0 md:mr-0 lg:mb-4"
    >
      <h6
        class="justify-start font-semibold text-fp-gray-darkest dark:text-fp-gray-light md:justify-start lg:font-bold"
      >
        {{ title }}
      </h6>

      <Icon
        name="fa6-solid:chevron-right"
        size="24"
        class="cursor-pointer text-fp-gray-darkest md:invisible"
        @click="isOpen = !isOpen"
        :class="isOpen ? 'rotate-90' : 'rotate-0'"
      />
    </div>
    <ul class="ml-6 md:ml-0" v-show="!isOpen">
      <li v-for="item in navItems" :key="item.id" class="mb-4 list-none">
        <NuxtLink
          :to="item.href"
          class="text-base font-medium text-fp-gray-darkest dark:text-fp-gray"
        >
          {{ item.name }}
        </NuxtLink>
      </li>
    </ul>
  </section>
</template>
