<script setup>
const { t } = useI18n();
defineProps({
  showBeta: {
    type: Boolean,
    default: false,
  },
  releaver: {
    type: Number,
  },
  betaver: {
    type: Number,
  },
});

// Fetch pre-generated Cloud AMIs list
const cloud_ami = await getCMS("editions/cloud/ami_list");
const showAMI = useState("showAMI", () => ({ show: false }));
const showAzure = useState("showAzure", () => ({ show: false }));

const arches = {
  x86_64: {
    desc: t("x86_64-based instances"),
    azId: "x64",
    azSecurityType: "TrustedLaunch",
  },
  arm64: {
    desc: t("ARM® aarch64-based instances"),
    azId: "Arm64",
    azSecurityType: "Standard",
  },
};

const btnTitles = {
  aws: t("List AWS EC2 region"),
  az: t("List Azure region"),
};

// TODO: Find a way to share that with the coreos dl page
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

const Azure_regions = {
  southafricanorth: "(Africa) South Africa North",
  australiaeast: "(Asia Pacific) Australia East",
  centralindia: "(Asia Pacific) Central India",
  eastasia: "(Asia Pacific) East Asia",
  japaneast: "(Asia Pacific) Japan East",
  koreacentral: "(Asia Pacific) Korea Central",
  southeastasia: "(Asia Pacific) Southeast Asia",
  canadacentral: "(Canada) Canada Central",
  northeurope: "(Europe) North Europe",
  uksouth: "(Europe) UK South",
  westeurope: "(Europe) West Europe",
  francecentral: "(Europe) France Central",
  switzerlandnorth: "(Europe) Switzerland North",
  germanywestcentral: "(Europe) Germany West Central",
  italynorth: "(Europe) Italy North",
  norwayeast: "(Europe) Norway East",
  swedencentral: "(Europe) Sweden Central",
  polandcentral: "(Europe) Poland Central",
  spaincentral: "(Europe) Spain Central",
  brazilsouth: "(South America) Brazil South",
  mexicocentral: "(Mexico) Mexico Central",
  uaenorth: "(Middle East) UAE North",
  israelcentral: "(Middle East) Israel Central",
  qatarcentral: "(Middle East) Qatar Central",
  eastus: "(US) East US",
  eastus2: "(US) East US 2",
  centralus: "(US) Central US",
  southcentralus: "(US) South Central US",
  westus2: "(US) West US 2",
  westus3: "(US) West US 3",
};

function updateAMIs(art) {
  showAMI.value.art = art;
  if (document) {
    document.body.classList.add("has-modal");
  }
  showAMI.value.show = true;
}

function updateAzure(version, arch) {
  showAzure.value.version = version;
  showAzure.value.arch = arch;
  showAzure.value.show = true;
}

function AzureLink(regionID, showBeta) {
  const ImageName = `Fedora-Cloud-${showAzure.value.version}${(showBeta) ? '-Prerelease' : ''}-${
    arches[showAzure.value.arch].azId
  }`;
  const communityImage = `/CommunityGalleries/Fedora-5e266ba4-2250-406d-adad-5d73860d958f/Images/${ImageName}`;

  const Azure_params = {
    displayName: ImageName,
    osType: "Linux",
    imageId: `/providers/Microsoft.Compute/locations/eastus/${communityImage}`,
    communityImage: communityImage,
    location: regionID,
    allowedLocations: Object.keys(Azure_regions),
    isSharedImage: true,
    isSpecializedImage: false,
    hyperVGeneration: "V2",
    architecture: arches[showAzure.value.arch].azId,
    securityType: arches[showAzure.value.arch].azSecurityType,
  };

  return `https://portal.azure.com/#view/Microsoft_Azure_Compute/CreateVmBlade/imageReference~/${encodeURIComponent(
    JSON.stringify(Azure_params),
  )}`;
}

function closeModal(state) {
  if (document) {
    document.body.classList.remove("has-modal");
  }
  state.show = false;
}
</script>
<template>
  <div class="container mx-auto my-8 max-w-7xl px-2">
    <h2
      class="mb-4 scroll-mt-20 text-fp-blue dark:text-gray-200"
      id="cloud_launch"
    >
      {{ $t("Launch on public cloud platforms") }}
    </h2>
    <p class="mb-5 text-gray-600 dark:text-fp-gray-light">
      {{ $t("Start Fedora Cloud instances on public cloud platforms.") }}
    </p>
    <div
      class="grid grid-flow-dense auto-rows-max grid-cols-1 gap-8 lg:grid-cols-2"
    >
      <template v-if="showBeta == false">
        <template v-for="(arch, arch_id) in arches">
          <div>
            <p class="my-2 font-bold">{{ arch.desc }}</p>
            <div class="download-section mb-2 cloud-theme">
              <FpDownloadItem
                :name="`Fedora Cloud ${releaver}`"
                type="aws"
                v-if="cloud_ami?.ga[arch_id]"
              >
                <template #btn>
                  <a
                    :title="btnTitles.aws"
                    class="rounded-xl"
                    @click="updateAMIs(cloud_ami.ga[arch_id])"
                  >
                    <Icon name="fa-solid:th-list" class="!align-baseline" />
                  </a>
                </template>
              </FpDownloadItem>
            </div>
            <div class="download-section mb-2 cloud-theme">
              <FpDownloadItem :name="`Fedora Cloud ${releaver}`" type="azure">
                <template #btn>
                  <a
                    :title="btnTitles.az"
                    class="rounded-xl"
                    @click="updateAzure(releaver, arch_id)"
                  >
                    <Icon name="fa-solid:th-list" class="!align-baseline" />
                  </a>
                </template>
              </FpDownloadItem>
            </div>
          </div>
        </template>
      </template>
      <template v-else-if="showBeta == true">
        <template v-for="(arch, arch_id) in arches">
          <div>
            <p class="my-2 font-bold">{{ arch.desc }}</p>
            <div class="download-section mb-2 cloud-theme">
              <FpDownloadItem
                :name="`Fedora Cloud ${betaver}`"
                type="aws"
                v-if="cloud_ami?.beta[arch_id]"
              >
                <template #btn>
                  <a
                    title="List AWS EC2 region"
                    class="rounded-xl"
                    @click="updateAMIs(cloud_ami.beta[arch_id])"
                  >
                    <Icon name="fa-solid:th-list" class="!align-baseline" />
                  </a>
                </template>
              </FpDownloadItem>
            </div>
            <div class="download-section mb-2 cloud-theme">
              <FpDownloadItem :name="`Fedora Cloud ${betaver}`" type="azure">
                <template #btn>
                  <a
                    title="List Azure region"
                    class="rounded-xl"
                    @click="updateAzure(betaver, arch_id)"
                  >
                    <Icon name="fa-solid:th-list" class="!align-baseline" />
                  </a>
                </template>
              </FpDownloadItem>
            </div>
          </div>
        </template>
      </template>
      <template v-else>
        <div class="text-center font-bold lg:col-span-2">
          {{ $t("No files available for this version.") }}
        </div>
      </template>
    </div>
  </div>

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
        <h5 class="text-xl font-medium ltr:text-left rtl:text-right">
          {{ $t("Select AWS EC2 region") }}
        </h5>
      </template>
      <table class="w-full table-auto ltr:text-left rtl:text-right">
        <thead>
          <tr>
            <th class="">Region</th>
            <th class="hidden sm:block">AMI ID</th>
            <th class="text-center">{{ $t("Launch instance") }}</th>
          </tr>
        </thead>
        <tbody>
          <tr
            v-for="(ami, region) in showAMI.art"
            class="hover:bg-gray-200 hover:dark:bg-slate-800"
          >
            <td class="ltr:pr-6 rtl:pl-6">
              {{ EC2_regions[region] || region }}
            </td>
            <td class="hidden ltr:pr-6 rtl:pl-6 sm:block">{{ ami }}</td>
            <td class="text-center">
              <FpLink
                :href="`https://console.aws.amazon.com/ec2/home?region=${region}#LaunchInstances:ami=${ami}`"
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
      v-if="showAzure.show"
      @close-modal="closeModal(showAzure)"
    >
      <template #header>
        <h5 class="text-xl font-medium ltr:text-left rtl:text-right">
          {{ $t("Select the Azure region") }}
        </h5>
      </template>
      <table class="w-full table-auto ltr:text-left rtl:text-right">
        <thead>
          <tr>
            <th class="">Region</th>
            <th class="text-center">{{ $t("Launch instance") }}</th>
          </tr>
        </thead>
        <tbody>
          <tr
            v-for="(regionName, regionID) in Azure_regions"
            class="hover:bg-gray-200 hover:dark:bg-slate-800"
          >
            <td class="ltr:pr-6 rtl:pl-6">
              {{ regionName }}
            </td>
            <td class="text-center">
              <a
                :href="AzureLink(regionID, showBeta)"
                target="blank"
                :title="`Launch in ${regionName}`"
                class="rounded-xl"
              >
                <Icon
                  name="material-symbols:rocket-launch"
                  class="!align-baseline"
                />
              </a>
            </td>
          </tr>
        </tbody>
      </table>
    </FpModal>
  </Transition>
</template>
