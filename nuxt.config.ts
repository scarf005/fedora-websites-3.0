import { defineNuxtConfig } from "nuxt";
import en from "./content/pages/index.en.json";
import fr from "./content/pages/index.fr.json";

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
    locales: ["en", "fr"], // used in URL path prefix
    strategy: "prefix_except_default",
    defaultLocale: "en",
    vueI18n: {
      legacy: false,
      locale: "en",
      messages: { en, fr },
    },
  },
  buildAssetsDir: base + "/_nuxt/",
  app: {
    baseURL: base,
    buildAssetsDir: base + "/_nuxt/",
  },
});
