<script setup>
const { locale } = useI18n();

let { data } = await useAsyncData("page-data", () => {
  return queryContent("/editions/coreos/community/" + locale._value).findOne();
});

if (data._value === null) {
  ({ data } = await useAsyncData("page-data-fallback", () => {
    return queryContent("/editions/coreos/community").sort().find();
  }));
  data._value = data._value[data._value.length - 1];
}

useContentHead(data);
</script>

<template>
  <main class="mt-4 border-t-8 border-fp-magenta">
    <header>
      <TheLocalBar
        image="assets/images/fedora-coreos-logo.png"
        home="/editions/coreos"
        :items="[
          { name: 'Download', link: '/editions/coreos/download' },
          { name: 'Community', link: '/editions/coreos/community' },
          { name: 'Help', link: '/editions/coreos/help' },
        ]"
      />
      <section class="my-8 mx-auto px-8 text-center lg:text-start xl:px-0">
        <div class="container mx-auto">
          <h1 class="mb-4 text-fp-magenta xl:mb-8">{{ data.title }}</h1>
          <p class="text-fp-gray">{{ data.description }}</p>
        </div>
      </section>
      <section class="mx-auto bg-fp-blue-light/5">
        <div
          class="container mx-auto px-8 py-12 text-center lg:px-0 lg:text-start"
        >
          <p class="text-fp-gray-darkest">
            {{ data.sections[0].sectionDescription }}
          </p>
        </div>
      </section>
    </header>
  </main>
</template>
