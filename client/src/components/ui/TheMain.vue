<script setup>
import { defineComponent, computed, reactive } from "vue";
import { useHead } from "@vueuse/head";
import { setEnvironmentData } from "worker_threads";
// TODO: Page components pass their page metadata to the main component which handles the logic for it. **NOTE** Make sure this performs well **NOTE**
const pageData = reactive({
  title: `Fedora Linux`,
  description: `Friends, Features, Freedom, First`
})
useHead({
  title: computed(() => siteData.title),
  meta: [
    {
      name: `description`,
      content: computed(() => siteData.description)
    }
  ]
})
</script>
<template>
  <!-- This serves as the root component for each page -->
  <main>
    <slot></slot>
  </main>
</template>
