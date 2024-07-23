<script setup>
const props = defineProps({
  content: {
    type: String,
  },
  isMarkdown: {
    type: Boolean,
    default: false,
  },
});

const contentMd = await mdparser(props.content);
</script>
<template>
  <ContentRenderer
    class="markdown text-center dark:text-gray-300 text-gray-600"
    tag="div"
    :value="contentMd"
    v-if="isMarkdown"
  />
  <p
    class="mx-auto max-w-lg text-center font-normal text-gray-600 dark:text-gray-300"
    v-else="isMarkdown"
  >
    {{ $t(content) }}
  </p>
</template>
