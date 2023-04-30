import locales from "./config/locales.json";
import path from "path";
const base = process?.env?.CI_PAGES_URL
  ? new URL(process?.env?.CI_PAGES_URL).pathname
  : "/";

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
    lazy: {
      skipNuxtState: true,
    },
    langDir: "./locales/",
    strategy: "prefix_and_default",
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
      link: [
        {
          rel: "me",
          href: "https://fosstodon.org/@fedora",
        },
        {
          rel: "icon",
          type: "image/x-icon",
          href: "/favicon.ico",
        },
      ],
      script: [
        {
          src: path.join(base, "js/navbar.js"),
          defer: true,
        },
        { src: path.join(base, "js/darkmode.js"), defer: true },
      ],
    },
  },
  hooks: {
    "pages:extend"(pages) {
      if (process?.env?.CI) {
        pages.forEach((page) => {
          pages.push({
            name: `${page.name}-alias`,
            path:
              page.path.length > 1 ? `${page.path}/index.html` : "/index.html",
            redirect: page.path,
            file: page.file,
          });
        });
      }
    },

    "build:manifest"(manifest) {
      for (const key in manifest) {
        manifest[key].dynamicImports = [];
        manifest[key].imports = [];
      }
    },
  },
  routeRules: {
    "/*": { experimentalNoScripts: true },
    "/coreos/download": { experimentalNoScripts: false },
    "/start": { experimentalNoScripts: false },
  },
});
