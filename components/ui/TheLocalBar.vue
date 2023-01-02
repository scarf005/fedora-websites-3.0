<script setup>
defineProps({
  home: String,
  image: String,
  items: Array,
  textColor: String,
});
</script>
<template>
  <div
    class="mx-auto mt-12 flex max-w-7xl flex-col justify-between sm:flex-row"
  >
    <FpLink :href="home">
      <FpImage
        class="mx-auto mb-5 max-h-8 w-auto sm:m-0 sm:mb-0"
        :src="image"
      />
    </FpLink>
    <div
      :class="`flex justify-center md:justify-end ${textColor || 'text-white'}`"
    >
      <FpLink class="px-5" v-for="item in items" :href="item.link">
        {{ $t(item.name) }}
      </FpLink>
    </div>
  </div>
</template>
