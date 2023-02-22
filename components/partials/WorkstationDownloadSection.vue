<script setup>
const { t } = useI18n();
const slots = useSlots();
const props = defineProps({
  name: {
    type: String,
  },
  art_name: {
    type: String,
  },
  version: {
    type: String,
  },
  betaVersion: {
    type: String,
  },
  artifacts: {
    type: Object,
  },
  theme: {
    type: String,
    default: "blue",
  },
  dlPrefix: {
    type: String,
  },
});
</script>

<template>
  <div>
    <p class="my-2 font-bold">{{ $t(name) }}</p>

    <div v-for="(v, k) in artifacts" key="k" class="download-section mb-2">
      <FpDownloadItem
        :name="`${art_name} ${version}`"
        :type="v.type"
        :format="v.format"
        :downloadLink="`${dlPrefix}/${version}/${v.path}`"
        @verify-click="$emit('verifyClick', v)"
        :theme="theme"
        v-if="v.arch != 'src'"
        class="mb-2"
      />
    </div>
    <div v-for="(v, k) in artifacts" key="k" class="download-section mb-2">
      <FpDownloadItem
        :name="`${art_name} ${betaVersion}`"
        :type="v.type"
        :format="v.format"
        :downloadLink="`${dlPrefix}/${betaVersion}/${v.path}`"
        @verify-click="$emit('verifyClick', v)"
        :theme="theme"
        v-if="v.arch != 'src' && betaVersion"
        betaVersion
      />
    </div>
  </div>
</template>

<style>
.download-section .fp-download-item,
.download-section .fp-beta-download-item {
  @apply first:rounded-t-xl last:rounded-b-xl;
}
</style>
