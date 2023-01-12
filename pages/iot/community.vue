<script setup>
const { locale } = useI18n();
const data = await getCMS("editions/iot/community");
const events = await getCMS("partials/events");
useContentHead(data);
</script>
<template>
  <main class="mt-4 border-t-8 border-fp-purple">
    <TheLocalBar
      image="assets/images/fiot-logo.png"
      home="/iot"
      textColor="text-fp-purple"
      :items="[
        { name: 'Download', link: '/iot/download' },
        { name: 'Community', link: '/iot/community' },
        { name: 'Help', link: '/iot/help' },
      ]"
    />

    <FpHeader
      :title="data.title"
      :description="data.description"
      :details="data.sections[0].sectionDescription"
      color="text-fp-purple"
      bgColor="bg-fp-blue-light/10"
    />

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
    />

    <!-- Fedora Events -->
    <FpEventSection color="text-fp-purple" />
    <!-- Publication Section -->
    <FpPublicationSection />
  </main>
</template>
