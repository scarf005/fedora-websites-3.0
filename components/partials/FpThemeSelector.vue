<script setup>
const colorMode = useColorMode();
</script>

<template>
  <div class="group relative inline-block">
    <button
      type="button"
      v-if="colorMode.preference === 'system'"
      @click="colorMode.preference = 'light'"
      class="hidden fill-white stroke-white sm:block"
    >
      <Icon name="fa-solid:laptop" class="white" />
    </button>

    <button
      type="button"
      v-if="colorMode.preference === 'light'"
      @click="colorMode.preference = 'dark'"
      class="hidden fill-white stroke-white sm:block"
    >
      <Icon name="fa-solid:sun" class="white" />
    </button>

    <button
      type="button"
      v-if="colorMode.preference === 'dark'"
      @click="colorMode.preference = 'system'"
      class="hidden fill-white stroke-white sm:block"
    >
      <Icon
        v-if="colorMode.preference === 'dark'"
        name="fa-solid:moon"
        class="white"
      />
    </button>
  </div>
</template>
