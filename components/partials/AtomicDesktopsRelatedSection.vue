<script setup>
const data = await getCMS("partials/atomic-desktops-related");
const { t } = useI18n();
const route = useRoute();
const title = data._value.title;
const cards = data._value.cards.filter((card) => {
  return card.url != route.path;
});
</script>

<template>
  <div
    class="mx-auto max-w-7xl rounded-lg bg-white px-12 pt-6 pb-10 dark:bg-neutral-900"
  >
    <h2
      class="mb-8 text-center text-4xl font-semibold text-fp-blue-500 dark:text-gray-200"
    >
      {{ $t(title) }}
    </h2>
    <div
      class="flex flex-wrap justify-between gap-4 text-center text-fp-darkblue-500 xl:gap-10"
    >
      <FpCard
        v-for="card in cards"
        :description="card.description"
        class="mx-auto grow basis-64"
      >
        <template #prepend>
          <FpLink :href="card.url">
            <FpImage
              slot="prepend"
              class="mx-auto mb-4 h-16"
              :src="card.images"
            />
          </FpLink>
        </template>
      </FpCard>
    </div>
  </div>
</template>
