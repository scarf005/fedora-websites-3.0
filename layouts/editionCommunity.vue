<script setup>
const { locale } = useI18n();
</script>
<template>
  <main>
    <slot />
    <EventSection />
    <PublicationSection />
  </main>
</template>
