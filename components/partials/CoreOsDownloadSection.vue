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

function getMajor(version) {
  return version.split(".")[0];
}
</script>

<template>
  <div>
    <p class="mt-2 font-bold">{{ $t(name) }}</p>

    <template v-for="(arts, art_type) in artifacts" key="art_type">
      <div
        v-for="(v, k) in arts?.formats"
        key="k"
        class="download-section mb-2"
      >
        <FpDownloadItem
          :name="'Fedora CoreOS ' + getMajor(arts.release)"
          :type="art_type != 'metal' ? art_type : k"
          :format="k"
          verifyLink="#"
          :downloadLink="v.disk?.location"
          :theme="theme"
          v-if="v.disk"
        />
        <FpDownloadItem
          :name="'Fedora CoreOS ' + getMajor(arts.release)"
          :type="art_type != 'metal' ? art_type : k"
          :format="name"
          verifyLink="#"
          :downloadLink="image.location"
          :theme="theme"
          v-else
          v-for="(image, name) in v"
        />
      </div>
    </template>
  </div>
</template>

<style>
.download-section .fp-download-item {
  @apply first:rounded-t-xl last:rounded-b-xl;
}
</style>
