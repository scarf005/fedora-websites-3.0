<script setup>
const menuOpen = ref(false);
</script>
<template>
  <div class="text-white">
    <button
      @click.prevent="menuOpen = !menuOpen"
      class="duration-300 ease-in-out hover:opacity-50"
    >
      <Icon v-if="menuOpen" name="line-md:close" size="32" />
      <Icon v-else name="fa6-solid:bars" size="32" />
    </button>
  </div>
</template>
