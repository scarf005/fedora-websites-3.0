<script setup>
defineProps({
  color: {
    default: "text-fp-blue-dark",
    type: String,
  },
});
// Data Import
let { data } = await useAsyncData(() => {
  return queryContent("/partials/publications").findOne();
});
</script>
<template>
  <section class="bg-fp-gray-lightest">
    <div
      class="container mx-auto grid grid-cols-1 gap-4 py-12 lg:grid-cols-2 lg:gap-10"
    >
      <!-- Loop through publications -->
      <article
        v-for="card in data.body[0].content.slice(0, 2)"
        :key="card.id"
        class="my-10 flex flex-col items-center justify-between lg:my-8"
      >
        <header class="mx-4 flex flex-col justify-end xl:mx-0">
          <h3 class="hidden">{{ card.title }}</h3>
          <p class="mt-7 mb-1 max-w-prose text-fp-gray-darkest">
            {{ card.description }}
          </p>
          <FpBtn :url="card.link.url" class="mx-auto mt-10 px-4">{{
            card.link.text
          }}</FpBtn>
        </header>
        <div class="order-first mx-4 lg:mx-auto">
          <FpImage :image="card.image" class="mx-auto w-5/6" />
        </div>
      </article>
      <FpJoinTip :description="data.body[0].content[2].description" />
    </div>
  </section>
</template>
