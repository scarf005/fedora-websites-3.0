<script setup>
const props = defineProps({
  title: {
    type: String,
    default: "Become a Fedora Contributor",
  },
  description: {
    type: String,
    default: "Contact the Join SIG to start contributing",
  },
  link: {
    type: "Object",
  },
});
const descriptionMd = await mdparser(props.description);
</script>
<template>
  <aside class="container my-2 flex gap-2">
    <div>
      <h4
        class="mb-2 text-lg font-semibold text-fp-newblue-500 dark:text-gray-200"
      >
        {{ $t(title) }}
      </h4>
      <div>
        <ContentRendererMarkdown
          tag="p"
          class="markdown text-sm text-fp-gray-dark dark:text-fp-gray"
          :value="descriptionMd"
        />
        <NuxtLink
          v-if="link"
          :to="link.url"
          class="ml-2 text-sm text-fp-newblue-500 transition duration-100 ease-in-out hover:text-fp-newblue-700 hover:dark:text-fp-newblue-300"
          >{{ $t(link.text) }}</NuxtLink
        >
        <NuxtLink
          v-else
          to="https://docs.fedoraproject.org/en-US/fedora-join/"
          class="ml-2 text-sm text-fp-newblue-500 transition duration-100 ease-in-out hover:text-fp-newblue-700 hover:dark:text-fp-newblue-300"
          >{{ $t("Learn More") }}</NuxtLink
        >
      </div>
    </div>
    <Icon
      name="fa6-solid:door-open"
      class="order-first text-fp-newblue-500 dark:text-gray-200"
      size="1.5rem"
    />
  </aside>
</template>
