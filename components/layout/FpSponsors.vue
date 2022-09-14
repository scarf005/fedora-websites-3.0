<script setup>
defineProps({
  sponsors: {
    name: String,
    imageURI: String,
    level: String,
    description: String,
  },
});

function sponsorClass(sponsor) {
  let classList = "";
  switch(sponsor.level) {
    case "platinium": classList = "bg-gray-100 col-span-4"; break;
    case "gold": classList = "bg-gray-100 col-span-3"; break;
    case "silver": classList = "bg-gray-100 col-span-2"; break;
    case "bronze": classList = "bg-gray-100"; break;
    case "media": classList = "bg-slate-100"; break;
    default: classList = "bg-gray-50";
  }
  return classList;
};
</script>

<template>
  <div class="flex-wrap md:flex-nowrap grid-none md:grid grid-cols-1 md:grid-cols-4 md:grid-flow-dense gap-4 mt-10 justify-items-stretch text-gray-500 mx-0 lg:mx-10">

    <div v-for="sponsor in sponsors" class="grid text-xs text-center h-48 p-8 content-center relative" :class="sponsorClass(sponsor)">
      <template v-if="sponsor.level != 'placeholder'">
      <img 
	v-if="sponsor.imageURI"
        class="object-contain mx-auto w-full max-h-32" 
        :src="`${$config.app.baseURL + '/' + sponsor.imageURI.replace('public/', '')}`"
      />
      <p v-else>{{ sponsor.name }}</p>
      <p class="text-xs capitalize absolute bottom-2.5 inset-x-0">{{ sponsor.level }} sponsor</p>
      </template>
    </div>

    <div class="media text-xs text-center h-48 bg-violet-300 align-middle p-8 content-center grid">
      <p class="text-3xl text-black">Become a Sponsor</p>
    </div>

  </div>
</template>
