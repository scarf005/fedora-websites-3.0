import locales from "./config/locales.json";
import path from "path";
const locales_ci = [
  { "code": "en", "language": "en", "file": "en.json", "name": "English" },
  { "code": "fr", "language": "fr", "file": "fr.json", "name": "Français" },
];
const base = process?.env?.CI_PAGES_URL
  ? new URL(process?.env?.CI_PAGES_URL +"/"+ process?.env?.PAGES_PREFIX).pathname
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

  content: {
    markdown: {
      anchorLinks: false,
    },
  },

  i18n: {
    locales: process?.env?.CI_FAST_BUILD ? locales_ci : locales,
    lazy: {
      skipNuxtState: true,
    },
    langDir: "./locales/",
    strategy: "prefix_and_default",
    defaultLocale: "en",
    vueI18n: './nuxt-i18n.js',
    compilation: {
      strictMessage: false,
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
        { src: path.join(base, "js/darkmode.js"), defer: true },
      ],
    },
  },

  hooks: {
    // "pages:extend"(pages) {
    //   if (process?.env?.CI_JOB_NAME == "build_preview") {
    //     pages.forEach((page) => {
    //       pages.push({
    //         name: `${page.name}-alias`,
    //         path:
    //           page.path.length > 1 ? `${page.path}/index.html` : "/index.html",
    //         redirect: page.path,
    //         file: page.file,
    //       });
    //     });
    //   }
    // },
   },

  nitro: {
    prerender: {
      concurrency: 1
    }
  },

  experimental: {
    inlineSSRStyles: false,
  },

  routeRules: {
    "*": { experimentalNoScripts: true }, // one level deep, render all pages statically
    "*/*/": { experimentalNoScripts: true }, // same, but for translated pages
    "*/download/": { experimentalNoScripts: false }, // except the download pages
    "atomic-desktops/": { experimentalNoScripts: true }, // no js on atomic-desktops home page
    "*/atomic-desktops/": { experimentalNoScripts: true }, // no js on atomic-desktops home page - translated
    "atomic-desktops/*/": { experimentalNoScripts: true }, // no js on atomic-desktops pages either
    "*/atomic-desktops/*/": { experimentalNoScripts: true }, // no js on atomic-desktops pages either - translated
    "spins/": { experimentalNoScripts: false }, // except the spins home page
    "*/spins/": { experimentalNoScripts: false }, // except the spins home page - translated
    "spins/*/": { experimentalNoScripts: false }, // except the spins pages
    "*/spins/*/": { experimentalNoScripts: false }, // except the spins pages - translated
    "labs/": { experimentalNoScripts: false }, // except the labs home page
    "*/labs/": { experimentalNoScripts: false }, // except the labs home page - translated
    "labs/*/": { experimentalNoScripts: false }, // except the labs pages
    "*/labs/*/": { experimentalNoScripts: false }, // except the labs pages - translated
    "*/community/" : { experimentalNoScripts: true }, // no js for community pages
    "*/*/community/" : { experimentalNoScripts: true }, // no js for community pages - translated
    "/coreos/download/": { experimentalNoScripts: false }, // except the download pages, where we need JS (coreOS images, or just GPG modal)
    "/coreos/release-notes/": { experimentalNoScripts: false }, // except release notes
    "/start": { experimentalNoScripts: false }, // except start pages
    "*/start": { experimentalNoScripts: false }, // except start pages - translated
    "/security": { experimentalNoScripts: false }, // except security page, for obsolete keys listing
    "*/security": { experimentalNoScripts: false }, // except security page, for obsolete keys listing - translated
  },

  compatibilityDate: "2024-10-27",
});
