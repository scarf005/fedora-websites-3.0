## Development: Getting Started

- This repository is a standard [`create-nuxt-app`](https://nuxt.com/docs) project.
- This guide is for making updates to the website code. If you are looking to update the content (text and/or images) of this site, you can use the [Content Management System](https://fedora.gitlab.io/websites-apps/fedora-websites/cms/fedoraproject.org/admin/) or you can submit merge requests to https://gitlab.com/fedora/websites-apps/fedora-websites/cms/fedoraproject.org.
  - To get write access to either repository (code or content), file a ticket [here](https://gitlab.com/fedora/websites-apps/fedora-websites/fedora-websites-3.0/-/issues/new?issuable_template=Collaborate&issue[title]=new%20collaborator%20request).
  - This content is pulled in with the [nuxt-content](https://www.npmjs.com/package/@nuxt/content) package.
- To add a new page or a new component, clone this repository, change into the folder, and run:

  - `npm install`: to install the project dependencies
  - [`npm run dev`](https://v3.nuxtjs.org/api/commands/dev): to run a live development server on localhost:3000
  - [`npm run generate`](https://v3.nuxtjs.org/api/commands/generate): creates pre-rendered pages for static hosting in .output/public (this is what the CI does too)

## Static site

Templates are written in Vue, but most of the site is compiled down to simple HTML at build time on the CI similar to static sites made with Jekyll or Hugo frameworks (with a few exceptions being rendered on the client using the full Vue client-side feature set listed in `nuxt.config.ts` like the CoreOS downloads page, etc.) with [these lines](https://gitlab.com/fedora/websites-apps/fedora-websites/fedora-websites-3.0/-/blob/develop/nuxt.config.ts#L87-92). Read up on experimentalNoScripts and routeRules on Nuxt for more info on this method. Note that currently, only pages one route deep are rendered fully-static like this, in order to avoid pages like /workstation/downloads which still need their JS. There is currently no way to _not_ render certain pages statically - conflicting routeRules seem to be simply ignored.

## Translations / i18n

- To edit translations, go to Fedora's [Weblate](https://translate.fedoraproject.org/projects/fedora-websites-3-0/fedoraproject-org/).
- For more information on nuxt-i18n, and how to add new strings to the project, please see (and update!) the [translation readme](https://gitlab.com/fedora/websites-apps/fedora-websites/fedora-websites-3.0/-/blob/develop/locales.build.d/README.md).
- To add a new language to the navbar/footer, please add it to the file `locales/locales.json`.

<a href="https://translate.fedoraproject.org/engage/fedora-websites-3-0/">
<img src="https://translate.fedoraproject.org/widgets/fedora-websites-3-0/-/fedoraproject-org/horizontal-auto.svg" alt="Translation status" />
</a>

## Bug reporting

- Design questions and discussion: https://gitlab.com/fedora/design/team/wwwfpo-2022/-/issues
- Bugs (ie. logo squished on mobile) https://gitlab.com/fedora/websites-apps/fedora-websites/fedora-websites-3.0/-/issues
- Who's working on what: https://gitlab.com/groups/fedora/websites-apps/fedora-websites/-/boards/4623394

## Training

We have a two-part training video series that takes you from start to finish implementing front end components using Vue.js starting with one of our design mockups and finishing with code. Part 1 is complete and part 2 is in editing:

- [How to create vue components for the new Fedora Website - Part 1](https://peertube.linuxrocks.online/w/9c6NkDP8vLnH2eWgrWasaw)

Other documentation:

- [How to contribute](https://gitlab.com/groups/fedora/websites-apps/fedora-websites/-/wikis/Contributor-Guidelines)
- [How to use Decap CMS](https://gitlab.com/fedora/websites-apps/fedora-websites/fedora-websites-3.0/-/wikis/Netlify-CMS)

## General Vue Setup

- vscode extensions:
  - [volar](https://github.com/johnsoncodehk/volar) (recommended to install from extensions menu)
  - [Steps to set up take over mode for better typescript support](https://github.com/johnsoncodehk/volar/discussions/471)
- [codium rpm alternative to vscode](https://gitlab.com/paulcarroty/vscodium-deb-rpm-repo)
  - For those who want to not use a microsoft code editor but still want the plugins **and** a functioning integrated terminal
- Or use vscode. Flatpak versions are generally fine as well, however the limited integrated terminal can cause issues
- [Check out the Vue Documentation for Vue syntax](https://vuejs.org/)

## Linting and Formating

- [eslint](https://eslint.org/)
- [prettier](https://prettier.io/)
- [eslint-prettier](https://github.com/prettier/eslint-config-prettier)

## Style and CSS

- [Tailwindcss editor setup](https://tailwindcss.com/docs/editor-setup)
- [Check out Tailwind's Documentation for help](https://tailwindcss.com/)

## Meeting Notes

- [HackMD](https://hackmd.io/Mxm2We3yTqKybLsdohadOA?both)

## License

This project is licensed under the [GNU Affero General Public License v3.0 only](LICENSE) (AGPL-3.0-only).
