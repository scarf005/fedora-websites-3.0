<script setup>
const props = defineProps({
  title: {
    type: String,
    default: "Section Title",
  },
  links: {
    type: Object,
  },
});

const mobileToggle = ref(false);
</script>

<template>
  <section>
    <header>
      <button
        class="flex w-full items-center justify-between transition duration-150 ease-in-out hover:bg-blue-200 sm:hidden"
        @click.prevent="mobileToggle = !mobileToggle"
      >
        <h4 class="text-2xl font-semibold">{{ title }}</h4>
        <div class="sm:hidden">
          <Icon name="fa6-solid:chevron-right" />
        </div>
      </button>
      <div class="hidden sm:block">
        <h4 class="text-2xl font-semibold">{{ title }}</h4>
      </div>
    </header>
    <ul :class="!mobileToggle ? 'hidden' : 'block'">
      <li v-for="link in links" :key="link.id">
        <FpLink :href="link.path" v-if="!link.i18n">{{ link.label }}</FpLink>
        <a
          v-if="link.i18n"
          :href="`${
            $config.app.baseURL.replace(new RegExp('/$'), '') + link.path
          }`"
        >
          {{ link.label }}
        </a>
      </li>
    </ul>
    <ul class="hidden sm:block">
      <li v-for="link in links" :key="link.id">
        <FpLink :href="link.path" v-if="!link.i18n">{{ link.label }}</FpLink>
        <a
          v-if="link.i18n"
          :href="`${
            $config.app.baseURL.replace(new RegExp('/$'), '') + link.path
          }`"
        >
          {{ link.label }}
        </a>
      </li>
    </ul>
  </section>
</template>
