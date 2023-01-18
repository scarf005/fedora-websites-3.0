<script setup>
let colorMode = useColorMode();

function setMode(value) {
  colorMode.preference = value;
}
</script>

<template>
  <button
    v-if="colorMode.preference === 'system'"
    @click="setMode('light')"
    class="cursor-pointer rounded-xl p-1 text-white hover:bg-fp-blue-dark md:p-3"
  >
    <Icon name="fa-solid:laptop" class="white" />
  </button>

  <button
    v-if="colorMode.preference === 'light'"
    @click="setMode('dark')"
    class="cursor-pointer rounded-xl p-1 text-white hover:bg-fp-blue-dark md:p-3"
  >
    <Icon name="fa-solid:sun" class="white" />
  </button>

  <button
    v-if="colorMode.preference === 'dark'"
    @click="setMode('system')"
    class="cursor-pointer rounded-xl p-1 text-white hover:bg-fp-blue-dark md:p-3"
  >
    <Icon name="fa-solid:moon" class="white" />
  </button>
</template>
