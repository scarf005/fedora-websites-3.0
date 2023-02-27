<script setup>
const { locale } = useI18n();
const data = await getCMS("editions/iot/community");

useContentHead(data);
</script>
<template>
  <main class="border-t-8 border-fp-purple dark:bg-neutral-800 md:mt-2">
    <header>
      <TheLocalBar
        :image="{
          light: 'assets/images/fedora-iot-logo-light.png',
          dark: 'assets/images/fedora-iot-logo.png',
        }"
        home="/iot"
        textColor="text-fp-purple"
        :items="[
          { name: 'Download', link: '/iot/download' },
          { name: 'Community', link: '/iot/community' },
        ]"
      />

      <section
        class="my-8 mx-auto max-w-7xl px-8 text-center lg:text-start xl:px-0"
      >
        <div class="container mx-auto">
          <h1 class="mb-4 text-fp-purple xl:mb-8">
            {{ data.title }}
          </h1>
          <p class="text-fp-gray">{{ data.description }}</p>
        </div>
      </section>
      <FpDescriptionSection
        :sectionDescription="data.sections[0].sectionDescription"
        class="dark:bg-neutral-900"
      />
    </header>

    <!-- communication channels -->
    <FpCommunicationSection
      color="purple"
      :sectionTitle="data.sections[1].sectionTitle"
      :content="data.sections[1].content"
    />

    <!-- ways to get involved -->
    <FpGetInvolvedSection
      color="purple"
      :sectionTitle="data.sections[2].sectionTitle"
      :content="data.sections[2].content"
      class="dark:bg-neutral-900"
    />

    <!-- Fedora Events -->
    <FpEventSection color="text-fp-purple" />
    <!-- Publication Section -->
    <FpPublicationSection class="dark:bg-black" />
  </main>
</template>
