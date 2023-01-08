<script setup>
const { data } = await useAsyncData("page-data", () => {
  return queryContent("/editions/coreos/download").find();
});
const { data: stable_data } = await useFetch(
  "https://builds.coreos.fedoraproject.org/streams/stable.json"
);
const { data: test_data } = await useFetch(
  "https://builds.coreos.fedoraproject.org/streams/testing.json"
);
const { data: next_data } = await useFetch(
  "https://builds.coreos.fedoraproject.org/streams/next.json"
);
const stream_data = {
  stable: stable_data,
  test: test_data,
  next: next_data,
};
let selectedStream = useState("stream", () => stable_data);
let selectedArch = useState("arch", () => "x86_64");
const color = useState("streamColor", () => ({
  name: "blue",
  text: "text-fp-blue",
}));

function switchStream(name) {
  switch (name) {
    case "stable":
      selectedStream.value = stable_data;
      color.value = { name: "blue", text: "text-fp-blue" };
      break;
    case "test":
      selectedStream.value = test_data;
      color.value = { name: "green", text: "text-fp-green" };
      break;
    case "next":
      selectedStream.value = next_data;
      color.value = { name: "orange", text: "text-fp-orange" };
      break;
  }
  console.log(selectedStream);
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

useHead({ htmlAttrs: { class: "scroll-smooth" } });
</script>
<template>
  <main class="mt-2 border-t-8 border-fp-magenta">
    <TheLocalBar
      image="assets/images/fedora-coreos-logo.png"
      home="/coreos"
      :items="[
        { name: 'Download', link: '/coreos/download' },
        { name: 'Community', link: '/coreos/community' },
        { name: 'Help', link: '/coreos/help' },
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
          {{
            $t("Fedora CoreOS is available across 3 different release streams")
          }}
        </p>

        <!-- STREAMS -->
        <div
          class="container mx-auto mt-8 grid grid-cols-1 gap-4 lg:grid-cols-3"
        >
          <!-- Stable -->
          <FpStream
            name="Stable"
            :version="stable_data.architectures.x86_64.artifacts.metal.release"
            :last_update="stable_data.metadata['last-modified']"
            icon="fa-solid:shield-alt"
            color="fp-blue"
          >
            The Stable stream is the most reliable version of Fedora CoreOS.
            Releases are battle-tested within the Testing stream before being
            promoted.
            <template #footer>
              <a
                id="stable"
                @click="switchStream('stable')"
                href="#arches"
                class="mx-auto mb-4 rounded-sm py-1 px-3 text-sm font-bold text-white"
                :class="`bg-fp-blue`"
                >Show Downloads</a
              >
            </template>
          </FpStream>
          <FpStream
            name="Testing"
            :version="test_data.architectures.x86_64.artifacts.metal.release"
            :last_update="test_data.metadata['last-modified']"
            icon="fa-solid:flask"
            color="fp-green"
          >
            The Testing stream contains the next Stable release. Mix a few
            Testing machines into your cluster to catch any bugs specific to
            your hardware or configuration.
            <template #footer>
              <a
                id="test"
                @click="switchStream('test')"
                href="#arches"
                class="mx-auto mb-4 rounded-sm py-1 px-3 text-sm font-bold text-white"
                :class="`bg-fp-blue`"
                >Show Downloads</a
              >
            </template>
          </FpStream>
          <!-- Next border-fp-orange bg-fp-orange -->
          <FpStream
            name="Next"
            :version="next_data.architectures.x86_64.artifacts.metal.release"
            :last_update="next_data.metadata['last-modified']"
            icon="fa-solid:layer-group"
            color="fp-orange"
          >
            The Next stream represents the future. It provides early access to
            new features and to the next major version of Fedora. Run a few Next
            machines in your cluster, or in staging, to help find problems.
            <template #footer>
              <a
                id="next"
                @click="switchStream('next')"
                href="#arches"
                class="mx-auto mb-4 rounded-sm py-1 px-3 text-sm font-bold text-white"
                :class="`bg-fp-blue`"
                >Show Downloads</a
              >
            </template>
          </FpStream>
        </div>
      </div>
    </section>

    <!-- ARCH SELECTOR -->
    <section
      class="scroll-mt-20 bg-blue-50 py-6 dark:bg-neutral-900"
      id="arches"
    >
      <div class="container mx-auto max-w-7xl">
        <div class="text-center lg:text-start">
          <h2 class="mb-4 text-fp-blue">
            {{ $t("Pick your") }}
            <span class="text-fp-magenta">{{ $t("architecture") }} </span>
          </h2>
          <p class="text-fp-gray dark:text-fp-gray-light">
            {{
              $t(
                "Fedora CoreOS can be deployed on 3 different CPU architecture."
              )
            }}
          </p>
        </div>
        <div class="mx-auto p-5">
          <div
            class="flex flex-wrap justify-between gap-4 text-center text-fp-blue-dark dark:text-white"
          >
            <a
              @click="selectedArch = 'x86_64'"
              href="#download_section"
              class="grow basis-64"
            >
              <FpCard
                title="x86_64"
                description="Most computers with Intel and AMD processors."
              >
              </FpCard>
            </a>
            <a
              @click="selectedArch = 'aarch64'"
              href="#download_section"
              class="grow basis-64"
            >
              <FpCard
                title="aarch64"
                description="Also known as armv8. For most processors other than Intel and AMD like Rasperry Pi or other comparable devices."
              >
              </FpCard>
            </a>
            <a
              @click="selectedArch = 's390x'"
              href="#download_section"
              class="grow basis-64"
            >
              <FpCard title="s390x" description="For IBM Cloud and zSystems">
              </FpCard>
            </a>
          </div>
        </div>
      </div>
    </section>

    <!-- DOWNLOAD ARTIFACTS -->
    <section
      class="scroll-mt-20 bg-gradient-to-r from-pink-50 to-blue-50 py-6 dark:bg-neutral-800 dark:bg-none"
      id="download_section"
    >
      <div class="container mx-auto mb-8 max-w-7xl">
        <div class="text-center lg:text-start">
          <h2 class="mb-4 text-fp-blue">
            <Icon
              name="fa-solid:server"
              size="24"
              class="!align-baseline text-black dark:text-white"
            />
            {{ $t("Bare Metal & Virtualized") }}
          </h2>
          <p class="text-fp-gray dark:text-fp-gray-light">
            Fedora CoreOS
            <span :class="color.text">{{ selectedStream.stream }}</span>
            download artifacts for {{ selectedArch }}.
          </p>
        </div>
        <div
          class="container mx-auto grid max-w-7xl grid-flow-row grid-flow-dense auto-rows-max grid-cols-1 gap-8 md:grid-cols-2"
        >
          <FpDownload
            name="Bare Metal"
            class="row-span-3"
            :theme="color.name"
            :artifacts="{
              metal: selectedStream.architectures[selectedArch].artifacts.metal,
            }"
          />
          <FpDownload
            name="Virtualized"
            :theme="color.name"
            :artifacts="
              virt_arts(selectedStream.architectures[selectedArch].artifacts)
            "
          />
        </div>
      </div>

      <div class="container mx-auto mb-8 max-w-7xl">
        <div class="text-center lg:text-start">
          <h2 class="mb-4 text-fp-blue">
            <Icon
              name="fa-solid:cloud"
              size="24"
              class="!align-baseline text-black dark:text-white"
            />
            {{ $t("Cloud Images") }}
          </h2>
          <p class="text-fp-gray dark:text-fp-gray-light">
            Fedora CoreOS
            <span :class="color.text">{{ selectedStream.stream }}</span>
            download artifacts for {{ selectedArch }}.
          </p>
        </div>
        <div
          class="container mx-auto grid max-w-7xl grid-flow-row grid-flow-dense auto-rows-max grid-cols-1 gap-8 md:grid-cols-2"
        >
          <FpDownload
            :artifacts="
              cloud_arts(selectedStream.architectures[selectedArch].artifacts)
            "
            name="Cloud Operators"
            :theme="color.name"
            class=""
          />
          <!-- TODO: AMIs & GCP -->
          <FpDownload
            :artifacts="{}"
            name="Cloud Launchable"
            :theme="color.name"
            class=""
          />
        </div>
      </div>
    </section>
  </main>
</template>
