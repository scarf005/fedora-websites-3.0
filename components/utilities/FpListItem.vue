<script setup>
import { mdparser } from "../../config/utilities";

const { t } = useI18n();
const props = defineProps({
  title: String,
  description: String,
  image: String,
  url: String,
  iconURI: String,
});
let descriptionMd;
if (props.description) {
  descriptionMd = await mdparser(t(props.description));
}
</script>
<template>
  <li
    class="mb-8 w-10/12"
    :style="
      iconURI
        ? {
            background: `url(${
              $config.app.baseURL + '/' + iconURI.replace('public/', '')
            }) no-repeat left top`,
            'padding-left': '60px',
            'list-style': 'none',
          }
        : 'null'
    "
  >
    <div v-if="props.image" class="flex h-64 items-center justify-center">
      <FpImage :src="props.image" />
    </div>
    <h4
      v-if="title"
      class="inline font-bold text-fp-blue-dark dark:text-slate-100"
    >
      {{ $t(props.title) }}
    </h4>
    <ContentRenderer
      v-if="descriptionMd"
      class="text-fp-blue-dark dark:text-slate-200"
      tag="p"
      :value="descriptionMd"
    />
    <br />
    <div v-if="props.url" class="flex items-center justify-center">
      <FpBtn :url="props.url">{{ $t("Learn More") }}</FpBtn>
    </div>
  </li>
</template>
