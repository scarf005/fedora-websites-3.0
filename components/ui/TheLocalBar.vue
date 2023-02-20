<script setup>
defineProps({
  home: String,
  image: String,
  imageDark: String,
  items: Array,
  textColor: String,
});
</script>
<template>
  <div
    class="mx-auto mt-12 flex max-w-screen-xl flex-col justify-between sm:flex-row"
  >
    <FpLink :href="home">
      <FpImage
        class="b-5 mx-auto mb-5 max-h-8 w-auto sm:m-0 sm:mb-0 sm:pl-5 lg:mx-auto"
        :src="image"
        :darksrc="imageDark"
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
