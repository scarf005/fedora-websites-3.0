<script setup>
const props = defineProps({
  open: Boolean || null,
});

const switchLocalePath = useSwitchLocalePath();
const { locales } = useI18n();
const availableLocales = computed(() => {
  return locales.value.map((i) => ({
    name: i.name,
    href: switchLocalePath(i.code),
  }));
});
</script>
<template>
  <ul
    class="absolute mt-4 w-32 rounded-b-xl border border-fp-blue bg-fp-blue py-2 text-white"
    v-if="open"
  >
    <li
      v-for="item in availableLocales"
      :key="item.name"
      class="mb-2 w-28 overflow-hidden text-ellipsis px-1"
    >
      <NuxtLink :href="item.href" :current="item.current">
        {{ item.name }}
      </NuxtLink>
    </li>
  </ul>
</template>
