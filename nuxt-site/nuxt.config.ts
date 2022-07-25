import { defineNuxtConfig } from "nuxt";

// https://v3.nuxtjs.org/api/configuration/nuxt.config
export default defineNuxtConfig({
  components: [
    "~/components/",
    "~/components/layout",
    "~/components/ui",
    "~/components/utilities",
  ],
  buildModules: [
    "@pinia/nuxt"
  ],
  modules: ["@nuxtjs/tailwindcss", "@nuxt/content"],
  // Plugin Configurations
  tailwindcss: {
    cssPath: "~/assets/css/main.css",
  },
});
