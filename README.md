# fedora-websites-3.0

- Test deployed at: https://fedora.gitlab.io/websites-apps/fedora-websites/fedora-websites-3.0/
- Netlify CMS to edit content: https://fedora.gitlab.io/websites-apps/fedora-websites/fedora-websites-3.0/admin

---

## Development: Getting Started

Note: To edit the content of this site you do not need this guide. Simply go to the CMS above. To develop new features or add new pages, read on.

This repository was set up on July 20th as the team voted on Fedora's static frontend pages. It runs on the principles of basic `create-nuxt-app` CLI commands.

- Clone this repository and run in the folder:

  - `npm install`: to install the project dependencies
  - [`npm run dev`](https://v3.nuxtjs.org/api/commands/dev): to run a live development server on localhost:3000
  - [`npm run generate`](https://v3.nuxtjs.org/api/commands/generate): creates pre-rendered pages for static hosting in .output/public (this is what the CI does too)

See also [nuxt configuration documentation](https://v3.nuxtjs.org/api/configuration/nuxt.config) - nuxt manages much of it's functionality inside the `nuxt.config.ts` file - and the [deployment documentation](https://v3.nuxtjs.org/guide/deploy/presets) for more information.

---

- Upcoming Major Tasks:
  - Outline contributor guidelines
  - Set up team roles
  - Assign Tasks

---

## General Vue Setup Stuff

- vscode extensions:
  - [volar](https://github.com/johnsoncodehk/volar) (recommended to install from extensions menu)
  - [Steps to set up take over mode for better typescript support](https://github.com/johnsoncodehk/volar/discussions/471)
- [codium rpm alternative to vscode](https://gitlab.com/paulcarroty/vscodium-deb-rpm-repo)
  - For those who want to not use a microsoft code editor but still want the plugins **and** a functioning integrated terminal
- Or use vscode. Flatpak versions are generally fine as well, however the limited integrated terminal can cause issues
- [Check out the Vue Documentation for Vue syntax](https://vuejs.org/)
- For Nuxt particular details, [View the Nuxt 3 Documentation](https://v3.nuxtjs.org/guide/concepts/introduction)

### Linting and Formating

- [eslint](https://eslint.org/)
- [prettier](https://prettier.io/)
- [eslint-prettier](https://github.com/prettier/eslint-config-prettier)

### Style and CSS

- [Tailwindcss editor setup](https://tailwindcss.com/docs/editor-setup)
- a postcss plugin is required if you use `<style lang="postcss"></style>` in your vue components
- [Check out Tailwind's Documentation for help](https://tailwindcss.com/)

---

## Vanilla Vue Setup and Usage

This is the original project folder

- cd into `client/`
- run `npm install` to install packages
- run `npm run dev` for a live development server
- to clean up formatting, run `npm run format` to clean up all files (except node_modules)
- the linter is giving a parsing error for unexpected token. This doesn't seem to be effecting anything and is likely a configuration issue.
- This was set up prior to creating the Nuxt version. Some of the filename conventions are a bit different and more generic.
  - It still uses file based routing, however components need to be imported
  - use `@vueuse/head` plugin for handling page metadata
