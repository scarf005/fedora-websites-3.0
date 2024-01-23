<script setup>
const release_data = await getCMS("release");
import navigation from "../../config/navigation.js";

useHead({
  title: "Fedora Atomic Desktops",
});
</script>
<template>
  <main class="dark:bg-neutral-800">
    <section
      class="bg-gradient-to-b from-fp-newblue-300/75 to-white px-2 pb-12 text-center dark:bg-none lg:text-start"
    >
      <TheLocalBar
        :image="{
          light: `assets/images/fedora-atomic-desktops-logo-light.png`,
          dark: `assets/images/fedora-atomic-desktops-logo-dark.png`,
        }"
        home="/atomic-desktops/"
        textColor="text-fp-newblue"
      />

      <!-- TITLE -->

      <div class="container mx-auto max-w-7xl px-2 pt-12">
        <h1 class="text-4xl text-gray-600 dark:text-gray-200">
          {{ $t("Atomic Desktops for Fedora") }}
        </h1>
        <div class="flex flex-col flex-wrap gap-8 lg:flex-row">
          <p class="mt-8 text-gray-600 dark:text-fp-gray-light">
            {{
              $t(
                "Find a Fedora atomic desktop to enhance your experience! You can find the latest versions of our atomic desktops here.",
              )
            }}
          </p>
          <div
            class="mx-auto flex h-32 w-32 flex-col items-center justify-center rounded-full bg-fp-newblue-500 p-3 text-white dark:bg-fp-newblue-700 md:h-48 md:w-48 md:p-10"
          >
            <p class="font-display text-xs font-semibold md:text-sm">
              {{ $t("Latest release") }}
            </p>
            <p class="font-display text-6xl font-bold md:text-8xl">
              {{ release_data.ga.releasever }}
            </p>
          </div>
        </div>
      </div>
    </section>

    <section class="space-y-24 py-24">
      <AtomicDesktopsPreviewSection
        v-for="atomic_desktop in navigation.downloads.sections.find(
          ({ label }) => label === 'Atomic Desktops',
        ).links"
        :name="`${atomic_desktop.path.split('/')[2]}`"
      >
        {{ atomic_desktop.description }}
      </AtomicDesktopsPreviewSection>
    </section>
  </main>
</template>

<style></style>
