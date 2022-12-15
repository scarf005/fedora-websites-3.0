<script setup>
defineProps({
  global: {
    type: Boolean,
    default: false,
  },
  navItems: {
    type: Array,
    required: true,
  },
  home: {
    type: Object,
  },
});
</script>
<template>
  <nav>
    <!-- Home Button-->
    <div>
      <NuxtLink :to="home.url"
        ><FpImage :src="home.image" :alt="home.altText"
      /></NuxtLink>
    </div>
    <ul class="flex justify-center gap-5 pt-4 md:gap-12 lg:pt-0">
      <li v-for="item in navItems" :key="item.id">
        <!-- TODO emit toggle function -->
        <button v-if="global">
          <div class="my-2 lg:hidden">
            <Icon :name="item.icon" size="32" />
          </div>
          <p class="text-base md:text-xl">{{ item.label }}</p>
        </button>
        <!-- local menus -->
        <NuxtLink v-else to="item.url">
          <div class="my-2 lg:hidden" :class="item.color">
            <Icon :name="item.icon" size="32" />
          </div>
          <p>{{ item.label }}</p></NuxtLink
        >
      </li>
    </ul>
  </nav>
</template>
