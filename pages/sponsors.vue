<script setup>
const data = await getCMS("sponsors");
// import data from cms see line 2 of flocktofedora.vue
</script>
<template>
  <main>
    <header class="mt-8">
      <div class="mx-auto my-12 w-4/5">
        <!-- h1 Hero Content -->
        <h1>{{ data.title }}</h1>
        <p>{{ data.description }}</p>
      </div>
      <div class="bg-fp-newblue py-12">
        <div class="mx-auto flex w-4/5 gap-4 md:gap-10 xl:gap-16">
          <!-- Red Hat Section -->
          <FpImage :src="data.sections[0].images" class="object-contain" />
          <p class="max-w-sm lg:max-w-none">
            {{ data.sections[0].sectionDescription }}
          </p>
        </div>
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
