<script setup>
const { t } = useI18n();
const slots = useSlots();
const props = defineProps({
  name: {
    type: String,
  },
  artifacts: {
    type: Object,
  },
  theme: {
    type: String,
    default: "blue",
  },
});

const prettyPlatforms = {
  aliyun: "Alibaba Cloud",
  aws: "AWS",
  azure: "Azure",
  azurestack: "Azure Stack",
  digitalocean: "DigitalOcean",
  exoscale: "Exoscale",
  gcp: "GCP",
  ibmcloud: "IBM Cloud",
  metal: {
    "raw.xz": "Raw",
    "4k.raw.xz": "Raw (4k Native)",
    iso: "ISO",
    pxe: "PXE",
  },
  nutanix: "Nutanix",
  openstack: "OpenStack",
  packet: "Packet",
  qemu: "QEMU",
  virtualbox: "VirtualBox",
  vmware: "VMware",
  vultr: "Vultr",
};

const themeClasses = {
  blue: "text-blue-500 hover:bg-blue-500 border-blue-500",
  green:
    "text-fp-green dark:text-green-600 dark:hover:bg-green-600 hover:bg-fp-green dark:hover:text-white border-fp-green dark:border-green-600",
  orange: "text-fp-orange hover:bg-fp-orange border-fp-orange",
};

function getMajor(version) {
  return version.split(".")[0];
}
</script>

<template>
  <div>
    <p class="mt-2 font-bold">{{ $t(name) }}</p>

    <template v-for="(arts, art_type) in artifacts">
      <div v-for="(v, k) in arts?.formats">
        <div
          class="mb-2 flex items-center justify-between rounded-xl border border-gray-200 bg-white px-5 py-2 dark:border-gray-900 dark:bg-neutral-900"
          v-if="v.disk"
        >
          <p class="text-gray-800 dark:text-gray-400">
            <span class="mr-5 font-semibold">
              Fedora CoreOS {{ getMajor(arts.release) }}
            </span>
            <span v-if="art_type != 'metal'" class="mr-5">{{
              prettyPlatforms[art_type]
            }}</span>
            <span v-else class="mr-5">{{ prettyPlatforms.metal[k] }}</span>
            <span class="text-gray-500"> {{ k }}</span>
          </p>
          <div class="inline-flex">
            <FpLink
              href="#"
              title="Verify"
              class="rounded-l-xl border py-1 px-3 hover:text-white"
              :class="themeClasses[theme]"
            >
              <Icon name="fa-solid:clipboard-check" class="!align-baseline" />
            </FpLink>
            <FpLink
              :href="v.disk.location"
              title="Download"
              class="-ml-px rounded-r-xl border py-1 px-3 hover:text-white"
              :class="themeClasses[theme]"
            >
              <Icon name="fa-download" class="!align-baseline" />
            </FpLink>
          </div>
        </div>

        <div v-else class="mb-2">
          <div
            class="flex items-center justify-between border border-gray-200 bg-white px-5 py-2 first:rounded-t-xl last:rounded-b-xl dark:border-gray-900 dark:bg-neutral-900"
            v-for="(image, name) in v"
          >
            <p class="text-gray-800 dark:text-gray-400">
              <span class="mr-5 font-semibold">
                Fedora CoreOS {{ getMajor(arts.release) }}
              </span>
              <span class="mr-5">{{ prettyPlatforms.metal[k] }}</span>
              <span class="text-gray-500"> {{ name }}</span>
            </p>
            <div class="inline-flex">
              <FpLink
                href="#"
                title="Verify"
                class="rounded-l-xl border py-1 px-3 hover:text-white"
                :class="themeClasses[theme]"
              >
                <Icon name="fa-solid:clipboard-check" class="!align-baseline" />
              </FpLink>
              <FpLink
                :href="image.location"
                title="Download"
                class="-ml-px rounded-r-xl border py-1 px-3 hover:text-white"
                :class="themeClasses[theme]"
              >
                <Icon name="fa-download" class="!align-baseline" />
              </FpLink>
            </div>
          </div>
        </div>
      </div>
    </template>
  </div>
</template>
