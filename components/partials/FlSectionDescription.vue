<script setup>
const props = defineProps({
  content: {
    type: String,
  },
});

const contentMd = await mdparser(props.content);
</script>
<template>
  <ContentRenderer
    class="markdown text-center dark:text-gray-300 text-gray-600"
    tag="div"
    :value="contentMd"
  />
</template>
