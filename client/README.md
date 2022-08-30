# Fedora Websites 3.0

## Component Conventions

Here are some conventions that are currently being established. This is of course not the only, or even possibly the best way to do these things, but they are being outlined here so that they can be observed, critiqued, and improved upon without leaving any rogues out there.

### Props and Slots in General

- tags that take text have text all passed in a slot (ie: AppLink or Display1)
  - however for any urls, the prop keyword is `to`, this is to mimic the behaviour in the vue router `<router-link to='/'>...</router-link>`

### Variations of the Same Element

- Variations of the same element are managed within the component, ie: there is 1 `AppBtn.vue` which should be able to have keywords to set whether it is a `solid`, `outline`, or `arrow` button (the three in use)
  - This can also be seen in the idea for `TextDisplay` (I'm not sold on that name because it's being used specifically for gradients and big display texts... but we can figure that out).

### layout components

- While i started by calling this directory layout, it might be better suited as 'content' or something.
  - Looking at component libraries such as Vuetify and Fast, they avoid creating actual true layout components in the way that BootstrapVue and Inkline do. While this could be useful, I have found that it really gets in the way and agree with the decision of Fast and Vuetify to not include these types of components.
    - For that stuff, we should be able to rely on our css framework, whether it be tailwind, bootstrap, or vanilla, to manage this stuff.
      - This will make it so that structuring a page does not require specialized knowledge of our system. The components are only for maintaining adherence to our element focused styles. For layout, we should be able to remain flexible and leverage the power of css to handle that.
- ***

## Recommended IDE Setup

- [VS Code](https://code.visualstudio.com/) + [Volar](https://marketplace.visualstudio.com/items?itemName=Vue.volar)

## Type Support For `.vue` Imports in TS

Since TypeScript cannot handle type information for `.vue` imports, they are shimmed to be a generic Vue component type by default. In most cases this is fine if you don't really care about component prop types outside of templates. However, if you wish to get actual prop types in `.vue` imports (for example to get props validation when using manual `h(...)` calls), you can enable Volar's Take Over mode by following these steps:

1. Run `Extensions: Show Built-in Extensions` from VS Code's command palette, look for `TypeScript and JavaScript Language Features`, then right click and select `Disable (Workspace)`. By default, Take Over mode will enable itself if the default TypeScript extension is disabled.
2. Reload the VS Code window by running `Developer: Reload Window` from the command palette.

You can learn more about Take Over mode [here](https://github.com/johnsoncodehk/volar/discussions/471).
