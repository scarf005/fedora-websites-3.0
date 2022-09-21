<script setup>
import FpBtn1 from "./FpBtn.vue";
const props = defineProps({
  title: String,
  description: String,
  image: String,
  url: String,
  iconURI: String,
});
</script>
<template>
  <li
    class="mb-8 w-10/12"
    :style="
      iconURI
        ? {
            background: `url(${
              $config.app.baseURL + '/' + iconURI.replace('public/', '')
            }) no-repeat left top`,
            'padding-left': '60px',
            'list-style': 'none',
          }
        : 'null'
    "
  >
    <FpImage v-if="props.image" :image="props.image.image" />
    <h4 class="inline font-bold text-fp-blue-dark">{{ props.title }}</h4>
    <p class="text-fp-blue-dark" v-html="props.description"></p>
    <br />
    <FpBtn v-if="props.url" :url="props.url">{{ props.url }}</FpBtn>
  </li>
</template>
