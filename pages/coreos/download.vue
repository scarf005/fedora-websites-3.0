<script setup>
const data = await getCMS("editions/coreos/download");
const { data: stable_data } = await useFetch(
  "https://builds.coreos.fedoraproject.org/streams/stable.json"
);
const { data: test_data } = await useFetch(
  "https://builds.coreos.fedoraproject.org/streams/testing.json"
);
const { data: next_data } = await useFetch(
  "https://builds.coreos.fedoraproject.org/streams/next.json"
);

let selectedStream = useState("stream", () => stable_data);
let selectedArch = useState("arch", () => "x86_64");
const verifyModal = useState("verifyModal", () => ({ show: false }));
const showAMI = useState("showAMI", () => ({ show: false }));
const streams = data._value.sections[0];
const architectures = data._value.sections[1];

function switchStream(name) {
  switch (name) {
    case "stable":
      selectedStream.value = stable_data;
      break;
    case "test":
      selectedStream.value = test_data;
      break;
    case "next":
      selectedStream.value = next_data;
      break;
  }
}

function updateVerify(art) {
  verifyModal.value.art_name = art.location.substring(
    art.location.lastIndexOf("/") + 1
  );
  verifyModal.value.signature = art.signature;
  verifyModal.value.checksum = `data:text/plain;charset=utf-8,SHA256 (${encodeURIComponent(
    verifyModal.value.art_name
  )}) = ${art.sha256}`;
  verifyModal.value.sig_name = art.signature.substring(
    art.signature.lastIndexOf("/") + 1
  );
  verifyModal.value.chk_name = `${verifyModal.value.art_name}-CHECKSUM`;
  if (document) {
    document.body.classList.add("has-modal");
  }
  verifyModal.value.show = true;
}

function updateAMIs(art) {
  showAMI.value.art = art;
  if (document) {
    document.body.classList.add("has-modal");
  }
  showAMI.value.show = true;
}

function closeModal(state) {
  if (document) {
    document.body.classList.remove("has-modal");
  }
  state.show = false;
}

function virt_arts(data) {
  let dict = {};
  const virtualizedImages = ["qemu", "virtualbox", "vmware"];
  if (data) {
    for (let k of virtualizedImages) {
      dict[k] = data[k];
    }
  }
  return dict;
}

function cloud_arts(data) {
  let dict = {};
  const cloudImages = [
    "aws",
    "azure",
    "azurestack",
    "aliyun",
    "digitalocean",
    "exoscale",
    "gcp",
    "ibmcloud",
    "nutanix",
    "openstack",
    "packet",
    "vultr",
  ];
  if (data) {
    for (let k of cloudImages) {
      dict[k] = data[k];
    }
  }
  return dict;
}

function getMajor(version) {
  return version.split(".")[0];
}

const EC2_regions = {
  "us-east-2": "US East (Ohio)",
  "us-east-1": "US East (N. Virginia)",
  "us-west-1": "US West (N. California)",
  "us-west-2": "US West (Oregon)",
  "af-south-1": "Africa (Cape Town)",
  "ap-east-1": "Asia Pacific (Hong Kong)",
  "ap-south-2": "Asia Pacific (Hyderabad)",
  "ap-southeast-3": "Asia Pacific (Jakarta)",
  "ap-south-1": "Asia Pacific (Mumbai)",
  "ap-northeast-3": "Asia Pacific (Osaka)",
  "ap-northeast-2": "Asia Pacific (Seoul)",
  "ap-southeast-1": "Asia Pacific (Singapore)",
  "ap-southeast-2": "Asia Pacific (Sydney)",
  "ap-northeast-1": "Asia Pacific (Tokyo)",
  "ca-central-1": "Canada (Central)",
  "eu-central-1": "Europe (Frankfurt)",
  "eu-west-1": "Europe (Ireland)",
  "eu-west-2": "Europe (London)",
  "eu-south-1": "Europe (Milan)",
  "eu-west-3": "Europe (Paris)",
  "eu-south-2": "Europe (Spain)",
  "eu-north-1": "Europe (Stockholm)",
  "eu-central-2": "Europe (Zurich)",
  "me-south-1": "Middle East (Bahrain)",
  "me-central-1": "Middle East (UAE)",
  "sa-east-1": "South America (São Paulo)",
};

useHead({ htmlAttrs: { class: "scroll-smooth" } });
useContentHead(data);
</script>
<template>
  <main
    class="border-t-8 border-fp-magenta md:mt-2"
    :class="`coreos-theme-${selectedStream.stream}`"
  >
    <TheLocalBar
      image="assets/images/fedora-coreos-logo.png"
      home="/coreos"
      textColor="text-fp-magenta"
      :items="[
        { name: 'Download', link: '/coreos/download' },
        { name: 'Community', link: '/coreos/community' },
      ]"
    />

    <!-- TITLE -->
    <section class="py-24 text-center lg:text-start">
      <div class="container mx-auto max-w-7xl">
        <h1 class="mb-4 text-4xl text-fp-gray">
          {{ $t("Download") }}
          <span class="text-fp-magenta"> Fedora CoreOS </span>
        </h1>
        <p class="text-fp-gray dark:text-fp-gray-light">
          {{ $t(streams.sectionDescription) }}
        </p>

        <!-- STREAMS -->
        <div
          class="container mx-auto mt-8 grid grid-cols-1 gap-4 lg:grid-cols-3"
        >
          <!-- Stable -->
          <CoreOsStream
            name="Stable"
            :version="stable_data.architectures.x86_64.artifacts.metal.release"
            :last_update="stable_data.metadata['last-modified']"
            icon="fa-solid:shield-alt"
            color="fp-blue"
          >
            {{ $t(streams.content[0].description) }}
            <template #footer>
              <a
                id="stable"
                @click="switchStream('stable')"
                href="#arches"
                class="mx-auto mb-4 rounded-sm bg-fp-blue py-1 px-3 text-sm font-bold text-white"
                >Show Downloads</a
              >
            </template>
          </CoreOsStream>
          <CoreOsStream
            name="Testing"
            :version="test_data.architectures.x86_64.artifacts.metal.release"
            :last_update="test_data.metadata['last-modified']"
            icon="fa-solid:flask"
            color="fp-green"
          >
            {{ $t(streams.content[1].description) }}
            <template #footer>
              <a
                id="test"
                @click="switchStream('test')"
                href="#arches"
                class="mx-auto mb-4 rounded-sm bg-fp-green py-1 px-3 text-sm font-bold text-white"
                >Show Downloads</a
              >
            </template>
          </CoreOsStream>
          <!-- Next border-fp-orange bg-fp-orange -->
          <CoreOsStream
            name="Next"
            :version="next_data.architectures.x86_64.artifacts.metal.release"
            :last_update="next_data.metadata['last-modified']"
            icon="fa-solid:layer-group"
            color="fp-orange"
          >
            {{ $t(streams.content[2].description) }}
            <template #footer>
              <a
                id="next"
                @click="switchStream('next')"
                href="#arches"
                class="mx-auto mb-4 rounded-sm bg-fp-orange py-1 px-3 text-sm font-bold text-white"
                >Show Downloads</a
              >
            </template>
          </CoreOsStream>
        </div>
      </div>
    </section>

    <!-- ARCH SELECTOR -->
    <section
      class="scroll-mt-14 bg-blue-50 py-6 dark:bg-neutral-900"
      id="arches"
    >
      <div class="container mx-auto max-w-7xl">
        <div class="text-center lg:text-start">
          <h2 class="mb-4 text-fp-blue">
            {{ $t("Pick your") }}
            <span class="text-fp-magenta">{{ $t("architecture") }} </span>
          </h2>
          <p class="text-fp-gray dark:text-fp-gray-light">
            {{ $t(architectures.sectionDescription) }}
          </p>
        </div>
        <div class="mx-auto p-5">
          <div
            class="flex flex-wrap justify-between gap-4 text-center text-fp-blue-dark dark:text-white"
          >
            <a
              @click="selectedArch = 'x86_64'"
              href="#download_section"
              class="grow basis-64 rounded-xl p-2 transition-colors hover:bg-slate-50 dark:hover:bg-slate-800"
            >
              <FpCard
                title="x86_64"
                :description="architectures.content[0].description"
                class="coreos-theme"
              >
              </FpCard>
            </a>
            <a
              @click="selectedArch = 'aarch64'"
              href="#download_section"
              class="grow basis-64 rounded-xl p-2 transition-colors hover:bg-slate-50 dark:hover:bg-slate-800"
            >
              <FpCard
                title="aarch64"
                :description="architectures.content[1].description"
                class="coreos-theme"
              >
              </FpCard>
            </a>
            <a
              @click="selectedArch = 's390x'"
              href="#download_section"
              class="grow basis-64 rounded-xl p-2 transition-colors hover:bg-slate-50 dark:hover:bg-slate-800"
            >
              <FpCard
                title="s390x"
                :description="architectures.content[2].description"
                class="coreos-theme"
              >
              </FpCard>
            </a>
          </div>
        </div>
      </div>
    </section>

    <!-- DOWNLOAD ARTIFACTS -->
    <section
      class="scroll-mt-14 bg-gradient-to-r from-pink-50 to-blue-50 py-6 dark:bg-neutral-800 dark:bg-none"
      id="download_section"
    >
      <div class="container mx-auto mb-8 max-w-7xl">
        <div class="mb-6 text-center lg:text-start">
          <h2 class="mb-4 text-fp-blue">
            <Icon
              name="fa-solid:server"
              size="24"
              class="!align-baseline text-black dark:text-white"
            />
            {{ $t("Bare Metal & Virtualized") }}
          </h2>
          <p class="text-fp-gray dark:text-fp-gray-light">
            Download Fedora CoreOS
            <span class="coreos-theme-text font-bold">{{
              selectedStream.stream
            }}</span>
            artifacts for
            <span class="font-bold">{{ selectedArch }}</span
            >.
          </p>
        </div>
        <div
          class="container mx-auto grid max-w-7xl grid-flow-row grid-flow-dense auto-rows-max grid-cols-1 gap-8 md:grid-cols-2"
        >
          <CoreOsDownloadSection
            name="Bare Metal"
            class="coreos-theme row-span-3"
            @verify-click="updateVerify"
            :artifacts="{
              metal: selectedStream.architectures[selectedArch].artifacts.metal,
            }"
          />
          <CoreOsDownloadSection
            name="Virtualized"
            class="coreos-theme"
            @verify-click="updateVerify"
            :artifacts="
              virt_arts(selectedStream.architectures[selectedArch].artifacts)
            "
          />
        </div>
      </div>

      <div class="container mx-auto mb-8 max-w-7xl">
        <div class="mb-6 text-center lg:text-start">
          <h2 class="mb-4 text-fp-blue">
            <Icon
              name="fa-solid:cloud"
              size="24"
              class="!align-baseline text-black dark:text-white"
            />
            {{ $t("Cloud Images") }}
          </h2>
          <p class="text-fp-gray dark:text-fp-gray-light">
            Download Fedora CoreOS
            <span class="coreos-theme-text font-bold">{{
              selectedStream.stream
            }}</span>
            cloud images for
            <span class="font-bold">{{ selectedArch }}</span
            >.
          </p>
        </div>
        <div
          class="container mx-auto grid max-w-7xl grid-flow-row grid-flow-dense auto-rows-max grid-cols-1 gap-8 md:grid-cols-2"
        >
          <CoreOsDownloadSection
            :artifacts="
              cloud_arts(selectedStream.architectures[selectedArch].artifacts)
            "
            name="Cloud Operators"
            @verify-click="updateVerify"
            class="coreos-theme"
          />
          <!-- AMIs & GCP -->
          <div
            class="coreos-theme"
            v-if="
              Object.keys(selectedStream.architectures[selectedArch].images)
                .length > 0
            "
          >
            <p class="my-2 font-bold">{{ $t("Cloud Launchable") }}</p>

            <div class="download-section mb-2">
              <FpDownloadItem
                :name="`Fedora CoreOS ${getMajor(
                  Object.values(
                    selectedStream.architectures[selectedArch].images.aws
                      .regions
                  )[0].release
                )}`"
                type="aws"
                v-if="selectedStream.architectures[selectedArch].images.aws"
              >
                <template #btn>
                  <a
                    title="Launch"
                    class="rounded-xl"
                    @click="
                      updateAMIs(
                        selectedStream.architectures[selectedArch].images.aws
                      )
                    "
                  >
                    <Icon
                      name="material-symbols:rocket-launch"
                      class="!align-baseline"
                    />
                  </a>
                </template>
              </FpDownloadItem>
            </div>
            <div class="download-section mb-2">
              <FpDownloadItem
                :name="`Fedora CoreOS ${getMajor(
                  selectedStream.architectures[selectedArch].images.gcp.release
                )}`"
                type="gcp"
                v-if="selectedStream.architectures[selectedArch].images.gcp"
              >
                <template
                  #btn
                  v-for="art in [
                    selectedStream.architectures[selectedArch].images.gcp,
                  ]"
                >
                  <FpLink
                    :href="`https://console.cloud.google.com/marketplace/details/${art.project}/${art.family}`"
                    target="blank"
                    title="Launch"
                    class="rounded-xl"
                  >
                    <Icon
                      name="material-symbols:rocket-launch"
                      class="!align-baseline"
                    />
                  </FpLink>
                </template>
              </FpDownloadItem>
            </div>
          </div>
        </div>
      </div>
      <a href="#"><p class="mr-4 text-end text-xs">Back to Top</p></a>
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
        @close-modal="closeModal(verifyModal)"
      >
        <template #header>
          <h5 class="text-xl font-medium">{{ $t("Verify your download") }}</h5>
        </template>
        <p class="text-base">
          {{
            $t(
              "Verify your download for security and integrity using the proper checksum and signature file. If there is a good signature from one of the Fedora keys, and the SHA256 checksum matches, then the download is valid."
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
                :download="verifyModal.chk_name"
                >checksum file</a
              >
              and
              <a class="text-fp-blue" :href="verifyModal.signature"
                >signature</a
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
            <p class="mb-2">{{ $t("Verify the signature file is valid") }}</p>
            <pre
              class="mb-4 bg-slate-100 px-4 text-sm text-gray-800 dark:bg-slate-800 dark:text-gray-300"
            ><code>gpgv --keyring ./fedora.gpg {{ verifyModal.sig_name }} {{ verifyModal.art_name }}</code></pre>
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
        v-if="showAMI.show"
        @close-modal="closeModal(showAMI)"
      >
        <template #header>
          <h5 class="text-xl font-medium">Select AWS EC2 region</h5>
        </template>
        <table class="w-full table-auto">
          <thead>
            <tr>
              <th class="">Region</th>
              <th class="hidden sm:block">AMI ID</th>
              <th class="text-center">Launch instance</th>
            </tr>
          </thead>
          <tbody>
            <tr
              v-for="(ami, region) in showAMI.art.regions"
              class="hover:bg-gray-200 hover:dark:bg-slate-800"
            >
              <td class="pr-6">{{ EC2_regions[region] || region }}</td>
              <td class="hidden pr-6 sm:block">{{ ami.image }}</td>
              <td class="text-center">
                <FpLink
                  :href="`https://console.aws.amazon.com/ec2/home?region=${region}#launchAmi=${ami.image}`"
                  target="blank"
                  :title="`Launch in ${region}`"
                  class="rounded-xl"
                >
                  <Icon
                    name="material-symbols:rocket-launch"
                    class="!align-baseline"
                  />
                </FpLink>
              </td>
            </tr>
          </tbody>
        </table>
      </FpModal>
    </Transition>
  </main>
</template>

<style>
body.has-modal {
  @apply overflow-hidden;
}

.coreos-theme-stable .coreos-theme-text,
.coreos-theme-stable .fp-card.coreos-theme h3 {
  @apply text-fp-blue;
}

.coreos-theme-testing .coreos-theme-text,
.coreos-theme-testing .fp-card.coreos-theme h3 {
  @apply text-fp-green;
}

.coreos-theme-next .coreos-theme-text,
.coreos-theme-next .fp-card.coreos-theme h3 {
  @apply text-fp-orange;
}

.coreos-theme-stable .coreos-theme .fp-download-item a {
  @apply border-blue-500 text-blue-500 hover:bg-blue-500 hover:text-white;
}

.coreos-theme-testing .coreos-theme .fp-download-item a {
  @apply border-fp-green text-fp-green hover:bg-fp-green hover:text-white dark:border-green-600 dark:text-green-600 dark:hover:bg-green-600 dark:hover:text-white;
}

.coreos-theme-next .coreos-theme .fp-download-item a {
  @apply border-fp-orange text-fp-orange hover:bg-fp-orange hover:text-white;
}
</style>
