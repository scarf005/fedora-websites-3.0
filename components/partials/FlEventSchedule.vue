<script setup>
import locales from "../../config/locales.json";
const { locale } = useI18n();

const props = defineProps({
  activities: Array[Object],
});
function dateToParts(iso_datetime_str, locale = "en-US") {
  //strip the time (and thus also the UTC-ness. unsure why its coming through as a UTC time but whatever)
  let datetime_str = iso_datetime_str.split("T")[0];
  // We need to convert this into something that doesnt look like ISO
  // or javascript will use an ISO parser, which will assume UTC, even though we explicitly removed it
  //per https://stackoverflow.com/a/31732581/
  datetime_str = datetime_str.replace(/-/g, "\/");
  const date = new Date(datetime_str);
  return {
    dayofweek: date.toLocaleString(locale, { weekday: "short" }),
    day: date.getDate(),
    month: date.toLocaleString(locale, { month: "short" }),
  };
}
let code = locales.find((l) => l.code == locale._value).iso;
</script>
<template>
  <div class="mx-auto flex flex-wrap justify-center max-w-screen-xl p-12">
    <div
      v-for="activity in activities"
      class="max-w-[17rem] rounded-lg flex flex-col dark:bg-black/70 bg-slate-200/70 p-4 m-4"
    >
      <!-- <FpImage 
            class="inline h-10 max-w-none align-baseline ltr:mr-1 rtl:ml-1"
            :src="activity.image.url"
            v-if="activity.image.url"
          /> -->
      <span
        class="text-[1.35rem] text-center font-bold text-fp-blue dark: text-fp-newblue"
      >
        {{ $t(activity.title) }}
      </span>
      <div
        class="text-lg font-italic text-center leading-none text-fp-blue"
        v-if="activity.subtitle"
      >
        {{ $t(activity.subtitle) }}
      </div>
      <FlDateBox v-bind="dateToParts(activity.date, code)" />
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
