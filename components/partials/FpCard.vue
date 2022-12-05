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
});

let descriptionMd;
if (props.description) {
  descriptionMd = await mdparser(props.description);
}
</script>
<template>
  <article class="container m-4 flex flex-col justify-between md:max-w-xs">
    <h3
      class="px-2 text-center text-2xl font-semibold text-fp-blue md:text-start lg:px-0"
    >
      {{ title }}
    </h3>
    <div>
      <ContentRenderer
        v-if="descriptionMd"
        class="mx-auto mt-2 hidden w-11/12 break-words text-center text-sm text-fp-gray-darkest sm:block md:text-start lg:w-80 lg:text-base"
        tag="p"
        :value="descriptionMd"
      />
    </div>
    <FpImage :src="image" class="mx-auto my-4 w-48 md:w-64 lg:w-full" />

    <NuxtLink
      :to="link.url"
      class="mx-auto flex w-2/4 justify-center rounded-lg bg-fp-blue-light py-2 font-medium text-white sm:w-11/12 lg:w-full"
      >{{ link.text }}</NuxtLink
    >
  </article>
</template>
