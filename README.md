<a href="https://translate.fedoraproject.org/engage/fedora-websites-3-0/">
<img src="https://translate.fedoraproject.org/widgets/fedora-websites-3-0/-/svg-badge.svg" alt="Translation status" />
</a>

## Bugs:
- Design questions and discussion: https://gitlab.com/fedora/design/team/wwwfpo-2022/-/issues
- Bugs (ie. logo squished on mobile) https://gitlab.com/fedora/websites-apps/fedora-websites/fedora-websites-3.0/-/issues
- Who's working on what: https://gitlab.com/groups/fedora/websites-apps/fedora-websites/-/boards/4623394

## Development: Getting Started

This repository was set up on July 20 2022 as the team voted on Fedora's static frontend pages.

It is an off-the-shelf `create-nuxt-app` project.

Note: To edit the content of this site you do not need this guide - simply go to the CMS above. To develop new features or add new pages, read on.

- Clone this repository and run in the folder:

  - `npm install`: to install the project dependencies
  - [`npm run dev`](https://v3.nuxtjs.org/api/commands/dev): to run a live development server on localhost:3000
  - [`npm run generate`](https://v3.nuxtjs.org/api/commands/generate): creates pre-rendered pages for static hosting in .output/public (this is what the CI does too)

See also [nuxt configuration documentation](https://v3.nuxtjs.org/api/configuration/nuxt.config) - nuxt manages much of it's functionality inside the `nuxt.config.ts` file - and the [deployment documentation](https://v3.nuxtjs.org/guide/deploy/presets) for more information.

---

## General Vue Setup

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
