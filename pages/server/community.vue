<script setup>
const { locale } = useI18n();
const data = await getCMS("editions/iot/community");
const events = await getCMS("partials/events");
useContentHead(data);
</script>
<template>
  <main class="border-t-8 border-fp-orange md:mt-2">
    <TheLocalBar
      image="assets/images/fedora_white.png"
      home="/iot"
      textColor="text-fp-orange"
      :items="[
        { name: 'Download', link: '/server/download' },
        { name: 'Community', link: '/server/community' },
      ]"
    />

    <FpHeader
      :title="data.title"
      :description="data.description"
      :details="data.sections[0].sectionDescription"
      color="text-fp-orange"
      bgColor="bg-fp-blue-light/10"
    />

    <!-- communication channels -->
    <FpCommunicationSection
      color="orange"
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
