<script setup>
defineProps({
  data: Object,
});
</script>

<template>
  <FpHero :background="data.header.headerImage.image" alignment="bg-top">
    <section class="w-10/12 mx-auto py-24">
      <h2 class="text-5xl font-semibold text-fp-blue text-center mb-5">
        {{ data.header.sectionTitle }}
      </h2>
      <h4 class="text-fp-blue-dark mb-5 mx-14">
        {{ data.header.subtitle1 }}
      </h4>
      <p class="text-fp-blue-dark mb-8 mx-14">
        {{ data.header.subtitle2 }}
      </p>

      <FpList columns="sm:grid-cols-2 gap-12 lg:gap-4">
        <FpListItem v-for="item in data.content.list" v-bind="item" />
      </FpList>
    </section>
  </FpHero>
</template>
