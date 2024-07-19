<script setup>
const props = defineProps({
  activities: Array[Object],
});
function dateToParts(iso_datetime_str, locale = "en-us") {
  const date = new Date(iso_datetime_str);
  return {
    dayofweek: date.toLocaleString(locale, { weekday: "short" }),
    day: date.getDay(),
    month: date.toLocaleString(locale, { month: "short" }),
  };
}
</script>
<template>
  <div class="mx-auto flex flex-wrap justify-center max-w-screen-xl p-12">
    <div
      v-for="activity in activities"
      class="max-w-[17rem] rounded-lg flex flex-col dark:bg-black/70 bg-white/70 p-4 m-4"
    >
      <!-- <FpImage 
            class="inline h-10 max-w-none align-baseline ltr:mr-1 rtl:ml-1"
            :src="activity.image.url"
            v-if="activity.image.url"
          /> -->
      <div class="flex mb-2">
        <FlDateBox v-bind="dateToParts(activity.date)" />
        <div class="mx-4">
          <span class="text-xl font-bold leading-none text-fp-blue">
            {{ $t(activity.title) }}
          </span>
          <div
            class="text-lg font-italic leading-none text-fp-blue"
            v-if="activity.subtitle"
          >
            {{ $t(activity.subtitle) }}
          </div>
        </div>
      </div>
      <p
        class="text-sm dark:text-slate-300 text-slate-800 m-2"
        v-if="activity.description"
      >
        {{ $t(activity.description) }}
      </p>
      <div class="grow"></div>
      <FpBtn
        :href="activity.link.url"
        v-if="activity.link.text != ''"
        class="mx-auto"
      >
        {{ activity.link.text }}
      </FpBtn>
    </div>
  </div>
</template>
