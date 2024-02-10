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
  art_variant: {
    type: String,
  },
  version: {
    type: Number,
  },
  rc: {
    type: String,
  },
  artifacts: {
    type: Object,
  },
  theme: {
    type: String,
    default: "blue",
  },
  variants: {
    type: Array,
    default: [],
  },
  dlPrefix: {
    type: String,
  },
  isBeta: {
    type: Boolean,
    default: false,
  },
  checksum_file: {
    type: Boolean,
    default: false,
  },
});

function checksum_filename(arch, format, beta = false) {
  const f = format == "iso" ? "iso" : "images";
  if (beta) {
    return [
      "Fedora",
      props.art_variant,
      f,
      props.version + "_Beta",
      props.rc,
      arch,
      "CHECKSUM",
    ].join("-");
  } else {
    return [
      "Fedora",
      props.art_variant,
      props.version,
      props.rc,
      arch,
      "CHECKSUM",
    ].join("-");
  }
}

function checksum_path(dl_prefix, arch, format, beta = false) {
  const f = format == "iso" ? "iso" : "images";
  if (beta) {
    if (dl_prefix) {
      return [
        dl_prefix,
        props.art_variant,
        arch,
        f,
        checksum_filename(arch, format, (beta = true)),
      ].join("/");
    } else {
      return [
        props.dlPrefix,
        "test",
        props.version + "_Beta",
        props.art_variant,
        arch,
        f,
        checksum_filename(arch, format, (beta = true)),
      ].join("/");
    }
  } else {
    if (dl_prefix) {
      return [
        dl_prefix,
        props.art_variant,
        arch,
        f,
        checksum_filename(arch, format),
      ].join("/");
    } else {
      return [
        props.dlPrefix,
        props.version,
        props.art_variant,
        arch,
        f,
        checksum_filename(arch, format),
      ].join("/");
    }
  }
}
</script>

<template>
  <div>
    <p class="my-2 font-bold">{{ $t(name) }}</p>

    <div v-for="(v, k) in artifacts" key="k" class="download-section mb-2">
      <FpDownloadItem
        :name="`${art_name} ${version}`"
        :type="v.type"
        :format="v.format"
        :downloadLink="`${dlPrefix}/test/${version}_Beta/${v.path}`"
        :checksumLink="
          checksum_file
            ? checksum_path(v.dl_prefix, v.arch, v.format, (beta = true))
            : undefined
        "
        @verify-click="$emit('verifyClick', v)"
        :theme="theme"
        :arch="v.arch"
        :size="v.size"
        v-if="v.arch != 'src' && isBeta"
        :variants="[...variants, 'beta']"
      />
      <FpDownloadItem
        :name="`${art_name} ${version}`"
        :type="v.type"
        :format="v.format"
        :downloadLink="
          v.dl_prefix
            ? `${v.dl_prefix}/${v.path}`
            : `${dlPrefix}/${version}/${v.path}`
        "
        :checksumLink="
          checksum_file
            ? checksum_path(v.dl_prefix, v.arch, v.format)
            : undefined
        "
        @verify-click="$emit('verifyClick', v)"
        :theme="theme"
        :arch="v.arch"
        :size="v.size"
        :variants="variants"
        v-if="v.arch != 'src' && !isBeta"
      />
    </div>
    <slot name="extra" />
  </div>
</template>

<style>
.download-section .fp-download-item {
  @apply first:rounded-t-xl last:rounded-b-xl;
}
</style>
