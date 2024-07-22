<script setup>
const props = defineProps({
  dayofweek: String,
  month: String,
  day: String | Number,
});
</script>
<template>
  <div class="text-2xl leading-none dark:text-white text-center">
    <span class="text-lg">{{ dayofweek }}</span
    ><br />
    {{ month }}<br />
    {{ day }}
  </div>
</template>
