<script setup>
import locales from "../../config/locales.json";

const { locale } = useI18n();
const localePath = useLocalePath();

const props = defineProps({
  href: String,
  current: Boolean,
  class: String,
  rel: String,
  i18n: Boolean,
});

let link = props.href;
if (/^https:\/\/docs.fedoraproject.org\//.test(link) && locale._value != "en") {
  let code = locales.find((l) => l.code == locale._value).iso;
  code = code.replace("-", "_"); // make pt-br (and others?) work
  link = props.href.replace("en-US", code);
}
</script>

<template>
  <a
    :href="`${
      i18n // i18n switcher link
        ? $config.app.baseURL.replace(new RegExp('/$'), '') + href
        : /^https:/.test(link) // external link
        ? link
        : $config.app.baseURL.replace(new RegExp('/$'), '') + localePath(href) // normal in-site link
    }`"
    :aria-current="current ? 'page' : undefined"
    :rel="rel"
    :class="class"
  >
    <slot></slot>
  </a>
</template>
