<script setup>
import { mdparser } from "../../config/utilities";

const props = defineProps({
  data: Object,
});

const descriptionMd = await mdparser(props.data.sectionDescription);
</script>

<template>
  <FpHero :background="data.images" alignment="bg-top">
    <section class="mx-auto w-10/12 max-w-screen-xl py-24">
      <h2 class="mb-5 text-center text-5xl font-semibold text-fp-blue">
        {{ data.sectionTitle }}
      </h2>
      <ContentRendererMarkdown
        tag="h4"
        class="mx-14 mb-5 text-fp-blue-dark"
        :value="descriptionMd"
      />

      <FpList columns="sm:grid-cols-2 gap-12 lg:gap-4">
        <FpListItem v-for="item in data.content" v-bind="item" />
      </FpList>
    </section>
  </FpHero>
</template>
