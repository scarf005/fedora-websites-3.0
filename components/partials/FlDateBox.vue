<script setup>
const props = defineProps({
  dayofweek: String,
  month: String,
  day: String | Number,
});
</script>
<template>
  <div class="text-xl leading-tight dark:text-white text-center">
    <span class="text-base leading-tight">{{ dayofweek }}</span
    ><br />
    {{ month }}<br />
    {{ day }}
  </div>
</template>
