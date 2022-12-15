<script setup>
// if props are null then use async call

const { data } = await useAsyncData("navigation", () =>
  queryContent("_navigation").findOne()
);

const categories = {
  downloads: data._value.downloads,
  community: data._value.community,
  contributors: data._value.contributors,
  support: data._value.support,
};
</script>
<template>
  <nav>
    <!-- Category Menu -->
    <ul class="flex gap-6">
      <li
        v-for="category in categories"
        :key="category.id"
        class="text-lg font-medium text-white lg:text-xl"
      >
        <button @click.prevent="isMobile = !isMobile">
          <!--  -->
          <span>{{ category.icon }}</span>
          <span>{{ category.label }}</span>
        </button>
      </li>
    </ul>
    <!-- Populate Menu here -->
    <section></section>
  </nav>
</template>
