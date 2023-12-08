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
    <div class="bg-fp-blue aspect-[472/200] rounded-lg bg-white">
      <a
        target="_blank"
        :href="link"
        class="ease-in-out duration-300 hover:opacity-80"
      >
        <img :src="thumbnail" class="w-full rounded-lg overflow-hidden" />
      </a>
    </div>
    <div class="text-base leading-8 text-gray-500 flex justify-between">
      <div>{{ date }}</div>
      <a target="_blank" :href="link + '/#comments'">
        <div
          v-if="comments"
          class="relative -top-8 z-10 w-8 aspect-square ease-in-out duration-300 rounded-full bg-gray-300/50 hover:bg-gray-300 leading-none text-white hover:text-gray-700 dark:text-black flex justify-center border-4 border-transparent bg-clip-padding items-center"
        >
          {{ comments }}
        </div>
      </a>
    </div>
    <div
      class="relative -left-1 w-[calc(100%+8px)] -top-1 h-[calc(100%+8px)] max-h-[5.25rem] p-1 overflow-hidden hover:bg-gray-500/10 dark:hover:bg-gray-800 rounded-xl"
    >
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
