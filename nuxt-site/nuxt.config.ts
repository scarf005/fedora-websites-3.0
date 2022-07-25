import { defineNuxtConfig } from "nuxt";

const base = process.env.CI_PAGES_URL ? new URL(process.env.CI_PAGES_URL).pathname : ''

// https://v3.nuxtjs.org/api/configuration/nuxt.config
export default defineNuxtConfig({
  css: [
    "@fortawesome/fontawesome-svg-core/styles.css"
  ],
  components: [
    "~/components/",
    "~/components/layout",
    "~/components/ui",
    "~/components/utilities",
  ],
  buildModules: ["@pinia/nuxt"],
  // TODO: Finish configuring Strapi to set up with this repo
  modules: ["@nuxtjs/tailwindcss", /* "@nuxtjs/strapi" */],
  // Plugin Configurations
  tailwindcss: {
    cssPath: "~/assets/css/main.css",
  },
  buildAssetsDir: base + '/_nuxt/',
  app: {
    baseURL: base,
    buildAssetsDir: base + '/_nuxt/',
  },
});
