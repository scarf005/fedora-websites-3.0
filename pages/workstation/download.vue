<script setup>
const { locale } = useI18n();

const data = await getCMS("editions/workstation/download");
const release_data = await getCMS("release");
const arches = release_data._value.ga.workstation;
const betaArches = release_data._value.beta.workstation;
useContentHead(data);

function evalLink(uri, release) {
  uri = uri
    .replaceAll("{releasever}", release.releasever)
    .replaceAll("{rc_version}", release.rc_version);
  return `${release_data._value.download_baseurl}${uri}`;
}
</script>

<template>
  <main
    class="border-t-8 border-fp-green dark:border-fp-green-700 dark:bg-neutral-800 md:mt-2"
  >
    <TheLocalBar
      :image="{
        light: 'assets/images/fedora-workstation-logo-light.png',
        dark: 'assets/images/fedora-workstation-logo.png',
      }"
      home="/workstation"
      textColor="text-fp-green-700"
      :items="[
        { name: 'Download', link: '/workstation/download' },
        { name: 'Community', link: '/workstation/community' },
      ]"
    />

    <!-- TITLE -->
    <section class="px-2 pt-24 pb-12 text-center lg:text-start">
      <div class="container mx-auto max-w-7xl px-2">
        <h1 class="mb-4 text-4xl text-gray-600 dark:text-gray-200">
          {{ $t("Download") }}
          <span class="text-fp-green-700">
            Fedora Workstation {{ release_data.ga.releasever }}
          </span>
        </h1>
        <p class="text-gray-600 dark:text-fp-gray-light">
          {{ $t(data.description) }}
        </p>
        <div class="mt-5 flex">
          <p class="mr-5 text-gray-600 dark:text-fp-gray-light">
            <span class="text-sm">{{
              $t(data.sections[0].content[0].title)
            }}</span>
            {{ $t(data.sections[0].content[0].description) }}
          </p>
          <p class="text-gray-600 dark:text-fp-gray-light">
            <span class="text-sm">{{
              $t(data.sections[0].content[1].title)
            }}</span>
            {{ $t(data.sections[0].content[1].description) }}
          </p>
        </div>
        <div class="mt-5 -ml-5 flex" id="ctas">
          <FpLink
            :href="data.sections[0].content[2].link.url"
            class="mx-5 text-blue-500"
          >
            <Icon name="fa-book" />
            {{ $t(data.sections[0].content[2].title) }}
          </FpLink>
          <FpLink
            :href="data.sections[0].content[3].link.url"
            class="mx-5 text-blue-500"
          >
            <Icon name="fa-book" />
            {{ $t(data.sections[0].content[3].title) }}
          </FpLink>
          <FpLink
            :href="data.sections[0].content[4].link.url"
            class="mx-5 text-blue-500"
          >
            <Icon name="fa-book" />
            {{ $t(data.sections[0].content[4].title) }}
          </FpLink>
        </div>
      </div>
    </section>

    <!-- FEDORA MEDIA WRITER DOWNLOAD -->
    <section
      class="bg-gradient-to-r from-green-50 to-blue-50 py-6 px-2 dark:bg-neutral-800 dark:bg-none"
    >
      <div class="container mx-auto grid max-w-7xl grid-cols-2">
        <div class="col-span-2 p-5 md:col-span-1">
          <div class="flex">
            <div>
              <FpImage :src="data.sections[1].images" />
            </div>
            <div>
              <h2 class="text-fp-blue">
                {{ $t(data.sections[1].sectionTitle) }}
              </h2>
              <p class="mb-10 text-fp-gray">
                {{ $t(data.sections[1].sectionDescription) }}
              </p>
            </div>
          </div>
          <div
            class="flex items-center justify-between rounded-xl border border-gray-200 bg-white px-5 py-2 dark:bg-gray-900"
          >
            <p>Fedora Media Writer</p>
            <div class="flex">
              <FpLink
                :href="item.link.url"
                v-for="item in data.sections[1].content"
                class="mx-1 rounded-xl border border-blue-400 py-2 px-4 text-blue-400"
              >
                <Icon :name="item.link.text" />
              </FpLink>
            </div>
          </div>
        </div>

        <!-- DESKTOP IMAGES -->
        <div class="col-span-2 p-5 md:col-span-1">
          <h2 class="text-fp-blue">
            {{ $t(data.sections[2].sectionTitle) }}
          </h2>
          <p class="mb-10 text-fp-gray">
            {{ $t(data.sections[2].sectionDescription) }}
          </p>
          <div v-for="(arch, i) in arches">
            <p class="mt-10 font-bold">{{ $t(arch.title) }}</p>

            <div
              class="mb-2 flex items-center justify-between rounded-xl border border-gray-200 bg-white px-5 py-2 dark:bg-gray-900"
              v-for="item in arch.items"
            >
              <p>
                <span class="mr-5 font-semibold text-gray-800">
                  Fedora Linux {{ release_data.ga.releasever }} </span
                ><span class="text-gray-500"> {{ $t(item.name) }}</span>
              </p>
              <FpLink
                :href="evalLink(item.uri, release_data.ga)"
                class="rounded-xl border border-blue-400 py-2 px-4 text-blue-400"
              >
                <Icon name="fa-download" />
              </FpLink>
            </div>

            <div
              class="mb-2 flex items-center justify-between rounded-xl border border-gray-200 bg-blue-50 px-5 py-2 dark:bg-gray-800"
              v-for="item in betaArches[i].items"
              v-if="release_data.beta.enabled"
            >
              <p>
                <span class="mr-5 font-semibold text-gray-800">
                  Fedora Linux {{ release_data.beta.releasever }} </span
                ><span class="text-gray-500"> {{ $t(item.name) }}</span>
                <span
                  class="ml-4 rounded-full bg-gray-300 px-2 text-sm font-bold text-white dark:bg-gray-700"
                  >{{ $t("BETA") }}</span
                >
              </p>
              <FpLink
                :href="evalLink(item.uri, release_data.beta)"
                class="rounded-xl border border-blue-400 p-2 px-4 text-blue-400"
              >
                <Icon name="fa-download" />
              </FpLink>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- SECURITY -->
    <section class="bg-white py-24 px-4 dark:bg-neutral-900">
      <div class="container mx-auto grid max-w-7xl grid-cols-2">
        <div class="col-span-2 my-5 p-2 md:col-span-1">
          <h2 class="mb-5 text-fp-blue">
            {{ $t(data.sections[3].content[0].title) }}
          </h2>
          <p class="mb-5 text-fp-gray">
            {{ $t(data.sections[3].content[0].description) }}
          </p>
          <FpLink
            class="text-fp-blue"
            :href="data.sections[3].content[0].link.url"
            >{{ $t(data.sections[3].content[0].link.text) }}</FpLink
          >
        </div>
        <div class="col-span-2 my-5 p-2 md:col-span-1">
          <h2 class="mb-5 text-fp-blue">
            {{ $t(data.sections[3].content[1].title) }}
          </h2>
          <p class="mb-5 text-fp-gray">
            {{ $t(data.sections[3].content[1].description) }}
          </p>
          <div
            class="flex items-center justify-between rounded-xl border border-gray-200 bg-white px-5 py-2 dark:bg-gray-900"
          >
            <p>
              {{ $t(data.sections[3].content[1].link.text) }}
            </p>
            <FpLink
              :href="data.sections[3].content[1].link.url"
              class="rounded-xl border border-blue-400 py-2 px-4 text-blue-400"
            >
              <Icon name="fa-download" />
            </FpLink>
          </div>
        </div>
      </div>
    </section>

    <!-- LAPTOPS PRELOADED -->
    <section class="bg-blue-50 py-24 px-4 dark:bg-neutral-800">
      <div class="container mx-auto grid max-w-7xl grid-cols-2">
        <div
          class="col-span-2 my-5 flex items-center justify-center p-2 md:col-span-1"
        >
          <FpImage class="max-h-72" :src="data.sections[4].content[0].image" />
        </div>
        <div class="col-span-2 my-5 p-2 md:col-span-1">
          <h2 class="mb-5 text-fp-blue">
            {{ $t(data.sections[4].sectionTitle) }}
          </h2>
          <p class="mb-5 text-fp-gray">
            {{ $t(data.sections[4].sectionDescription) }}
          </p>
          <FpBtn :href="data.sections[4].content[0].link.url">{{
            $t(data.sections[4].content[0].link.text)
          }}</FpBtn>
        </div>
      </div>
    </section>

    <!-- LEARN MORE ABOUT FEDORA MEDIA WRITER -->
    <section class="py-24 px-4 dark:bg-neutral-900">
      <div class="container mx-auto grid max-w-7xl grid-cols-2">
        <div class="col-span-2 my-5 p-2 md:col-span-1">
          <h2 class="mb-5 text-fp-blue">
            {{ $t(data.sections[5].sectionTitle) }}
          </h2>
          <p class="text-base text-fp-gray">
            {{ $t(data.sections[5].content[0].description) }}
          </p>
          <p class="mt-5 text-sm text-gray-300">
            {{ $t(data.sections[5].content[1].description) }}
          </p>
        </div>
        <div
          class="col-span-2 my-5 flex items-center justify-center p-2 md:col-span-1"
        >
          <FpImage class="max-h-72" :src="data.sections[5].content[1].image" />
        </div>
      </div>
    </section>

    <!-- CONTRIBUTE -->
    <section class="bg-gray-50 py-12 px-4 dark:bg-neutral-800">
      <BecomeContributorSection />
    </section>

    <!-- COMPLIANCE -->
    <section class="py-12 px-4 dark:bg-black">
      <DownloadComplianceSection />
    </section>
  </main>
</template>
