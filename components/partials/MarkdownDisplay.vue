<script setup>
const props = defineProps({
  content: String,
});

const contentMd = await mdparser(props.content);
</script>
<template>
  <ContentRenderer
    class="markdown text-center dark:text-white"
    tag="div"
    :value="contentMd"
  />
</template>
