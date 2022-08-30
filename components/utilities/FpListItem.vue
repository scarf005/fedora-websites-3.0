<script setup>
const props = defineProps({
  title: String,
  description: String
})
</script>
<template>
  <li class="w-10/12">
    <h4 class="inline font-bold text-fp-blue-dark">{{ props.title }}</h4>
    <p class="text-fp-blue-dark">{{ props.description }}</p>
  </li>
</template>
