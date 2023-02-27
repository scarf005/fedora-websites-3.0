<script setup>
const { locale } = useI18n();

const data = await getCMS("editions/workstation/download");
const release_data = await getCMS("release");

const { data: images_data } = await useFetch(
  `https://dl.fedoraproject.org/pub/alt/stage/${release_data._value.ga.releasever}_RC-${release_data._value.ga.rc_version}/metadata/images.json`
);

// TODO: Fetch BETA metadata is beta toggle is enabled
const { data: beta_data } = await useFetch(
  `https://dl.fedoraproject.org/pub/alt/stage/${release_data._value.beta.releasever}_Beta-${release_data._value.beta.rc_version}/metadata/images.json`
);

const betaSwitch = useState("betaSwitch", () => false);
function toggleBetaSwitch() {
  this.betaSwitch = !this.betaSwitch;
}

const verifyModal = useState("verifyModal", () => ({ show: false }));

const dlpath = {
  x86_64: "https://download.fedoraproject.org/pub/fedora/linux/releases",
  aarch64: "https://download.fedoraproject.org/pub/fedora/linux/releases",
  s390x: "https://download.fedoraproject.org/pub/fedora-secondary/releases",
  ppc64le: "https://download.fedoraproject.org/pub/fedora-secondary/releases",
};

function updateVerify(art) {
  console.log(art);
  verifyModal.value.art_name = art.path.substring(
    art.path.lastIndexOf("/") + 1
  );
  let path = art.path.substring(0, art.path.lastIndexOf("/"));
  verifyModal.value.chk_name = `Fedora-Workstation-${release_data._value.ga.releasever}-${release_data._value.ga.rc_version}-${art.arch}-CHECKSUM`;
  // Fedora-Workstation-37-1.7-x86_64-CHECKSUM
  verifyModal.value.checksum = `${dlpath[art.arch]}/${
    release_data._value.ga.releasever
  }/${path}/${verifyModal.value.chk_name}`;
  if (document) {
    document.body.classList.add("has-modal");
  }
  verifyModal.value.show = true;
}

function closeVerify() {
  if (document) {
    document.body.classList.remove("has-modal");
  }
  verifyModal.value.show = false;
}

useContentHead(data);
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
      <div
        class="container mx-auto flex max-w-7xl justify-end"
        v-if="release_data.beta.enabled"
      >
        <p class="mr-3 text-fp-gray">Show Beta Downloads</p>
        <div>
          <FpSwitch @switchToggled="toggleBetaSwitch()" />
        </div>
      </div>

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
          <div v-if="betaSwitch == false">
            <DownloadSection
              name="For Intel and AMD x86_64 systems"
              art_name="Fedora Workstation"
              @verify-click="updateVerify"
              :artifacts="images_data.payload.images.Workstation.x86_64"
              :dlPrefix="dlpath.x86_64"
              :version="release_data.ga.releasever"
              class="workstation-theme"
            />
            <DownloadSection
              name="For ARM® aarch64 systems"
              art_name="Fedora Workstation"
              @verify-click="updateVerify"
              :artifacts="images_data.payload.images.Workstation.aarch64"
              :dlPrefix="dlpath.aarch64"
              :version="release_data.ga.releasever"
              class="workstation-theme"
            />
            <DownloadSection
              name="For Power ppc64le systems"
              art_name="Fedora Workstation"
              @verify-click="updateVerify"
              :artifacts="images_data.payload.images.Workstation.ppc64le"
              :dlPrefix="dlpath.ppc64le"
              :version="release_data.ga.releasever"
              class="workstation-theme"
            />
          </div>
          <!-- Beta Releases -->
          <div v-else>
            <DownloadSection
              name="For Intel and AMD x86_64 systems"
              art_name="Fedora Workstation"
              @verify-click="updateVerify"
              :artifacts="images_data.payload.images.Workstation.x86_64"
              :dlPrefix="dlpath.x86_64"
              :version="release_data.beta.releasever"
              isBeta
              class="workstation-theme"
            />
            <DownloadSection
              name="For ARM® aarch64 systems"
              art_name="Fedora Workstation"
              @verify-click="updateVerify"
              :artifacts="images_data.payload.images.Workstation.aarch64"
              :dlPrefix="dlpath.aarch64"
              :version="release_data.beta.releasever"
              isBeta
              class="workstation-theme"
            />
            <DownloadSection
              name="For Power ppc64le systems"
              art_name="Fedora Workstation"
              @verify-click="updateVerify"
              :artifacts="images_data.payload.images.Workstation.ppc64le"
              :dlPrefix="dlpath.ppc64le"
              :version="release_data.beta.releasever"
              isBeta
              class="workstation-theme"
            />
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

    <!-- Verify pop up -->
    <Transition
      enter-active-class="transform duration-200 ease-out"
      enter-from-class="opacity-0"
      enter-to-class="opacity-30"
      leave-active-class="transform duration-200 ease-out"
      leave-from-class="opacity-100"
      leave-to-class="opacity-0"
    >
      <FpModal class="pt-12" v-if="verifyModal.show" @close-modal="closeVerify">
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
              class="mb-1 bg-slate-100 px-4 text-sm text-gray-800 dark:bg-slate-800 dark:text-gray-300"
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
              class="mb-4 bg-slate-100 px-4 text-sm text-gray-800 dark:bg-slate-800 dark:text-gray-300"
            ><code>gpgv --keyring ./fedora.gpg {{ verifyModal.chk_name }}</code></pre>
          </li>
          <li>
            <p class="mb-2">{{ $t("Verify the checksum matches") }}</p>
            <pre
              class="mb-4 bg-slate-100 px-4 text-sm text-gray-800 dark:bg-slate-800 dark:text-gray-300"
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
.workstation-theme .fp-download-item a,
.workstation-theme .fp-beta-download-item a {
  @apply border-fp-newblue text-fp-newblue hover:bg-fp-newblue hover:text-white;
}
</style>
