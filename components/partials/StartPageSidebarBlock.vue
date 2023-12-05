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
  pulsers: {
    type: String,
    default: "0",
  },
});

// keep the icon centered in its column
const padding = (48 - Math.min(48, parseInt(props.iconsize))) / 8;
</script>

<template>
  <div class="mb-6 p-6 xl:p-4 rounded-2xl bg-white dark:bg-gray-700">
    <h2 class="mb-8 text-2xl leading-none">
      <a
        target="_blank"
        :href="link"
        class="text-2xl font-semibold leading-none text-fp-newblue"
        >{{ $t(title) }}</a
      >
      <p v-if="subtitle" class="mb-6 font-semibold text-fp-newblue">
        ({{ $t(subtitle) }})
      </p>
    </h2>
    <div
      v-if="content != null"
      :class="`grid grid-cols-1 md:grid-cols-2 xl:grid-cols-1 gap-x-6 ${
        pulsers != '0' ? 'sp_static' : ''
      }`"
    >
      <div
        v-for="c in content"
        class="mb-6 hover:bg-gray-100 dark:hover:bg-gray-600 rounded-xl"
      >
        <div class="flex items-center">
          <a
            target="_blank"
            :href="c.link.url"
            :class="`flex-none p-${padding}`"
          >
            <img
              v-if="c.avatar"
              :src="c.avatar"
              class="h-12 w-12 rounded object-cover"
            />
            <Icon
              v-else-if="iconname"
              :name="iconname"
              :size="iconsize"
              class="text-fp-blue rtl:-scale-x-100"
            />
          </a>
          <a
            target="_blank"
            :href="c.link.url"
            class="ltr:ml-6 rtl:mr-6 max-h-12 overflow-hidden text-base font-semibold"
            >{{ c.link.text }}</a
          >
        </div>
      </div>
    </div>
    <div v-else>
      <div class="mb-6">
        <slot name="loneitem" />
      </div>
    </div>
    <ClientOnly>
      <div
        v-if="content != null && content.length > 0"
        v-show="pulsers != '0'"
        class="grid grid-cols-1 md:grid-cols-2 xl:grid-cols-1 gap-x-6"
      >
        <div
          v-for="c in content"
          class="mb-6 hover:bg-gray-100 dark:hover:bg-gray-600 rounded-xl"
        >
          <div class="flex items-center">
            <a
              target="_blank"
              :href="c.link.url"
              :class="`flex-none p-${padding}`"
            >
              <img
                v-if="c.avatar"
                :src="c.avatar"
                class="h-12 w-12 rounded object-cover"
              />
              <Icon
                v-else-if="iconname"
                :name="iconname"
                :size="iconsize"
                class="text-fp-blue rtl:-scale-x-100"
              />
            </a>
            <a
              target="_blank"
              :href="c.link.url"
              class="ltr:ml-6 rtl:mr-6 max-h-12 overflow-hidden text-base font-semibold"
              >{{ c.link.text }}</a
            >
          </div>
        </div>
      </div>
      <div
        v-else-if="pulsers != '0'"
        class="grid grid-cols-1 md:grid-cols-2 xl:grid-cols-1 gap-x-6"
      >
        <div v-for="p in parseInt(pulsers)" class="mb-6">
          <div class="flex">
            <div
              class="h-12 w-12 rounded inline-block startpage-stripes opacity-25 dark:opacity-10"
            ></div>
            <div
              class="h-12 flex-1 ltr:ml-6 rtl:mr-6 inline-block startpage-stripes opacity-25 dark:opacity-10"
            ></div>
          </div>
        </div>
      </div>
      <template #fallback>
        <div
          v-show="pulsers != '0'"
          class="grid grid-cols-1 md:grid-cols-2 xl:grid-cols-1 gap-x-6"
        >
          <div
            v-for="p in parseInt(pulsers)"
            class="mb-6 sp_pulser_container hidden"
          >
            <div class="flex animate-pulse">
              <div
                class="h-12 w-12 rounded bg-gray-400 dark:bg-gray-500 inline-block"
              ></div>
              <div
                class="h-12 flex-1 ltr:ml-6 rtl:mr-6 bg-gray-400 dark:bg-gray-500 inline-block"
              ></div>
            </div>
          </div>
        </div>
      </template>
    </ClientOnly>
    <div
      v-if="slots.footnote"
      class="whitespace-no-wrap text-right hover:bg-gray-100 dark:hover:bg-gray-600 rounded-xl"
    >
      <slot name="footnote" />
    </div>
  </div>
</template>

<style scoped>
a {
  cursor: default;
}

/* css-tricks.com/stripes-css */
.startpage-stripes {
  color: black;
  background: repeating-linear-gradient(
      135deg,
      transparent,
      transparent 10px,
      #aaa 10px,
      #aaa 20px
    ),
    linear-gradient(to bottom, #eee, #555);
}
</style>
