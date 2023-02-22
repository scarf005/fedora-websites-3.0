<script setup>
const { t } = useI18n();
const slots = useSlots();
const props = defineProps({
  name: {
    type: String,
  },
  type: {
    type: String,
  },
  format: {
    type: String,
  },
  theme: {
    type: String,
  },
  variants: {
    type: Array,
    default: [],
  },
  downloadLink: {
    type: String,
  },
  verifyLink: {
    type: String,
  },
  betaVersion: {
    type: Boolean,
  },
});

const variantClasses = props.variants.map(
  (v) => `fp-download-item--variant-${v}`
);

const prettyType = {
  aliyun: "Alibaba Cloud",
  aws: "AWS",
  azure: "Azure",
  azurestack: "Azure Stack",
  digitalocean: "DigitalOcean",
  exoscale: "Exoscale",
  gcp: "GCP",
  hyperv: "Hyper-V",
  ibmcloud: "IBM Cloud",
  "raw.xz": "Raw",
  "raw-xz": "Raw",
  "4k.raw.xz": "Raw (4k Native)",
  iso: "Live DVD",
  dvd: "DVD",
  "dvd-ostree": "OSTree",
  pxe: "Netboot",
  nutanix: "Nutanix",
  openstack: "OpenStack",
  packet: "Packet",
  qemu: "QEMU",
  qcow2: "QEMU",
  virtualbox: "VirtualBox",
  vmware: "VMware",
  vultr: "Vultr",
  "vagrant-libvirt": "Vagrant",
  "vagrant-virtualbox": "Vagrant",
  "tar-gz": "Compressed Image",
  boot: "Netboot",
  live: "Live ISO",
};
</script>

<template>
  <div
    :class="[
      betaVersion ? 'fp-beta-download-item' : 'fp-download-item',
      variantClasses,
      theme,
    ]"
  >
    <div class="flex items-center justify-between">
      <p class="text-gray-800 dark:text-gray-400">
        <slot>
          <span class="mr-5 font-semibold">
            {{ name }}
          </span>
          <span class="mr-5">{{ prettyType[type] }}</span>
          <span class="text-gray-500"> {{ format }}</span>
          <span
            v-if="betaVersion"
            class="ml-4 rounded-full bg-gray-300 px-2 text-sm font-bold text-white dark:bg-gray-700"
            >{{ $t("BETA") }}</span
          >
        </slot>
      </p>
      <div class="inline-flex">
        <slot name="btn">
          <a @click="$emit('verifyClick')" title="Verify" class="rounded-l-xl">
            <Icon name="fa-solid:clipboard-check" class="!align-baseline" />
          </a>
          <FpLink
            :href="downloadLink"
            v-if="downloadLink"
            title="Download"
            class="-ml-px rounded-r-xl"
          >
            <Icon name="fa-download" class="!align-baseline" />
          </FpLink>
        </slot>
      </div>
    </div>
    <slot name="footer" />
  </div>
</template>

<style>
.fp-download-item {
  @apply border border-gray-200 bg-white px-5 py-2 dark:border-gray-900 dark:bg-neutral-900;
}

.fp-beta-download-item {
  @apply border border-gray-200 bg-blue-50 px-5 py-2 dark:border-gray-900 dark:bg-gray-800;
}

.fp-download-item a,
.fp-beta-download-item a {
  @apply cursor-pointer border py-1 px-3 transition-colors;
}
</style>
