<script setup>
defineProps({
  home: String,
  image: String,
  items: Array,
});
</script>
<template>
  <div
    class="mx-auto mt-12 flex max-w-7xl flex-col justify-between px-2 sm:flex-row sm:px-6 lg:px-8"
  >
    <FpLink :href="home">
      <FpImage
        class="mx-auto mb-5 max-h-8 w-auto sm:m-0 sm:mb-0"
        :src="image"
      />
    </FpLink>
    <div class="flex justify-end text-white drop-shadow">
      <FpLink class="px-5" v-for="item in items" :href="item.link">
        {{ item.name }}
      </FpLink>
    </div>
  </div>
</template>
