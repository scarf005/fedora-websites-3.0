<script setup>
defineProps({
  image: String,
  items: Array,
});
</script>
<template>
  <!-- This serves as the root component for each page -->
  <div
    class="mx-auto mt-12 flex max-w-7xl justify-between px-2 sm:px-6 lg:px-8"
  >
    <div>
      <FpImage class="h-8 w-auto" :image="image" />
    </div>
    <div class="flex justify-end text-white">
      <a class="px-5" v-for="item in items" :href="item.link">{{
        item.name
      }}</a>
    </div>
  </div>
</template>
