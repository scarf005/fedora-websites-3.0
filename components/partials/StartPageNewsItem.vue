<!-- vim:set ts=2 sw=2 et: -->

<script setup>
const props = defineProps({
  link: {
    type: String,
  },
  thumbnail: {
    type: String,
  },
  date: {
    type: String,
  },
  title: {
    type: String,
  },
  comments: {
    type: String,
  },
});
</script>

<template>
  <div>
    <div class="bg-fp-blue aspect-[472/200] rounded-lg">
      <a target="_blank" :href="link">
        <img :src="thumbnail" class="w-full rounded-lg overflow-hidden" />
      </a>
    </div>
    <div class="text-base leading-8 text-gray-500 flex justify-between">
      <div>{{ date }}</div>
      <a target="_blank" :href="link + '/#comments'">
        <div
          v-if="comments"
          class="relative -top-8 z-10 w-8 aspect-square rounded-full bg-gray-300/50 leading-none text-white flex justify-center border-4 border-transparent bg-clip-padding items-center"
        >
          {{ comments }}
        </div>
      </a>
    </div>
    <div class="max-h-[5.25rem] overflow-hidden">
      <a
        target="_blank"
        :href="link"
        class="align-top text-xl font-semibold text-fp-blue"
        >{{ title }}</a
      >
    </div>
  </div>
</template>

<style scoped>
a {
  cursor: default;
}
</style>
