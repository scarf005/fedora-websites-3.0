<!-- vim:set ts=2 sw=2 et: -->

<script setup>
const { t } = useI18n();
const slots = useSlots();
const props = defineProps({
  link: {
    type: String,
  },
  title: {
    type: String,
  },
  subtitle: {
    type: String,
  },
  content: {
    type: Object,
  },
  iconname: {
    type: String,
  },
  iconsize: {
    type: String,
    default: "48",
  },
  avatar: {
    type: String,
  },
});

// keep the icon centered in its column
const padding = (48 - Math.min(48, parseInt(props.iconsize))) / 8;
const margin = 6 - padding;
</script>

<template>
  <div class="mb-6 p-6 xl:p-4 rounded-2xl bg-white dark:bg-gray-700">
    <h2 class="mb-8 text-2xl leading-none">
      <a
        :href="link"
        class="text-2xl font-semibold leading-none text-fp-newblue"
        >{{ $t(title) }}</a
      >
      <p v-if="subtitle" class="mb-6 font-semibold text-fp-newblue">
        ({{ $t(subtitle) }})
      </p>
    </h2>
    <div class="mb-6 grid grid-cols-1 gap-6 md:grid-cols-2 xl:grid-cols-1">
      <div v-if="content != null" v-for="c in content">
        <div
          class="flex items-center"
          :style="`margin-left: ${padding * 4}px;`"
        >
          <a :href="c.link.url" :class="`flex-none p-${padding}`">
            <img
              v-if="c.avatar"
              :src="c.avatar"
              class="h-12 w-12 rounded object-cover"
            />
            <Icon
              v-else-if="iconname"
              :name="iconname"
              :size="iconsize"
              class="text-fp-blue"
            />
          </a>
          <a
            :href="c.link.url"
            :style="`margin-left: ${margin * 4}px;`"
            class="max-h-12 overflow-hidden text-base font-semibold"
            >{{ c.link.text }}</a
          >
        </div>
      </div>
      <div v-else>
        <slot name="loneitem" />
      </div>
    </div>
    <div v-if="slots.footnote" class="whitespace-no-wrap text-right">
      <slot name="footnote" />
    </div>
  </div>
</template>
