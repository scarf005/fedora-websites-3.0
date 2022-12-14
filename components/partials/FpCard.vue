<script setup>
import { mdparser } from "../../config/utilities";

const props = defineProps({
  title: {
    type: String,
    default: "Card Title",
  },
  description: {
    type: String,
    default:
      "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.",
  },
  image: {
    type: String,
    default: "assets/logos/fedora-blue.png",
  },
  link: {
    type: Object,
    default: {
      url: "#",
      text: "Button",
    },
  },
  imgOrderFirst: {
    type: Boolean,
    default: false,
  },
  centerAlign: {
    type: Boolean,
    default: false,
  },
});

let descriptionMd;
if (props.description) {
  descriptionMd = await mdparser(props.description);
}
</script>
<template>
  <article class="container m-4 flex flex-col justify-between md:max-w-xs">
    <h3
      class="px-2 text-2xl font-semibold text-fp-blue lg:px-0"
      :class="centerAlign ? 'text-center' : 'text-center md:text-start'"
    >
      {{ title }}
    </h3>
    <div>
      <ContentRenderer
        v-if="descriptionMd"
        class="lg:w-prose my-3 hidden w-11/12 break-words text-sm text-fp-gray-darkest sm:block lg:text-base"
        :class="centerAlign ? 'text-center' : 'text-center md:text-start'"
        tag="p"
        :value="descriptionMd"
      />
    </div>
    <FpImage
      :src="image"
      class="mx-auto my-4"
      :class="
        imgOrderFirst
          ? 'order-first w-24 md:w-36'
          : 'order-4 w-48 md:w-64 lg:w-full'
      "
    />

    <NuxtLink
      :to="link.url"
      class="mx-auto my-3 flex w-2/4 justify-center rounded-lg bg-fp-blue-light py-2 font-medium text-white sm:w-11/12"
      :class="centerAlign ? 'lg:w-prose' : 'lg-full'"
      >{{ link.text }}</NuxtLink
    >
  </article>
</template>
