<script setup>
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
    <div v-if="props.image" class="flex h-64 items-center justify-center">
      <FpImage :image="props.image" />
    </div>
    <h4 class="inline font-bold text-fp-blue-dark">{{ props.title }}</h4>
    <p class="text-fp-blue-dark" v-html="props.description"></p>
    <br />
    <div v-if="props.url" class="flex items-center justify-center">
      <FpBtn :url="props.url">Learn More</FpBtn>
    </div>
  </li>
</template>
