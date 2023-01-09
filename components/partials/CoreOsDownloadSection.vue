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

function getMajor(version) {
  return version.split(".")[0];
}
</script>

<template>
  <div>
    <p class="my-2 font-bold">{{ $t(name) }}</p>

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
          :downloadLink="v.disk?.location"
          :theme="theme"
          v-if="v.disk"
        />
        <FpDownloadItem
          :name="'Fedora CoreOS ' + getMajor(arts.release)"
          :type="art_type != 'metal' ? art_type : k"
          :format="name"
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
