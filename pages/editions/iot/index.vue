<script setup>
const { data } = await useAsyncData("page-data", () => {
  return queryContent("pages/editions/iot/home").find();
});

useHead({
  title: "Fedora IoT | The Fedora Project",
});
</script>
<template>
  <main>
    <FpHero :background="data[0].header.images.backgroundImage">
      <FpBanner
        :title="data[0].header.title"
        :subtitle="data[0].header.subtitle"
        :image="data[0].header.images.image"
        color="text-fp-purple"
        border="border border-fp-purple"
        background="text-white bg-fp-purple"
        :cta1="data[0].header.cta[0].text"
        :link1="data[0].header.cta[0].url"
        :cta2="data[0].header.cta[1].text"
        :link2="data[0].header.cta[1].url"
      />
    </FpHero>
    <FpHero :background="data[0].section[0].header.headerImage.image">
      <section class="w-10/12 pt-12 mx-auto">
        <h3
          class="text-fp-blue font-medium mb-4 xl:mb-6 md:col-span-2 xl:col-span-1"
        >
          {{ data[0].section[0].header.sectionTitle }}
        </h3>
        <FpList columns="sm:grid-cols-2 gap-12 lg:gap-4">
          <FpListItem
            v-for="item in data[0].section[0].content.list"
            v-bind="item"
          />
        </FpList>
      </section>
    </FpHero>
    <div class="bg-magenta-100" style="min-height: 60vh">
      <section class="w-10/12 mx-auto pt-12">
        <h3
          class="text-center text-fp-blue font-medium mb-4 xl:mb-6 md:col-span-2 xl:col-span-1"
        >
          {{ data[0].section[1].header.sectionTitle }}
        </h3>
        <FpList columns="sm:grid-cols-4 gap-12 lg:gap-4">
          <FpListItem
            v-for="item in data[0].section[1].content.list"
            v-bind="item"
          />
        </FpList>
      </section>
    </div>
    <FpHero :background="data[0].section[2].header.headerImage.image">
      <section class="w-10/12 mx-auto pt-12">
        <div class="w-1/2 mx-auto">
          <h2 class="text-center text-fp-blue mx-auto mb-5">
            {{ data[0].section[2].header.sectionTitle }}
          </h2>
          <h4 class="text-center text-fp-blue mx-auto mb-5">
            {{ data[0].section[2].header.subtitle1 }}
          </h4>
          <h6 class="text-center text-fp-blue mx-auto mb-8">
            {{ data[0].section[2].header.subtitle2 }}
          </h6>
        </div>

        <FpList columns="sm:grid-cols-2 gap-12 lg:gap-4">
          <FpListItem
            v-for="item in data[0].section[2].content.list"
            v-bind="item"
          />
        </FpList>
      </section>
    </FpHero>
  </main>
</template>
