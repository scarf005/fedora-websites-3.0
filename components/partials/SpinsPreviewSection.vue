<script setup>
const { t } = useI18n();
const slots = useSlots();
const props = defineProps({
  name: {
    type: String,
  },
});
</script>

<template>
  <div :class="`mx-auto grid max-w-screen-xl grid-cols-1 md:grid-cols-2`">
    <div class="col-span-1 flex items-center justify-center p-5">
      <FpImage
        :src="`assets/images/spins/screenshot-${name}.jpg`"
        class="max-h-72 rounded-lg border border-neutral-900 drop-shadow-lg"
      />
    </div>
    <div
      :class="`col-span-1 flex flex-col items-center justify-center p-5 text-center sm:text-start md:items-start`"
    >
      <FpImage
        :src="{
          light: `assets/images/spins/spins-${name}-logo-light.png`,
          dark: `assets/images/spins/spins-${name}-logo-dark.png`,
        }"
        class="w-max"
      />
      <p class="pt-4 pb-12 font-normal text-gray-600 dark:text-gray-300">
        <slot></slot>
      </p>
      <div class="flex gap-4">
        <FpBtn
          :href="`/spins/${name}`"
          class="!rounded-md !px-10 !py-4 font-display text-sm font-bold"
          >{{ $t("Get Started") }}</FpBtn
        >
        <FpBtn
          :href="`/spins/${name}/download`"
          class="!rounded-md !px-10 !py-4 font-display text-sm font-bold"
          >{{ $t("Download Now") }}</FpBtn
        >
      </div>
    </div>
  </div>
</template>
