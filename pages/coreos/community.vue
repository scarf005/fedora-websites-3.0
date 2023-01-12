<script setup>
const { locale } = useI18n();
const data = await getCMS("editions/coreos/community");

useContentHead(data);
</script>

<template>
  <main class="mt-4 border-t-8 border-fp-magenta">
    <header>
      <TheLocalBar
        image="assets/images/fedora-coreos-logo.png"
        home="/coreos"
        :items="[
          { name: 'Download', link: '/coreos/download' },
          { name: 'Community', link: '/coreos/community' },
          { name: 'Help', link: '/coreos/help' },
        ]"
        textColor="text-fp-magenta"
      />
      <section
        class="my-8 mx-auto max-w-7xl px-8 text-center lg:text-start xl:px-0"
      >
        <div class="container mx-auto">
          <h1 class="mb-4 text-fp-magenta xl:mb-8">{{ data.title }}</h1>
          <p class="text-fp-gray">{{ data.description }}</p>
        </div>
      </section>
      <FpDescriptionSection
        :sectionDescription="data.sections[0].sectionDescription"
      />
    </header>

    <!-- communication channels -->
    <FpCommunicationSection
      color="magenta"
      :sectionTitle="data.sections[1].sectionTitle"
      :content="data.sections[1].content"
    />

    <!-- ways to get involved -->
    <FpGetInvolvedSection
      color="magenta"
      :sectionTitle="data.sections[2].sectionTitle"
      :content="data.sections[2].content"
    />

    <!-- Fedora Events -->
    <FpEventSection color="text-fp-magenta" />

    <!-- Publication Section -->
    <FpPublicationSection />
  </main>
</template>
