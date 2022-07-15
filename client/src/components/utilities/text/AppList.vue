<script setup></script>
<template>
  <!-- Use v-if with a conditional to set whether it is ul or ol, ul by default -->
  <ol v-if="placeholder">
    <slot></slot>
  </ol>
  <ul v-else>
    <slot></slot>
  </ul>
</template>
