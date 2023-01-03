<script setup>
let props = defineProps({
  sectionDescription: {
    required: true,
    type: String,
  },
});

let sectionDescriptionMd;
if (props.sectionDescription) {
  sectionDescriptionMd = await mdparser(props.sectionDescription);
}
</script>

<template>
  <section class="mx-auto bg-fp-blue-light/5">
    <div
      class="container mx-auto max-w-7xl px-8 py-12 text-center lg:px-0 lg:text-start"
    >
      <ContentRenderer
        tag="p"
        class="text-fp-gray-darkest"
        :value="sectionDescriptionMd"
      />
    </div>
  </section>
</template>
