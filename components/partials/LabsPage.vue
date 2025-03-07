<script setup>
const route = useRoute();
const props = defineProps({
  name: {
    type: String,
  },
});

const variant_name = props.name.replace("-", "_");
const data = await getCMS(`labs/${props.name.toLowerCase()}`);
const release_data = await getCMS("release");

data._value.descriptionMd = await mdparser(data._value.description);

// TODO: fallback to n-1 version if metadata are not yet available
const { data: ga_data } = await useFetch(
  `https://kojipkgs.fedoraproject.org/compose/${release_data._value.ga.releasever}/latest-Fedora-${release_data._value.ga.releasever}/compose/metadata/images.json`,
  {
    transform: (ga_data) => {
      let image = "Labs";
      if (release_data._value.ga.compose_overrides?.[image]) {
        console.log("Overrides: ");
        console.log(release_data._value.ga.compose_overrides[image]);
        if (!ga_data.payload.images[image]) ga_data.payload.images[image] = {};
        for (var arch in release_data._value.ga.compose_overrides[image]) {
          if (arch in ga_data.payload.images[image]) {
            ga_data.payload.images[image][arch].push(
              ...release_data._value.ga.compose_overrides[image][arch],
            );
          } else {
            ga_data.payload.images[image][arch] =
              release_data._value.ga.compose_overrides[image][arch];
          }
        }
      }
      return ga_data;
    },
    key: "koji-ga",
  },
);

const { data: beta_data } = await useFetch(
  `https://dl.fedoraproject.org/pub/alt/stage/${release_data._value.beta.releasever}_Beta-${release_data._value.beta.rc_version}/metadata/images.json`,
);

// for checksums
const dlpath = {
  x86_64: "https://download.fedoraproject.org/pub/alt/releases",
  aarch64: "https://download.fedoraproject.org/pub/fedora/linux/releases",
  s390x: "https://download.fedoraproject.org/pub/fedora-secondary/releases",
  ppc64le: "https://download.fedoraproject.org/pub/fedora-secondary/releases",
};

const arches = {
  x86_64: "For Intel and AMD x86_64 systems",
  aarch64: "For ARM® aarch64 systems",
  ppc64le: "For Power ppc64le systems",
  s390x: "For IBM s390x zSystems",
};

function checksum_filename(release, rc, beta = false) {
  if (beta) {
    return ["Fedora-Labs", "*", release, rc, "*", "CHECKSUM"].join("-");
  } else {
    return ["Fedora-Labs", release, rc, "*", "CHECKSUM"].join("-");
  }
}

function capitalize(string) {
  return string.charAt(0).toUpperCase() + string.slice(1).toLowerCase();
}

useHead({ htmlAttrs: { class: "scroll-smooth" } });
useContentHead(data);

const betaSwitch = useState("betaSwitch", () => false);
betaSwitch.value = typeof route.query.beta != "undefined";
</script>

<template>
  <main
    class="group/main border-t-8 border-fp-newblue-300 dark:bg-neutral-800"
    :class="`${name.toLowerCase()}`"
  >
    <!-- TITLE -->
    <section
      class="relative z-10 bg-gradient-to-b from-white to-fp-newblue-100 px-2 pt-24 pb-12 text-center dark:bg-none lg:text-start"
    >
      <div class="container mx-auto max-w-7xl px-2">
        <h1 class="mb-8 text-4xl text-gray-600 dark:text-gray-200">
          {{
            $t(data.title) + (betaSwitch ? " " + $t("BETA").toLowerCase() : "")
          }}
        </h1>
        <ContentRendererMarkdown
          class="space-y-6 text-start text-gray-600 dark:text-fp-gray-light lg:w-4/5"
          :value="data.descriptionMd"
        />

        <div class="mt-5 flex flex-wrap gap-10" id="ctas">
          <FpLink
            v-for="link in data.downloadSection.links"
            :href="link.url"
            class="text-blue-500"
          >
            <Icon name="fa-book" />
            {{ $t(link.text) }}
          </FpLink>
          <FpLink
            :href="`https://docs.fedoraproject.org/en-US/fedora/f${release_data.ga.releasever}/release-notes/`"
            class="text-blue-500"
          >
            <Icon name="fa-book" />
            {{ $t("Release Notes") }}
          </FpLink>

          <a
            class="mx-auto sm:mx-0 sm:ml-auto max-w-fit cursor-pointer rounded py-2 px-4 font-medium duration-300 ease-in-out hover:ease-in-out lg:py-3 lg:px-6 bg-fp-newblue-500 text-white hover:bg-fp-newblue-700 dark:bg-fp-newblue-700 dark:hover:bg-fp-newblue-900"
            href="#download_section"
            >{{ $t("Download Now") }}</a
          >
        </div>
      </div>
    </section>

    <section class="group relative z-0 overflow-hidden dark:bg-neutral-900">
      <svg
        viewBox="0 0 209.9868 38.261421"
        width="100%"
        height="100%"
        preserveAspectRatio="none"
        version="1.1"
        id="svg4475"
        class="absolute top-0 z-10 h-20"
        xmlns="http://www.w3.org/2000/svg"
        xmlns:svg="http://www.w3.org/2000/svg"
      >
        <defs id="defs4472" />
        <g id="layer1" transform="translate(0.04450727,-135.47272)">
          <path
            class="fill-fp-newblue-100 dark:fill-neutral-800"
            d="M 209.94229,136.77754 -0.04450727,157.96768 V 135.47272 H 209.94229 Z"
            id="path6102"
          />
        </g>
      </svg>
      <img
        :src="`${
          $config.app.baseURL.replace(new RegExp('/$'), '') +
          '/' +
          data.splash_image.image.replace('public/', '')
        }`"
        class="z-0 h-40 md:h-60 xl:h-96 w-full object-cover"
      />
      <svg
        viewBox="0 0 209.98682 22.494961"
        width="100%"
        height="100%"
        preserveAspectRatio="none"
        version="1.1"
        id="svg4475"
        class="absolute bottom-0 z-10 h-20 hidden xl:block"
        xmlns="http://www.w3.org/2000/svg"
        xmlns:svg="http://www.w3.org/2000/svg"
      >
        <defs id="defs4472" />
        <g id="layer1" transform="matrix(1,0,0,-1,0.04450727,157.96768)">
          <path
            class="fill-fp-newblue-100 dark:fill-neutral-900"
            d="M 209.94229,136.77754 -0.04450727,157.96768 V 135.47272 H 209.94229 Z"
            id="path6102"
          />
        </g>
      </svg>
    </section>

    <!-- Features Section -->
    <section
      class="relative z-0 space-y-24 bg-gradient-to-b from-fp-newblue-100 to-fp-purple-100 pb-20 dark:bg-neutral-900 dark:bg-none"
    >
      <div
        class="mx-auto max-w-7xl rounded-lg bg-white px-12 pt-6 pb-10 dark:bg-neutral-800"
        v-for="section in data.sections"
      >
        <h2
          class="mb-8 text-center text-4xl font-semibold text-fp-blue-500 dark:text-gray-200"
        >
          {{ $t(section.sectionTitle) }}
        </h2>
        <div
          class="flex flex-wrap justify-between gap-4 text-center text-fp-darkblue-500 xl:gap-10"
        >
          <FpCard
            v-for="card in section.content"
            :title="card.title"
            :description="card.description"
            :link="card.link"
            class="mx-auto basis-80 lg:basis-64"
          >
            <template #prepend>
              <FpCardImage slot="prepend" :src="card.image" />
            </template>
            <template #footer v-if="card.link">
              <a
                :href="card.link.url"
                class="dark:text-fp-blue-300 after:content-['_↗']"
                v-if="card.link.text"
                >{{ $t(card.link.text) }}</a
              >
              <a
                :href="card.link.url"
                class="dark:text-fp-blue-300 after:content-['_↗']"
                v-else
                >{{ $t("Learn More") }}</a
              >
            </template>
          </FpCard>
        </div>
      </div>
    </section>

    <!-- DOWNLOAD ARTIFACTS -->
    <section
      class="peer/download scroll-mt-14 bg-gradient-to-r from-sky-50 to-blue-50 py-6 px-2 dark:bg-neutral-800 dark:bg-none"
      id="download_section"
    >
      <div class="container mx-auto max-w-7xl px-2">
        <h1 class="mb-4 text-4xl text-gray-600 dark:text-gray-200">
          {{ $t("Download") }}
          <span
            class="text-fp-newblue-700 group-has-[#betaswitch:checked]/main:hidden"
          >
            {{ data.title }} {{ release_data.ga.releasever }}</span
          >
          <span
            class="text-fp-newblue-700 hidden group-has-[#betaswitch:checked]/main:inline"
          >
            {{ data.title }} {{ release_data.beta.releasever }}
            {{ capitalize($t("BETA")) }}
          </span>
        </h1>

        <div class="mt-5 flex">
          <p
            class="text-sm text-gray-600 ltr:mr-5 rtl:ml-5 dark:text-fp-gray-200"
          >
            {{ $t("RELEASE DATE") }}:
            <time
              :datetime="
                new Date(Number(release_data.ga.release_date)).toISOString()
              "
              class="font-semibold group-has-[#betaswitch:checked]/main:hidden"
              >{{
                $d(Number(release_data.ga.release_date), {
                  dateStyle: "full",
                  timeZone: "UTC",
                })
              }}</time
            >
            <time
              :datetime="
                new Date(Number(release_data.beta.release_date)).toISOString()
              "
              class="font-semibold hidden group-has-[#betaswitch:checked]/main:inline"
              >{{
                $d(Number(release_data.beta.release_date), {
                  dateStyle: "full",
                  timeZone: "UTC",
                })
              }}</time
            >
          </p>
        </div>
      </div>

      <div class="container mx-auto max-w-7xl">
        <div
          class="flex items-center justify-end gap-4 peer/beta"
          v-if="release_data.beta.enabled && beta_data"
        >
          <p class="text-fp-gray">{{ $t("Show Beta downloads") }}</p>
          <ClientOnly>
            <FpSwitch
              id="betaswitch"
              @switchToggled="betaSwitch = $event.target.checked"
              :checked="betaSwitch"
            />
            <template #fallback>
              <FpSwitch
                id="betaswitch"
                @switchToggled="betaSwitch = $event.target.checked"
                :checked="false"
              />
            </template>
          </ClientOnly>
        </div>
        <div class="flex justify-end">
          <FpJoinTip
            description="Help us with testing!"
            inline
            class="origin-right scale-75"
          />
        </div>
        <div
          class="group flex gap-8 flex-wrap justify-center peer-has-[:checked]/beta:hidden"
        >
          <!-- GA artifacts -->
          <template v-if="ga_data?.payload">
            <template v-for="(arch_desc, arch_id) in arches">
              <DownloadSection
                :name="arch_desc"
                v-if="
                  ga_data.payload.images.Labs[arch_id]?.filter((a) =>
                    a.subvariant.startsWith(variant_name),
                  ).length
                "
                :art_name="data.title"
                art_variant="Labs"
                :artifacts="
                  ga_data.payload.images.Labs[arch_id].filter((a) =>
                    a.subvariant.startsWith(variant_name),
                  )
                "
                :dlPrefix="dlpath[arch_id]"
                checksum_file
                :version="release_data.ga.releasever"
                :rc="release_data.ga.rc_version"
                class="labs-theme basis-[620px] grow lg:grow-0"
                :variants="['labs']"
              />
            </template>
          </template>
          <div
            class="text-center font-bold lg:col-span-2 group-has-[.download-section]:hidden"
          >
            {{ $t("No files available for this version.") }}
          </div>
        </div>

        <!-- Beta artifacts -->
        <div
          class="group gap-8 flex-wrap justify-center hidden peer-has-[:checked]/beta:flex"
        >
          <template v-if="beta_data?.payload?.images?.Labs">
            <template v-for="(arch_desc, arch_id) in arches">
              <DownloadSection
                :name="arch_desc"
                v-if="
                  beta_data.payload.images.Labs[arch_id]?.filter((a) =>
                    a.subvariant.startsWith(variant_name),
                  ).length
                "
                :art_name="data.title"
                art_variant="Labs"
                :artifacts="
                  beta_data.payload.images.Labs[arch_id].filter((a) =>
                    a.subvariant.startsWith(variant_name),
                  )
                "
                :dlPrefix="dlpath[arch_id]"
                checksum_file
                :version="release_data.beta.releasever"
                :rc="release_data.beta.rc_version"
                class="labs-theme basis-[620px] grow lg:grow-0"
                :variants="['labs']"
                isBeta
              />
            </template>
          </template>
          <div
            class="text-center font-bold lg:col-span-2 group-has-[.download-section]:hidden"
          >
            {{ $t("No files available for this version.") }}
          </div>
        </div>
      </div>
    </section>

    <!-- Fedora Media Writer -->
    <section class="bg-white py-8 px-4 dark:bg-neutral-900">
      <FMWSection />
    </section>

    <!-- Verify section -->
    <section
      class="group/verify relative z-0 overflow-hidden bg-gray-50 dark:bg-neutral-800 py-6"
      id="verify-section"
    >
      <CoreOsVerifySection>
        <template #instructions>
          <ul
            class="list-outside list-decimal pt-2 ltr:pl-8 ltr:text-left rtl:pr-8 rtl:text-right"
          >
            <li>
              <i18n-t
                keypath="verify_button_download"
                scope="global"
                tag="p"
                class="mb-2"
              >
                <template #verify_button>
                  <Icon
                    name="fa-solid:clipboard-check"
                    class="!align-baseline text-fp-newblue-500 dark:text-gray-200"
                  />
                </template>
              </i18n-t>
            </li>
            <li>
              <p class="mb-2">{{ $t("Import Fedora's GPG key(s)") }}</p>
              <pre
                class="mb-1 bg-slate-100 px-4 text-sm text-gray-800 dark:bg-slate-800 dark:text-gray-300"
              >
                <code>curl -O https://fedoraproject.org/fedora.gpg</code>
              </pre>
              <i18n-t
                keypath="you_can_verify_the_GPG_details"
                scope="global"
                tag="p"
                class="mb-4 text-sm"
              >
                <template #icon>
                  <Icon name="fa-solid:info-circle" class="mx-2 !align-sub" />
                </template>
                <template #here>
                  <FpLink class="text-sm text-fp-blue" href="security">{{
                    $t("here")
                  }}</FpLink>
                </template>
              </i18n-t>
            </li>
            <li>
              <p class="mb-2">{{ $t("Verify the checksum file is valid") }}</p>
              <pre
                class="mb-4 bg-slate-100 px-4 text-sm text-gray-800 dark:bg-slate-800 dark:text-gray-300 group-has-[#betaswitch:checked]/main:hidden"
              >
                <code>gpgv --keyring ./fedora.gpg {{ checksum_filename(release_data.ga.releasever, release_data.ga.rc_version) }}</code>
              </pre>
              <pre
                class="mb-4 bg-slate-100 px-4 text-sm text-gray-800 dark:bg-slate-800 dark:text-gray-300 hidden group-has-[#betaswitch:checked]/main:block"
              >
                <code>gpgv --keyring ./fedora.gpg {{ checksum_filename(release_data.beta.releasever, release_data.beta.rc_version, beta=true) }}</code>
              </pre>
            </li>
            <li>
              <p class="mb-2">{{ $t("Verify the checksum matches") }}</p>
              <pre
                class="mb-4 bg-slate-100 px-4 text-sm text-gray-800 dark:bg-slate-800 dark:text-gray-300 group-has-[#betaswitch:checked]/main:hidden"
              >
                <code>sha256sum -c {{ checksum_filename(release_data.ga.releasever, release_data.ga.rc_version) }}</code>
              </pre>

              <pre
                class="mb-4 bg-slate-100 px-4 text-sm text-gray-800 dark:bg-slate-800 dark:text-gray-300 hidden group-has-[#betaswitch:checked]/main:block"
              >
                <code>sha256sum -c {{ checksum_filename(release_data.beta.releasever, release_data.beta.rc_version, beta=true) }}</code>
              </pre>
            </li>
          </ul>
          <p class="ltr:text-left rtl:text-right">
            {{
              $t(
                "If the output states that the file is valid, then it's ready to use!",
              )
            }}
          </p>
        </template>
      </CoreOsVerifySection>
    </section>

    <!-- COMPLIANCE -->
    <section class="py-12 px-4 dark:bg-black">
      <DownloadComplianceSection />
    </section>
  </main>
</template>

<style>
.labs-theme .fp-download-item a {
  @apply border-fp-newblue-700 text-fp-newblue-700 hover:bg-fp-newblue-700 hover:text-white;
  @apply dark:border-fp-newblue-300 dark:text-fp-newblue-300 dark:hover:bg-fp-newblue-300 dark:hover:text-white;
}

.fp-download-item--variant-labs > div > p {
  @apply justify-between flex-grow;
}

.fp-download-item--variant-labs .dl-format {
  @apply hidden sm:block;
}
</style>
