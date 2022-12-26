<script setup>
const { locale } = useI18n();

let { data } = await useAsyncData("page-data", () => {
  return queryContent("/editions/cloud/community/" + locale._value).findOne();
});

if (data._value === null) {
  ({ data } = await useAsyncData("page-data-fallback", () => {
    return queryContent("/editions/cloud/community").sort().find();
  }));
  data._value = data._value[data._value.length - 1];
}

useContentHead(data);
</script>

<template>
  <main class="mt-4 border-t-8 border-fp-blue">
    <header>
      <TheLocalBar
        image="assets/images/fedora-cloud-logo.png"
        home="/cloud"
        :items="[
          { name: 'Download', link: '/cloud/download' },
          { name: 'Community', link: '/cloud/community' },
          { name: 'Help', link: '/cloud/help' },
        ]"
        textColor="text-fp-blue"
      />
      <section
        class="my-8 mx-auto max-w-7xl px-8 text-center lg:text-start xl:px-0"
      >
        <div class="container mx-auto">
          <h1 class="mb-4 text-fp-blue xl:mb-8">{{ data.title }}</h1>
          <p class="text-fp-gray">{{ data.description }}</p>
        </div>
      </section>
      <FpDescriptionSection
        :sectionDescription="data.sections[0].sectionDescription"
      />
    </header>

    <!-- communication channels -->
    <FpCommunicationSection
      color="blue"
      :sectionTitle="data.sections[1].sectionTitle"
      :content="data.sections[1].content"
    />

    <!-- ways to get involved -->
    <FpGetInvolvedSection
      color="blue"
      :sectionTitle="data.sections[2].sectionTitle"
      :content="data.sections[2].content"
    />

    <!-- Fedora Events -->
    <FpEventSection color="text-fp-blue" />

    <!-- Publication Section -->
    <FpPublicationSection />
  </main>
</template>
