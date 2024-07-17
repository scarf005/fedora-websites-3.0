<script setup>
const props = defineProps({
  legalNotices: {
    type: Array[String],
  },
  isMarkdown: {
    type: Boolean,
  },
});

const legalNoticesMd = await Promise.all(
  props.legalNotices.map(async (value) => await mdparser(value.attribution)),
);
</script>
<template>
  <div class="container mx-auto max-w-7xl">
    <div class="p-2">
      <ContentRenderer
        class="markdown text-center dark:text-white"
        tag="div"
        v-if="isMarkdown"
        v-for="notice in legalNoticesMd"
        :value="notice"
      />
      <p v-else="isMarkdown" v-for="notice in legalNotices">
        {{ notice }}
      </p>
    </div>
  </div>
</template>
