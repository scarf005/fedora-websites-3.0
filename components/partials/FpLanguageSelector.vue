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
    class="absolute mt-5 w-56 rounded border border-fp-blue bg-fp-blue py-2 text-white"
    v-if="open"
  >
    <li v-for="item in availableLocales" :key="item.name" class="mb-2">
      <FpLink
        :href="item.href"
        :current="item.current"
        class="rounded-md px-3 py-4 text-base font-medium text-white"
      >
        {{ item.name }}
      </FpLink>
    </li>
  </ul>
</template>
