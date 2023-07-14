<script setup>
const route = useRoute();
const router = useRouter();
const { locale } = useI18n();
const data = await getCMS("editions/coreos/releasenotes");
const baseProdUrl = "https://builds.coreos.fedoraproject.org";

let selectedStream = useState("stream", () => "stable");
let selectedArch = useState("arch", () => "x86_64");

let buildsList = useState("buildsList", () => ({}));
let buildsDetails = useState("buildsDetails", () => ({}));

const diffType = ["added", "removed", "upgraded", "downgraded"];

const importantPkgs = [
  "kernel",
  "systemd",
  "rpm-ostree",
  "ignition",
  "podman",
  "moby-engine",
  "containerd",
];

async function switchStream(stream) {
  selectedStream.value = stream;
  // Fetch build list & release notes if not yet cached
  if (!buildsList.value[stream]) {
    try {
      const buildUrl = `${baseProdUrl}/prod/streams/${stream}/releases.json`;
      const buildsrq = await $fetch(buildUrl, {
        key: "buildsrq",
        server: false,
        watch: false,
      });
      const notesUrl = `${baseProdUrl}/release-notes/${stream}.json`;
      const notesrq = await $fetch(notesUrl, {
        key: `notesrq-${stream}`,
        server: false,
        watch: false,
      });
      buildsList.value[stream] = {
        builds: buildsrq.releases
          .map((release) => ({
            id: release.version,
            arches: release.commits.map((arch) => arch.architecture),
          }))
          .reverse(),
        releases: notesrq.releases,
      };
    } catch (e) {
      console.log(e);
    }
  }

  // Update URL parameters
  router.replace({
    hash: route.hash,
    path: route.path,
    query: { ...route.query, ...{ stream: stream } },
  });

  // Preload first 3 builds for this stream/arch
  preloadBuild();

  // Update stream selector on DOM
  window.requestAnimationFrame(() => {
    if (document) {
      Array.from(
        document.querySelectorAll(".coreos-stream .coreos-selector a")
      ).forEach(function (el) {
        el.classList.remove("active");
      });
      document.getElementById(stream)?.classList.add("active");
    }
  });
}

function switchArch(arch) {
  selectedArch.value = arch;

  // Update URL parameters
  router.replace({
    hash: route.hash,
    path: route.path,
    query: { ...route.query, ...{ arch: arch } },
  });

  // Preload first 3 builds for this stream/arch
  preloadBuild();

  // Update arch selector on DOM
  window.requestAnimationFrame(() => {
    if (document) {
      Array.from(
        document.querySelectorAll(".coreos-arch .coreos-selector a")
      ).forEach(function (el) {
        el.classList.remove("active");
      });
      document.getElementById(arch)?.classList.add("active");
    }
  });
}

function preloadBuild(nb = 3) {
  if (buildsList.value[selectedStream.value]?.builds) {
    for (var i = 0; i < nb; i++) {
      loadBuild(buildsList.value[selectedStream.value].builds[i].id);
    }
  }
}

async function loadBuild(id) {
  if (!buildsDetails.value[selectedArch.value]) {
    buildsDetails.value[selectedArch.value] = {};
  }
  if (!buildsDetails.value[selectedArch.value][id]) {
    const metaUrl = `${baseProdUrl}/prod/streams/${selectedStream.value}/builds/${id}/${selectedArch.value}/meta.json`;
    const { data: build_data } = await useFetch(metaUrl);
    const commitmetaUrl = `${baseProdUrl}/prod/streams/${selectedStream.value}/builds/${id}/${selectedArch.value}/commitmeta.json`;
    const { data: meta_data } = await useFetch(commitmetaUrl);
    buildsDetails.value[selectedArch.value][id] = {
      meta: build_data.value,
      commitmeta: meta_data.value,
    };
    if (build_data.value) {
      parsePkgs(id);
      if (meta_data.value) parsePkgDiff(id);
    }
  }
}

function parsePkgs(id) {
  if (!buildsDetails.value[selectedArch.value][id]["pkglist"]) {
    buildsDetails.value[selectedArch.value][id]["pkglist"] = [];
    buildsDetails.value[selectedArch.value][id]["commitmeta"][
      "rpmostree.rpmdb.pkglist"
    ].forEach((pkg) => {
      if (importantPkgs.includes(pkg[0])) {
        buildsDetails.value[selectedArch.value][id]["pkglist"].push(pkg);
      }
    });
  }
}

function parsePkgDiff(id) {
  if (!buildsDetails.value[selectedArch.value][id]["pkgdiff"]) {
    var pkgdiff = {};
    diffType.forEach((t) => (pkgdiff[t] = []));
    // parent-pkgdiff key should have all the information we need, we just need to sort by diffType (added/removed/upgraded)
    if (buildsDetails.value[selectedArch.value][id].meta["parent-pkgdiff"]) {
      buildsDetails.value[selectedArch.value][id].meta[
        "parent-pkgdiff"
      ].forEach((d) => pkgdiff[diffType[d[1]]].push(d));
    } else if (buildsDetails.value[selectedArch.value][id].meta["pkgdiff"]) {
      buildsDetails.value[selectedArch.value][id].meta["pkgdiff"].forEach((d) =>
        pkgdiff[diffType[d[1]]].push(d)
      );
    } else {
      // No diff ?!
      console.log(`no pkgdiff for ${id}`);
    }
    buildsDetails.value[selectedArch.value][id]["pkgdiff"] = pkgdiff;
  }
}

function parseArgs() {
  // stream param
  if (!route.query.stream) {
    // default to stable stream
    switchStream("stable");
  } else if (route.query.stream.match("^(stable|testing|next)$")) {
    switchStream(route.query.stream);
  }
  // arch param
  if (!route.query.arch) {
    // default to x86_64 arch
    switchArch("x86_64");
  } else if (route.query.arch.match("^(x86_64|aarch64|s390x|ppc64le)$")) {
    switchArch(route.query.arch);
  }
}

onMounted(() => {
  parseArgs();
});
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
      <h1 class="text-center text-3xl text-fp-magenta">Streams<br /><br /></h1>
      <div class="coreos-stream container mx-auto max-w-7xl px-2">
        <div class="mx-auto px-24 pb-4">
          <div
            class="coreos-selector grid grid-cols-1 gap-4 text-center text-fp-darkblue-500 dark:text-white sm:grid-cols-3"
          >
            <a
              id="stable"
              class="active"
              href="#"
              @click="switchStream('stable')"
            >
              <FpCard title="stable"> </FpCard>
            </a>
            <a id="testing" href="#" @click="switchStream('testing')">
              <FpCard title="testing"> </FpCard>
            </a>
            <a id="next" href="#" @click="switchStream('next')">
              <FpCard title="next"> </FpCard>
            </a>
          </div>
        </div>
      </div>
      <!-- Mini arch selector -->
      <h1 class="text-center text-3xl text-fp-magenta">
        <br />Architectures<br /><br />
      </h1>
      <div class="coreos-arch container mx-auto max-w-7xl px-2">
        <div class="mx-auto px-24 pb-4">
          <div
            class="coreos-selector grid grid-cols-1 gap-4 text-center text-fp-darkblue-500 dark:text-white sm:grid-cols-2"
          >
            <a
              id="x86_64"
              class="active"
              href="#"
              @click="switchArch('x86_64')"
            >
              <FpCard title="x86_64"> </FpCard>
            </a>
            <a id="aarch64" href="#" @click="switchArch('aarch64')">
              <FpCard title="aarch64"> </FpCard>
            </a>
            <a id="s390x" href="#" @click="switchArch('s390x')">
              <FpCard title="s390x"> </FpCard>
            </a>
            <a id="ppc64le" href="#" @click="switchArch('ppc64le')">
              <FpCard title="ppc64le"> </FpCard>
            </a>
          </div>
        </div>
      </div>
    </section>

    <!-- Release notes -->
    <section class="scroll-mt-14 bg-blue-50 py-6 px-2 dark:bg-neutral-800">
      <div
        class="container mx-auto grid max-w-max divide-y divide-dotted divide-fp-gray text-fp-gray-600 dark:text-fp-gray-200"
      >
        <template v-if="buildsList[selectedStream]?.builds">
          <template v-for="build in buildsList[selectedStream]?.builds">
            <CoreOsBuildInfo
              v-if="build.arches.includes(selectedArch)"
              :buildid="build.id"
              :build-details="buildsDetails[selectedArch]?.[build.id]"
              :build-info="buildsList[selectedStream]?.releases[build.id]"
              @load-build="loadBuild"
            />
          </template>
        </template>
        <template v-else>
          <div class="mx-auto mt-8 text-center">
            <Icon
              name="ei:spinner-3"
              size="64"
              class="animate-spin !align-baseline text-fp-magenta"
            />
          </div>
        </template>
      </div>
    </section>
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
