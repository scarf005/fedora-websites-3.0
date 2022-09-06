import { defineNuxtConfig } from "nuxt";

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
      '@fortawesome/fontawesome-svg-core',
      '@fortawesome/free-solid-svg-icons',
      '@fortawesome/free-regular-svg-icons',
      '@fortawesome/free-brands-svg-icons',
      '@fortawesome/vue-fontawesome'
    ]
  },
  buildModules: ["@pinia/nuxt"],
  modules: ["@nuxtjs/tailwindcss", "@nuxt/content"],
  tailwindcss: {
    cssPath: "~/assets/css/main.css",
  },
  buildAssetsDir: base + "/_nuxt/",
  app: {
    baseURL: base,
    buildAssetsDir: base + "/_nuxt/",
  },
});
