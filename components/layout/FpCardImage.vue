<script setup>
defineProps({
    src: String,
});

</script>
<template>
  <img class="mx-auto mb-4 max-h-[100px]" :src="`${$config.app.baseURL + '/' + src.replace('public/', '')}`"/>
</template>
