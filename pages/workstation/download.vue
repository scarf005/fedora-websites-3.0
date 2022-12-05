<script setup>
const { data } = await useAsyncData("page-data", () => {
  return queryContent("/editions/workstation/download").find();
});
</script>
<template>
  <TheLocalBar
    image="assets/images/workstation_logo.png"
    home="/workstation"
    :items="[
      { name: 'Download', link: '/workstation/download' },
      { name: 'Community', link: '/workstation/community' },
      { name: 'Help', link: '/workstation/help' },
    ]"
  />
</template>
