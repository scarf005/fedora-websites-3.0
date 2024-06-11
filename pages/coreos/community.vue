<script setup>
const { locale } = useI18n();
const data = await getCMS("editions/coreos/community");

const get_involved = data._value.sections[2];
if (process.server) {
  const meetings = await getMeetingTime("CoreOS");
  for (let c of get_involved.content) {
    setMeetingTime(c, meetings);
  }
}

useContentHead(data);
</script>

<template>
  <main class="border-t-8 border-fp-magenta dark:bg-neutral-800">
    <header>
      <TheLocalBar
        :image="{
          light: 'assets/images/fedora-coreos-logo-light.png',
          dark: 'assets/images/fedora-coreos-logo.png',
        }"
        home="/coreos"
        :items="[
          { name: 'Download', link: '/coreos/download' },
          { name: 'Community', link: '/coreos/community' },
        ]"
        textColor="text-fp-magenta"
      />
      <div class="px-8">
        <div class="my-8 mx-auto max-w-7xl text-center lg:text-start">
          <div class="container mx-auto lg:mx-0">
            <h1 class="mb-4 text-fp-magenta xl:mb-8">
              {{ $t(data.title) }}
            </h1>
            <p class="text-fp-gray">{{ $t(data.description) }}</p>
          </div>
        </div>
      </div>
      <FpDescriptionSection
        :sectionDescription="data.sections[0].sectionDescription"
        class="px-8 dark:bg-neutral-900"
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
      :sectionTitle="get_involved.sectionTitle"
      :content="get_involved.content"
      class="dark:bg-neutral-900"
    />

    <!-- Fedora Events -->
    <FpEventSection color="text-fp-magenta" />

    <!-- Publication Section -->
    <FpPublicationSection class="dark:bg-black" />
  </main>
</template>
