<script setup>
import TheNavLogo from "./TheNavLogo.vue";
import TheNav from "./TheNav.vue";

// TODO: Programmatically set the nav logo's text to change depending on the specific page and router **Design Not finished yet**
</script>
<template>
  <!-- TODO: This is the top level navbar, it handles collapsing behviour and logic for page NavLogo context -->
  <header>
    <the-nav-logo></the-nav-logo>
    <!-- TODO: Make the nav programmatic based on section of the site-->
    <the-nav />
  </header>
</template>
