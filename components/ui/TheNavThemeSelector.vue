<script setup></script>
<template>
  <div class="group relative inline-block">
    <select
      v-model="$colorMode.preference"
      class="rounded bg-transparent text-sm text-white"
    >
      <option value="system">☀️/🌙</option>
      <option value="light">☀️</option>
      <option value="dark">🌙</option>
    </select>
  </div>
</template>
