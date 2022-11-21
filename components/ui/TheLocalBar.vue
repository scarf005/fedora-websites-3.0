<script setup>
defineProps({
  home: String,
  image: String,
  items: Array,
});
</script>
<template>
  <div
    class="mx-auto mt-12 flex max-w-7xl justify-between px-2 sm:px-6 lg:px-8"
  >
    <FpLink :href="home">
      <FpImage class="h-8 w-auto" :src="image" />
    </FpLink>
    <div class="flex justify-end text-white">
      <FpLink class="px-5" v-for="item in items" :href="item.link">
        {{ item.name }}
      </FpLink>
    </div>
  </div>
</template>
