<script setup>
const { locale } = useI18n();
const data = await getCMS("editions/coreos/releasenotes");

useContentHead(data);
</script>

<template>
  <main class="border-t-8 border-fp-magenta dark:bg-neutral-800 md:mt-2">
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
    </header>
    <section class="py-12 px-2 text-center lg:text-start">
      <div class="container mx-auto max-w-7xl px-2">
        <h1 class="mb-4 text-4xl text-gray-600 dark:text-gray-200">
          <span class="text-fp-magenta">Fedora CoreOS </span>
          {{ $t("Release Notes") }}
        </h1>
        <p class="text-fp-gray">{{ data.description }}</p>
      </div>
    </section>
    <!-- Mini stream selector -->
    <section class="scroll-mt-14 bg-blue-50 py-2 px-2 dark:bg-neutral-900">
      <div class="container mx-auto max-w-7xl px-2">
        <div class="mx-auto px-24 pb-4">
          <div
            class="coreos-selector flex flex-wrap justify-between gap-4 text-center text-fp-darkblue-500 dark:text-white"
          >
            <a id="stable" class="active" href="#">
              <FpCard title="stable"> </FpCard>
            </a>
            <a id="testing" href="#">
              <FpCard title="testing"> </FpCard>
            </a>
            <a id="next" href="#">
              <FpCard title="next"> </FpCard>
            </a>
          </div>
        </div>
      </div>
    </section>

    <!-- Mini arch selector -->
    <section class="scroll-mt-14 bg-white py-2 px-2 dark:bg-neutral-800">
      <div class="container mx-auto max-w-7xl px-2">
        <div class="mx-auto px-24 pb-4">
          <div
            class="coreos-selector flex flex-wrap justify-between gap-4 text-center text-fp-darkblue-500 dark:text-white"
          >
            <a id="x86_64" class="active" href="#">
              <FpCard title="x86_64"> </FpCard>
            </a>
            <a id="aarch64" href="#">
              <FpCard title="aarch64"> </FpCard>
            </a>
            <a id="s390x" href="#">
              <FpCard title="s390x"> </FpCard>
            </a>
          </div>
        </div>
      </div>
    </section>

    <!-- Release notes -->
    <section
      class="scroll-mt-14 bg-blue-50 py-6 px-2 dark:bg-neutral-900"
    ></section>
  </main>
</template>
<style>
.coreos-selector a {
  @apply grow basis-64 border-b-8 border-fp-blue/10 p-2 transition-colors hover:border-fp-newblue-500 dark:hover:border-gray-200;
}

.coreos-selector .active {
  @apply border-fp-blue dark:border-gray-400;
}
</style>
