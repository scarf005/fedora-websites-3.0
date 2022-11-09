<template>
  <div id="app">
    <TheNavBar />
    <main class="pt-12">
      <slot />
      <EventSection />
    </main>
    <TheFooter />
  </div>
</template>
