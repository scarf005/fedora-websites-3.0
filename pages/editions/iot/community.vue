<script setup>
const { locale } = useI18n();
let { data } = await useAsyncData("page-data", () => {
  return queryContent("/editions/iot/community." + locale._value).findOne();
});

if (data._value === null) {
  ({ data } = await useAsyncData("page-data-fallback", () => {
    return queryContent("/editions/iot/community").sort().find();
  }));
  data._value = data._value[data._value.length - 1];
}
let events = await useAsyncData(() => {
  return queryContent("/partials/events").findOne();
});
useContentHead(data);
</script>
<template>
  <main class="mt-4 border-t-8 border-fp-purple">
    <TheLocalBar
      image="assets/images/fiot-logo.png"
      home="/editions/iot"
      :items="[
        { name: 'Download', link: '/editions/iot/download' },
        { name: 'Community', link: '/editions/iot/community' },
        { name: 'Help', link: '/editions/iot/help' },
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
    <EventSection color="text-fp-purple" />
    <!-- Publication Section -->
    <PublicationSection />
  </main>
</template>
