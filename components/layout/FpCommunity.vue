<script setup>
defineProps({
  data: Object,
});
</script>

<template>
  <FpHero
    :background="data.images"
    alignment="bg-top"
    class="dark:bg-blend-difference"
  >
    <section class="mx-auto w-10/12 max-w-screen-xl py-24">
      <h2
        class="mb-5 text-center text-5xl font-semibold text-fp-blue dark:text-slate-100"
      >
        {{ data.sectionTitle }}
      </h2>
      <h4 class="mx-14 mb-5 text-fp-blue-dark dark:text-slate-300">
        {{ data.sectionDescription }}
      </h4>

      <FpList columns="sm:grid-cols-2 gap-12 lg:gap-4">
        <FpListItem v-for="item in data.content" v-bind="item" />
      </FpList>
    </section>
  </FpHero>
</template>
