<script setup>
const menuOpen = false;
</script>
<template>
  <div class="text-white md:hidden">
    <button @click.prevent="">
      <Icon v-if="MenuOpen" name="line-md:close" class="text-xl" size="32" />
      <Icon v-else name="fa6-solid:bars" class="text-xl" size="32" />
    </button>
  </div>
</template>
