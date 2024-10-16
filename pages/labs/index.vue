<script setup>
const route = useRoute();
const release_data = await getCMS("release");
import navigation from "../../config/navigation.js";

useHead({
  title: "Fedora Labs",
});

const beta = computed(() => typeof route.query.beta != "undefined");
</script>
<template>
  <main class="dark:bg-neutral-800">
    <section
      class="bg-gradient-to-b from-fp-newblue-300/75 to-white px-2 pb-12 text-center dark:bg-none lg:text-start"
    >
      <ClientOnly>
        <TheLocalBar
          :image="{
            light: `assets/images/labs/labs-logo-light.png`,
            dark: `assets/images/labs/labs-logo-dark.png`,
          }"
          :home="`/labs/${beta ? '?beta=true' : ''}`"
          textColor="text-fp-newblue"
        />
        <template #fallback>
          <TheLocalBar
            :image="{
              light: `assets/images/labs/labs-logo-light.png`,
              dark: `assets/images/labs/labs-logo-dark.png`,
            }"
            home="/labs/"
            textColor="text-fp-newblue"
          />
        </template>
      </ClientOnly>

      <!-- TITLE -->

      <div class="container mx-auto max-w-7xl px-2 pt-12">
        <h1 class="text-4xl text-gray-600 dark:text-gray-200">
          {{ $t("What is Fedora Labs?") }}
        </h1>
        <div class="flex flex-col flex-wrap gap-8 lg:flex-row">
          <p class="mt-8 text-gray-600 dark:text-fp-gray-light">
            {{
              $t(
                "Fedora Labs is a selection of curated bundles of purpose-driven software and content as curated and maintained by members of the Fedora Community. These may be installed as standalone full versions of Fedora or as add-ons to existing Fedora installations.",
              )
            }}
          </p>
          <div
            class="mx-auto flex h-32 w-32 flex-col items-center justify-center rounded-full bg-fp-newblue-500 p-3 text-white dark:bg-fp-newblue-700 md:h-48 md:w-48 md:p-10"
          >
            <p class="font-display text-xs font-semibold md:text-sm">
              {{ beta ? $t("Beta release") : $t("Latest release") }}
            </p>
            <p class="font-display text-6xl font-bold md:text-8xl">
              {{
                beta ? release_data.beta.releasever : release_data.ga.releasever
              }}
            </p>
          </div>
        </div>
      </div>
    </section>

    <section class="space-y-24 py-24">
      <ClientOnly>
        <LabsPreviewSection
          v-for="lab in navigation.downloads.sections.find(
            ({ label }) => label === 'Labs',
          ).links"
          :slug="`${lab.path.split('/')[2]}`"
          :name="lab.label"
          :beta="beta"
        >
          {{ lab.description }}
        </LabsPreviewSection>
        <template #fallback>
          <LabsPreviewSection
            v-for="lab in navigation.downloads.sections.find(
              ({ label }) => label === 'Labs',
            ).links"
            :slug="`${lab.path.split('/')[2]}`"
            :name="lab.label"
            :beta="false"
          >
            {{ lab.description }}
          </LabsPreviewSection>
        </template>
      </ClientOnly>
    </section>
  </main>
</template>

<style></style>
