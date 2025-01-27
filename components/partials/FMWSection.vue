<script setup>
const data = await getCMS("partials/fedora-media-writer");
const descriptionMd = await mdparser(data._value.description);
</script>

<template>
  <div class="container mx-auto grid max-w-7xl grid-cols-2 mb-4">
    <div class="col-span-2 p-2 md:col-span-1">
      <FpImage
        :src="data.logo.image"
        :alt="data.logo.text"
        class="w-1/4 float-start"
      />
      <ContentRendererMarkdown
        class="markdown font-normal text-fp-gray dark:text-gray-300"
        :value="descriptionMd"
      />
      <div v-for="item in data.links" class="download-section mb-2">
        <FpDownloadItem name="Fedora Media Writer" :format="item.title">
          <template #btn>
            <FpLink
              :href="item.button.url"
              :title="$t('Download')"
              target="_blank"
              class="rounded-xl"
            >
              <Icon :name="item.button.icon" class="!align-baseline" />
            </FpLink>
          </template>
        </FpDownloadItem>
      </div>
    </div>
    <div
      class="col-span-2 flex items-center justify-center mb-4 p-2 md:col-span-1"
    >
      <FpImage class="max-h-72" :src="data.image" />
    </div>
  </div>
</template>

<style scoped>
.markdown :deep(h2) {
  @apply mb-[1ex] text-fp-blue dark:text-gray-200;
}
.markdown :deep(p) {
  @apply mb-[1em];
}
.markdown :deep(a) {
  @apply text-fp-newblue-500;
  @apply dark:text-fp-darkblue-500;
}
.markdown :deep(ul) li {
  @apply list-none before:content-['*_'] -indent-[1.5ex] ms-[1.5ex] mb-[1.5em] text-sm;
}
.download-section .fp-download-item a {
  @apply border-fp-newblue-500 text-fp-newblue-500 hover:bg-fp-newblue-500 hover:text-white;
  @apply dark:border-fp-darkblue-500 dark:text-fp-darkblue-500 dark:hover:bg-fp-darkblue-500 dark:hover:text-white;
}
.download-section .fp-download-item {
  @apply bg-gray-50;
  @apply dark:bg-neutral-800;
}
</style>
