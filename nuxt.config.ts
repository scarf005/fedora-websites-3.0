import locales from "./locales/locales.json";
var path = require('path');

const base = process?.env?.CI_PAGES_URL
  ? new URL(process?.env?.CI_PAGES_URL).pathname
  : "/";

// https://v3.nuxtjs.org/api/configuration/nuxt.config
export default defineNuxtConfig({
  components: [
    "~/components/",
    "~/components/ui",
    "~/components/utilities",
    "~/components/partials",
  ],
  modules: [
    "@nuxtjs/color-mode",
    "@nuxtjs/tailwindcss",
    "@nuxt/content",
    "@nuxtjs/i18n",
    "nuxt-icon",
  ],
  tailwindcss: {
    cssPath: "~/assets/css/main.css",
  },
  colorMode: {
    classSuffix: "",
  },
  i18n: {
    locales: locales,
    langDir: "./locales/",
    strategy: "prefix_except_default",
    defaultLocale: "en",
    vueI18n: {
      legacy: false,
      fallbackLocale: "en",
    },
  },
  app: {
    baseURL: base,
    buildAssetsDir: "/_nuxt/",
    head: {
      titleTemplate: "%s | The Fedora Project",
      script: [{ src: path.join(base,'assets/js/darkmode.js'), defer: true}],
    },
  }
});
