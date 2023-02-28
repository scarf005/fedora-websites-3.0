<script setup>
const data = await getCMS("sponsors");
// import data from cms see line 2 of flocktofedora.vue
</script>
<template>
  <main>
    <header>
      <div>
        <!-- h1 Hero Content -->
        <h1>{{ data.title }}</h1>
        <p>{{ data.description }}</p>
      </div>
      <div>
        <!-- Red Hat Section -->
        <h2>{{ data.sections[0].sectionDescription }}</h2>
      </div>
    </header>
    <pre> {{ data }} </pre>
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
