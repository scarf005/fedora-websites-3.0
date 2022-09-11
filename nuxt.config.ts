import { defineNuxtConfig } from "nuxt";
import locales from './locales/locales.json';

const base = process?.env?.CI_PAGES_URL
  ? new URL(process?.env?.CI_PAGES_URL).pathname
  : "";


// https://v3.nuxtjs.org/api/configuration/nuxt.config
export default defineNuxtConfig({
  css: ["@fortawesome/fontawesome-svg-core/styles.css"],
  components: [
    "~/components/",
    "~/components/layout",
    "~/components/ui",
    "~/components/utilities",
  ],
  build: {
    transpile: [
      "@fortawesome/fontawesome-svg-core",
      "@fortawesome/free-solid-svg-icons",
      "@fortawesome/free-regular-svg-icons",
      "@fortawesome/free-brands-svg-icons",
      "@fortawesome/vue-fontawesome",
    ],
  },
  buildModules: ["@pinia/nuxt"],
  modules: ["@nuxtjs/tailwindcss", "@nuxt/content", "@nuxtjs/i18n"],
  tailwindcss: {
    cssPath: "~/assets/css/main.css",
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
  buildAssetsDir: base + "/_nuxt/",
  app: {
    baseURL: base,
    buildAssetsDir: base + "/_nuxt/",
  },
});
