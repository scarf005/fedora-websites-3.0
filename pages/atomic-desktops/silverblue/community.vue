<script setup>
const { locale } = useI18n();
const data = await getCMS("atomic-desktops/silverblue/community");

useContentHead(data);
</script>

<template>
  <main
    class="border-t-8 border-fp-newblue dark:border-fp-newblue-700 dark:bg-neutral-800"
  >
    <header>
      <TheLocalBar
        :image="{
          light: 'assets/images/fedora-silverblue-logo-light.png',
          dark: 'assets/images/fedora-silverblue-logo-dark.png',
        }"
        home="/atomic-desktops/silverblue"
        textColor="text-fp-newblue-700"
        :items="[
          { name: 'Download', link: '/atomic-desktops/silverblue/download' },
          {
            name: 'Community',
            link: '/atomic-desktops/silverblue/community',
          },
        ]"
      />
      <div class="px-8">
        <div class="my-8 mx-auto max-w-7xl text-center lg:text-start">
          <div class="container mx-auto lg:mx-0">
            <h1 class="mb-4 text-fp-newblue dark:text-fp-newblue-700 xl:mb-8">
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
      color="newblue"
      :sectionTitle="data.sections[1].sectionTitle"
      :content="data.sections[1].content"
    />

    <!-- ways to get involved -->
    <FpContributingSection
      color="newblue"
      :sectionTitle="data.sections[2].sectionTitle"
      :content="data.sections[2].content"
      class="dark:bg-neutral-900"
    />

    <!-- Event Section -->
    <FpEventSection color="text-fp-green-700" />

    <!-- Publication Section -->
    <FpPublicationSection class="dark:bg-black" />
  </main>
</template>
