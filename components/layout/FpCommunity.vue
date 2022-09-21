<script setup>
defineProps({
  data: Object,
});
</script>

<template>
  <FpHero :background="data.header.headerImage.image" alignment="bg-top">
    <section class="mx-auto w-10/12 max-w-screen-xl py-24">
      <h2 class="mb-5 text-center text-5xl font-semibold text-fp-blue">
        {{ data.header.sectionTitle }}
      </h2>
      <h4 class="mx-14 mb-5 text-fp-blue-dark">
        {{ data.header.subtitle1 }}
      </h4>
      <p class="mx-14 mb-8 text-fp-blue-dark">
        {{ data.header.subtitle2 }}
      </p>

      <FpList columns="sm:grid-cols-2 gap-12 lg:gap-4">
        <FpListItem v-for="item in data.content.list" v-bind="item" />
      </FpList>
    </section>
  </FpHero>
</template>
