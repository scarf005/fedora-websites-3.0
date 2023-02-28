<script setup>
const data = await getCMS("sponsors");
// import data from cms see line 2 of flocktofedora.vue
</script>
<template>
  <main>
    <header class="mx-auto grid grid-cols-2">
      <div class="col-span-2 justify-self-center">
        <!-- h1 Hero Content -->
        <h1>{{ data.title }}</h1>
        <p>{{ data.description }}</p>
      </div>
      <div class="bg-fp-newblue">
        <!-- Red Hat Section -->
        <FpImage :src="data.sections[0].images" class="" />
      </div>
      <div class="bg-fp-newblue">
        <p class="max-w-prose">{{ data.sections[0].sectionDescription }}</p>
      </div>
    </header>
    <section>
      <header>
        <!-- h2 General  Sponsor Gallery Header -->
      </header>
      <div>
        <!-- Gallery Content -->
        <!-- Note: use v-for to loop -->
      </div>
    </section>
    <section>
      <header>
        <!-- h2 Flock Sponsor Gallery Header -->
      </header>
      <div>
        <!-- Gallery Content See line 364 of flocktofedora.vue -->
      </div>
    </section>
    <section>
      <header>
        <!-- h2 Sponsor Engagement Header -->
      </header>
      <div>
        <!-- Sponsor Engagement content -->
      </div>
    </section>
  </main>
</template>
