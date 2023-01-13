<script setup>
let colorMode = useColorMode();

function setMode(value) {
  colorMode.preference = value;
}
</script>

<template>
  <div class="group relative inline-block">
    <button
      v-if="colorMode.preference === 'system'"
      @click="setMode('light')"
      class="hidden fill-white stroke-white sm:block"
    >
      <Icon name="fa-solid:laptop" class="white" />
    </button>

    <button
      v-if="colorMode.preference === 'light'"
      @click="setMode('dark')"
      class="hidden fill-white stroke-white sm:block"
    >
      <Icon name="fa-solid:sun" class="white" />
    </button>

    <button
      v-if="colorMode.preference === 'dark'"
      @click="setMode('system')"
      class="hidden fill-white stroke-white sm:block"
    >
      <Icon name="fa-solid:moon" class="white" />
    </button>
  </div>
</template>
