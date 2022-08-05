<script setup>
// pull data from the content directory like this
const { data } = await useAsyncData("page-data", () => {
  return queryContent("pages/editions/iot/home").find();
});
</script>
<template>
  <main>
    <FpHero :background="data[0].header.images.backgroundImage">
      <div class="mt-16 mx-auto max-w-7xl px-4 sm:mt-24 sm:px-6 text-center">
        <h1 class="text-6xl tracking-tight text-white">
          <span class="block">{{ data[0].header.title }}</span>
        </h1>
        <p class="mt-3 mx-auto text-3xl text-white">
          {{ data[0].header.subtitle }}
        </p>
      </div>

      <div class="flex justify-center my-5">
        <FpImage :image="data[0].header.images.image"/>
      </div>

       <div class="mt-5 flex justify-end px-4 sm:-mt-32 sm:mb-24">
        <a class="mx-2 px-12 py-4 z-10 cursor-pointer font-semibold text-magenta">
          Watch the latest reviews ➔
        </a>
      </div>

      <div class="mt-5 flex px-4">
        <button class="mx-2 shadow bg-purple sm:px-12 sm:py-4 z-10">
          Download Now
        </button>
        <button
          class="mx-2 shadow bg-white border border-purple text-purple sm:px-12 sm:py-4 z-10"
        >
          <font-awesome-icon icon="fa-brands fa-youtube" />
          Reviewed by Reviewer
        </button>
      </div>
      
    </FpHero>
  </main>
</template>
