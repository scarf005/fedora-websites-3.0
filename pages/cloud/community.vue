<script setup>
const { locale } = useI18n();
const data = await getCMS("editions/cloud/community");

useContentHead(data);
</script>

<template>
  <main
    class="border-t-8 border-fp-newblue dark:border-fp-newblue-700 dark:bg-neutral-800 md:mt-2"
  >
    <header>
      <TheLocalBar
        :image="{
          light: 'assets/images/fedora-cloud-logo-light.png',
          dark: 'assets/images/fedora-cloud-logo.png',
        }"
        home="/cloud"
        class="sm:px-2"
        textColor="text-fp-newblue dark:text-fp-newblue-700"
        :items="[
          { name: 'Download', link: '/cloud/download' },
          { name: 'Community', link: '/cloud/community' },
        ]"
      />
      <section
        class="my-8 mx-auto max-w-7xl px-8 text-center lg:text-start xl:px-0"
      >
        <div class="container mx-auto">
          <h1 class="mb-4 text-fp-newblue dark:text-fp-newblue-700 xl:mb-8">
            {{ $t(data.title) }}
          </h1>
          <p class="text-fp-gray">{{ $t(data.description) }}</p>
        </div>
      </section>
      <FpDescriptionSection
        :sectionDescription="data.sections[0].sectionDescription"
        class="dark:bg-neutral-900"
      />
    </header>

    <!-- communication channels -->
    <FpCommunicationSection
      color="newblue"
      :sectionTitle="data.sections[1].sectionTitle"
      :content="data.sections[1].content"
    />

    <!-- ways to get involved -->
    <FpGetInvolvedSection
      color="newblue"
      :sectionTitle="data.sections[2].sectionTitle"
      :content="data.sections[2].content"
      class="dark:bg-neutral-900"
    />

    <!-- Fedora Events -->
    <FpEventSection color="text-fp-newblue" />

    <!-- Publication Section -->
    <FpPublicationSection class="dark:bg-black" />
  </main>
</template>
