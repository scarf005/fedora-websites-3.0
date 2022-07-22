import { defineNuxtConfig } from "nuxt";

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
  buildAssetsDir: '/fedora-websites-3.0/_nuxt/',
  app: {
    baseURL: '/fedora-websites-3.0/',
    buildAssetsDir: '/fedora-websites-3.0/_nuxt/',
  },
});
