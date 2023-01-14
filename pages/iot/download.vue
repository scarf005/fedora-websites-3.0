<script setup>
const data = await getCMS("editions/iot/download");
const release_data = await getCMS("release");
// TODO: fallback to n-1 version if metadata are not yet available
const { data: images_data } = await useFetch(
  `https://dl.fedoraproject.org/pub/alt/iot/${release_data._value.ga.releasever}/metadata/images.json`
);
// TODO: Fetch BETA metadata is beta toggle is enabled
const verifyModal = useState("verifyModal", () => ({ show: false }));

const releaseDate =
  images_data._value.payload.compose.date.substr(0, 4) +
  "-" +
  images_data._value.payload.compose.date.substr(4, 2) +
  "-" +
  images_data._value.payload.compose.date.substr(6, 2);

function updateVerify(art) {
  console.log(art);
  verifyModal.value.art_name = art.path.substring(
    art.path.lastIndexOf("/") + 1
  );
  let path = art.path.substring(0, art.path.lastIndexOf("/"));
  verifyModal.value.chk_name = `Fedora-IoT-${release_data._value.ga.releasever}-${art.arch}-${images_data._value.payload.compose.date}.${images_data._value.payload.compose.respin}-CHECKSUM`;
  verifyModal.value.checksum = `https://download.fedoraproject.org/pub/alt/iot/${release_data._value.ga.releasever}/${path}/${verifyModal.value.chk_name}`;
  verifyModal.value.show = true;
}

useContentHead(data);
</script>
<template>
  <main class="border-t-8 border-fp-purple md:mt-2">
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

    <!-- TITLE -->
    <section class="py-24 text-center lg:text-start">
      <div class="container mx-auto max-w-7xl">
        <h1 class="mb-4 text-4xl text-fp-gray">
          {{ $t("Download") }}
          <span class="text-fp-purple">
            Fedora IoT {{ release_data.ga.releasever }}</span
          >
        </h1>
        <p class="text-fp-gray dark:text-fp-gray-light">
          {{ $t(data.description) }}
        </p>
        <div class="mt-5 flex">
          <p class="mr-5 text-sm text-fp-gray">
            {{ $t("Latest release:") }}
            <span class="font-semibold">{{ releaseDate }}</span>
          </p>
        </div>
      </div>
    </section>

    <!-- DOWNLOAD ARTIFACTS -->
    <section
      class="scroll-mt-14 bg-gradient-to-r from-purple-50 to-blue-50 py-6 dark:bg-neutral-800 dark:bg-none"
      id="download_section"
    >
      <div class="container mx-auto mb-8 max-w-7xl">
        <div class="mb-6 text-center lg:text-start">
          <h2 class="mb-4 text-fp-blue">
            {{ $t("") }}
          </h2>
        </div>
        <div
          class="container mx-auto grid max-w-7xl grid-flow-row grid-flow-dense auto-rows-max grid-cols-1 gap-8 md:grid-cols-2"
        >
          <IotDownloadSection
            name="For Intel and AMD x86_64 systems"
            @verify-click="updateVerify"
            :artifacts="images_data.payload.images.IoT.x86_64"
            :version="release_data.ga.releasever"
            class="iot-theme"
          />
          <IotDownloadSection
            name="For ARM® aarch64 systems"
            @verify-click="updateVerify"
            :artifacts="images_data.payload.images.IoT.aarch64"
            :version="release_data.ga.releasever"
            class="iot-theme"
          />
        </div>
      </div>
    </section>

    <section class="bg-white py-8 dark:bg-neutral-900">
      <CoreOsVerifySection />
    </section>

    <section class="bg-blue-50 py-12 dark:bg-neutral-800">
      <BecomeContributorSection />
    </section>

    <section class="py-12 dark:bg-black">
      <DownloadComplianceSection />
    </section>

    <Transition
      enter-active-class="transform duration-200 ease-out"
      enter-from-class="opacity-0"
      enter-to-class="opacity-30"
      leave-active-class="transform duration-200 ease-out"
      leave-from-class="opacity-100"
      leave-to-class="opacity-0"
    >
      <FpModal
        class="pt-12"
        v-if="verifyModal.show"
        @close-modal="verifyModal.show = false"
      >
        <template #header>
          <h5 class="text-xl font-medium">{{ $t("Verify your download") }}</h5>
        </template>
        <p class="text-base">
          {{
            $t(
              "Verify your download for security and integrity using the proper checksum file. If there is a good signature from one of the Fedora keys, and the SHA256 checksum matches, then the download is valid."
            )
          }}
        </p>
        <ul class="list-outside list-decimal pl-8 pt-2">
          <li>
            <p class="mb-2">
              Download the
              <a
                class="text-fp-blue"
                :href="verifyModal.checksum"
                target="_blank"
                >checksum file</a
              >
              into the same directory as the image you downloaded.
            </p>
          </li>
          <li>
            <p class="mb-2">{{ $t("Import Fedora's GPG key(s)") }}</p>
            <pre
              class="mb-1 bg-slate-100 px-4 text-sm text-gray-800"
            ><code>curl -O https://getfedora.org/static/fedora.gpg</code></pre>
            <p class="mb-4 text-sm">
              <Icon name="fa-solid:info-circle" class="mx-2 !align-sub" />

              {{ $t("You can verify the details of the GPG key(s)") }}
              <FpLink class="text-sm text-fp-blue" href="/security">here</FpLink
              >.
            </p>
          </li>
          <li>
            <p class="mb-2">{{ $t("Verify the checksum file is valid") }}</p>
            <pre
              class="mb-4 bg-slate-100 px-4 text-sm text-gray-800"
            ><code>gpgv --keyring ./fedora.gpg {{ verifyModal.chk_name }}</code></pre>
          </li>
          <li>
            <p class="mb-2">{{ $t("Verify the checksum matches") }}</p>
            <pre
              class="mb-4 bg-slate-100 px-4 text-sm text-gray-800"
            ><code>sha256sum -c {{ verifyModal.chk_name }}</code></pre>
          </li>
        </ul>
        <p>
          {{
            $t(
              "If the output states that the file is valid, then it's ready to use!"
            )
          }}
        </p>
      </FpModal>
    </Transition>
  </main>
</template>

<style>
.iot-theme .fp-download-item a {
  @apply border-purple-500 text-purple-500 hover:bg-purple-500 hover:text-white;
}
</style>
