<script setup>
import locales from "../../config/locales.json";

const { locale } = useI18n();
const localePath = useLocalePath();
const config = useRuntimeConfig();

const props = defineProps({
  href: String,
  target: String,
  current: Boolean,
  class: String,
  rel: String,
  i18n: Boolean,
});

function processLink(href) {
  let link = href;
  if (
    /^https:\/\/docs.fedoraproject.org\//.test(href) &&
    locale._value != "en"
  ) {
    let code = locales.find((l) => l.code == locale._value).iso;
    code = code.replace("-", "_"); // make pt-br (and others?) work
    link = href.replace("en-US", code);
  }

  if (props.i18n) {
    // i18n switcher link
    link = config.app.baseURL.replace(new RegExp("/$"), "") + href;
  } else if (!/^https:/.test(href)) {
    link = config.app.baseURL.replace(new RegExp("/$"), "") + localePath(href); // normal in-site link
  }

  return link;
}
</script>

<template>
  <a
    :href="processLink(href)"
    :aria-current="current ? 'page' : undefined"
    :rel="rel"
    :class="class"
    :target="target"
  >
    <slot></slot>
  </a>
</template>
