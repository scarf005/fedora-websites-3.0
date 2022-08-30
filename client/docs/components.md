# Components

_This file outlines how to make the best use of components as well as tips on editing them_

## July 8 Component Building Notes

Today I (lilyx) took a macro approach to our components. Starting by drafting out the content needed on the **workstation** page - My focus at this stage is to determine the most productive and consistent workflow for component usage - **workflow 1**: Simplest components: - dynamic content passed as a prop - static text is slotted - **would feel like using an `<a></a>` tag** - **workflow 2**: Looped components such as lists: - pass an array of information to the component - component generates multiple child elements based on the arrays and objects passed into it - slots used for content that doesn't quite fit the majority use cases - **takes advantage of `v-for` syntax and ability to pass lists of info, reduced html editing later** - **workflow 3**: Complex components (cards, heros) - Named slots are used for sections (I think if there's 3+ rows in a component, this is a good time for this configuration - Background content is passed as a prop - Component is utilitiy focused, focusing on how the elements are aligned at different screen sizes - Named slots allow for a diverse amount of layout changes - ie: in the hero sections, we currently have 3 ways that buttons are positioned, slotted styles can give us default options with each named slot to account for variation while still maintaining standardized ways of doing things

## July 15 Component Building Notes

- `TheMain.vue` is used on each page to wrap the page content, style wise this is to address outer level unchangable css to make it responsive
  - this component is also given logic for handling page metadata to reduce code redunancy. Metadata info will be able to be written on each page and passed to the main component. They are computed properties because they don't need to be changed or anything.
- `AppList.vue`: I was unsure of the best way to handle this. Creating a AppUnorderedList and AppOrderedList felt unnecessary and confusing, so to remedy this situation, I want to use a generic applist component that makes use of `v-if/v-else` where a keyword is set to determine the type of list it creates
  - **I think this could be a reproduced strategy for other components such as `AppBtn` to reduce the amount of code.**
    - if we can have one way of handling this sort
- `utilities/text`: We are starting to use a lot of gradients on title texts. I think we should have a specially defined set up text utilities to handle these particular use cases.
  - [Vuetify](https://vuetifyjs.com/en/styles/text-and-typography/) has an example that uses a class based approach. I propose that we make a couple custom components that have predefined gradient classes that can be set
    - this would look like:
      - `TextCaption.vue`
      - `TextDisplay.vue`

## July 19

- After looking further at other UI kits and considering our generic components. I think that we would benefit from using the prefix `f` instead of `app`
  - benefits:
    - less typing
    - leaner naming convention
    - looks cool
    - f is for fedora ==> good branding if we ever deploy this as our own component library
    - clearly defines our components from general html components (`f-nav` vs `nav` vs `app-nav`)
  - downsides:
    - less common convention
- At this stage, it would take a very short amount of time to make a change like this, but within a week this would become a pain in the butt
