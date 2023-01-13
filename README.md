<a href="https://translate.fedoraproject.org/engage/fedora-websites-3-0/">
<img src="https://translate.fedoraproject.org/widgets/fedora-websites-3-0/-/svg-badge.svg" alt="Translation status" />
</a>

## Development: Getting Started

- This repository is a standard [`create-nuxt-app`](https://nuxt.com/docs) project.
- To edit the text/images of this site you do not need this guide, simply go to the [CMS](https://fedora.gitlab.io/websites-apps/fedora-websites/fedora-websites-3.0/admin/) once you have write access to this repository. Ask an admin for write access on discussion.fedoraproject.org. This content is pulled in with the [nuxt-content](https://www.npmjs.com/package/@nuxt/content) package.
- To edit translations, go to Fedora's [Weblate](https://translate.fedoraproject.org/projects/fedora-websites-3-0/#languages). Every change made there will generate a merge request into the /locales folder of this project, and once that's accepted the site will be rebuilt with the changes automatically. The translated locale/foo.json files are pulled in with the [nuxt-i18n](https://www.npmjs.com/package/@nuxtjs/i18n) package, fallback is English.

- To add a new page or a new component, clone this repository, change into the folder, and run:

  - `npm install`: to install the project dependencies
  - [`npm run dev`](https://v3.nuxtjs.org/api/commands/dev): to run a live development server on localhost:3000
  - [`npm run generate`](https://v3.nuxtjs.org/api/commands/generate): creates pre-rendered pages for static hosting in .output/public (this is what the CI does too)


- Static rendering: Templates are written in Vue, but most of the site is compiled down to simple HTML at build time on the CI - similar to static sites made with Jekyll or Hugo frameworks (this is signaled by the components being named [foo.server.vue](https://nuxt.com/docs/guide/directory-structure/components#server-components)). There are some exceptions where full Vue components are requried, like the navbar (where it was simpler to use Vue state) or the CoreOS downloads component (which pulls up-to-the-minute builds from CoreOS pipeline). These are named foo.vue, and are rendered on the client.

## Bug reporting

- Design questions and discussion: https://gitlab.com/fedora/design/team/wwwfpo-2022/-/issues
- Bugs (ie. logo squished on mobile) https://gitlab.com/fedora/websites-apps/fedora-websites/fedora-websites-3.0/-/issues
- Who's working on what: https://gitlab.com/groups/fedora/websites-apps/fedora-websites/-/boards/4623394



### Vue Training Videos for Fedora Websites developers

We have a two-part training video series that takes you from start to finish implementing front end components using Vue.js starting with one of our design mockups and finishing with code. Part 1 is complete and part 2 is in editing:

- [How to create vue components for the new Fedora Website - Part 1](https://peertube.linuxrocks.online/w/9c6NkDP8vLnH2eWgrWasaw)

---

## General Vue Setup

- vscode extensions:
  - [volar](https://github.com/johnsoncodehk/volar) (recommended to install from extensions menu)
  - [Steps to set up take over mode for better typescript support](https://github.com/johnsoncodehk/volar/discussions/471)
- [codium rpm alternative to vscode](https://gitlab.com/paulcarroty/vscodium-deb-rpm-repo)
  - For those who want to not use a microsoft code editor but still want the plugins **and** a functioning integrated terminal
- Or use vscode. Flatpak versions are generally fine as well, however the limited integrated terminal can cause issues
- [Check out the Vue Documentation for Vue syntax](https://vuejs.org/)

### Linting and Formating

- [eslint](https://eslint.org/)
- [prettier](https://prettier.io/)
- [eslint-prettier](https://github.com/prettier/eslint-config-prettier)

### Style and CSS

- [Tailwindcss editor setup](https://tailwindcss.com/docs/editor-setup)
- a postcss plugin is required if you use `<style lang="postcss"></style>` in your vue components
- [Check out Tailwind's Documentation for help](https://tailwindcss.com/)
