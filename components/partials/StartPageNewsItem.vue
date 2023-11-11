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
});
</script>

<template>
  <div>
    <div class="bg-fp-blue aspect-[472/200] rounded-lg">
      <a :href="link">
        <img :src="thumbnail" class="w-full rounded-lg overflow-hidden" />
      </a>
    </div>
    <div class="text-base leading-8 text-gray-500">
      {{ date }}
    </div>
    <div class="max-h-[5.25rem] overflow-hidden">
      <a :href="link" class="align-top text-xl font-semibold text-fp-blue">{{
        title
      }}</a>
    </div>
  </div>
</template>
