<script setup>
import { mdparser } from "../../config/utilities";
const props = defineProps({
  color: {
    default: "green",
    type: String,
  },
  sectionTitle: {
    required: true,
    type: String,
  },
  content: {
    required: true,
    type: Object,
  },
});

for (let item of props.content) {
  item.descriptionMd = await mdparser(item.description);
}
</script>

<template>
  <section class="bg-fp-blue-light/10">
    <div
      class="container mx-auto grid justify-center gap-8 py-12 lg:grid-cols-2 lg:justify-start xl:py-8"
    >
      <header class="col-span-full my-8 mx-auto text-center lg:text-start">
        <h2 :class="`text-fp-${color}`" class="xl:text-4xl">
          {{ sectionTitle }}
        </h2>
      </header>
      <div
        v-for="item in content.slice(0, 2)"
        :key="item.id"
        class="mx-auto max-w-lg text-center lg:text-start"
      >
        <h3 class="font-medium text-fp-blue">{{ item.title }}</h3>
        <ContentRenderer
          tag="p"
          class="max-w-sm text-fp-gray-darkest"
          :value="item.descriptionMd"
        />
      </div>
      <FpJoinTip
        description="Attending a meeting or reporting and discussing issues you've found can be a great first step at contribution"
      />
    </div>
  </section>
</template>
