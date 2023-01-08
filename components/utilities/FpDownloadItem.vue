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
  ibmcloud: "IBM Cloud",
  "raw.xz": "Raw",
  "4k.raw.xz": "Raw (4k Native)",
  iso: "ISO",
  pxe: "Netboot",
  nutanix: "Nutanix",
  openstack: "OpenStack",
  packet: "Packet",
  qemu: "QEMU",
  virtualbox: "VirtualBox",
  vmware: "VMware",
  vultr: "Vultr",
};
</script>

<template>
  <div :class="['fp-download-item', variantClasses, theme]">
    <p class="text-gray-800 dark:text-gray-400">
      <slot>
        <span class="mr-5 font-semibold">
          {{ name }}
        </span>
        <span class="mr-5">{{ prettyType[type] }}</span>
        <span class="text-gray-500"> {{ format }}</span>
      </slot>
    </p>
    <div class="inline-flex">
      <slot name="btn">
        <FpLink
          :href="verifyLink"
          v-if="verifyLink"
          title="Verify"
          class="rounded-l-xl border py-1 px-3 hover:text-white"
        >
          <Icon name="fa-solid:clipboard-check" class="!align-baseline" />
        </FpLink>
        <FpLink
          :href="downloadLink"
          v-if="downloadLink"
          title="Download"
          class="-ml-px rounded-r-xl border py-1 px-3 hover:text-white"
        >
          <Icon name="fa-download" class="!align-baseline" />
        </FpLink>
      </slot>
    </div>
  </div>
</template>

<style>
.fp-download-item {
  @apply flex items-center justify-between border border-gray-200 bg-white px-5 py-2 dark:border-gray-900 dark:bg-neutral-900;
}

.fp-download-item.blue a {
  @apply border-blue-500 text-blue-500 hover:bg-blue-500 hover:text-white;
}

.fp-download-item.green a {
  @apply border-fp-green text-fp-green hover:bg-fp-green hover:text-white dark:border-green-600 dark:text-green-600 dark:hover:bg-green-600;
}

.fp-download-item.orange a {
  @apply border-fp-orange text-fp-orange hover:bg-fp-orange hover:text-white;
}
</style>
