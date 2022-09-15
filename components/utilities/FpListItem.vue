<script setup>
const props = defineProps({
  title: String,
  description: String,
  iconURI: String,
});
</script>
<template>
  <li class="w-10/12 mb-8" 
    :style="iconURI ? {
      'background': `url(${
        $config.app.baseURL + '/' + iconURI.replace('public/', '')
      }) no-repeat left top`,
      'padding-left': '60px',
      'list-style': 'none'

    } : 'null'"
  >
    <h4 class="inline font-bold text-fp-blue-dark">{{ props.title }}</h4>
    <p class="text-fp-blue-dark" v-html="props.description"></p>
  </li>
</template>
