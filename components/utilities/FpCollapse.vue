<script setup>
const is_hidden = ref(true);
</script>

<template>
  <div class="flex items-center justify-start gap-4">
    <div>
      <slot name="head" class="">expandable section</slot>
    </div>
    <div>
      <span
        class="cursor-pointer font-sans text-sm underline"
        v-if="is_hidden"
        @click="is_hidden = !is_hidden"
        >details</span
      >
      <span
        class="cursor-pointer font-sans text-sm underline"
        v-if="!is_hidden"
        @click="is_hidden = !is_hidden"
        >collapse</span
      >
    </div>
  </div>
  <div v-show="!is_hidden">
    <slot></slot>
  </div>
</template>
