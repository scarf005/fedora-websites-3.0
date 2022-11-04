import locales from "./locales/locales.json"

const base = process?.env?.CI_PAGES_URL
  ? new URL(process?.env?.CI_PAGES_URL).pathname
  : ""

// https://v3.nuxtjs.org/api/configuration/nuxt.config
export default defineNuxtConfig({
  components: [
    "~/components/",
    "~/components/layout",
    "~/components/ui",
    "~/components/utilities",
  ],
  modules: [
    "@nuxtjs/tailwindcss",
    "@nuxt/content",
    "@nuxtjs/i18n",
    "nuxt-icons",
  ],
  tailwindcss: {
    viewer: false,
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
    head: {
      titleTemplate: "%s | The Fedora Project",
    },
  },
})
