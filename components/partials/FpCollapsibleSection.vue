<script setup>
defineProps({
  title: String,
  navItems: Array,
  use: String,
});
</script>
<template>
  <section>
    <div
      class="ml-6 mb-2 mr-6 flex cursor-pointer items-start justify-between md:ml-0 md:mr-0 lg:mb-4"
      :onclick="`togglenav('${title + use}')`"
    >
      <h6
        :class="`justify-start font-semibold ${
          use === 'nav' ? 'text-fp-gray-lightest' : 'text-fp-gray-darkest'
        } dark:text-fp-gray-light md:justify-start lg:font-bold`"
      >
        {{ title }}
      </h6>

      <Icon
        name="fa6-solid:chevron-right"
        v-bind:id="title + use + 'chevron'"
        size="24"
        :class="`${
          use === 'nav' ? 'text-fp-gray-lightest' : 'text-fp-gray-darkest'
        } rotate-90 transition md:invisible`"
      />
    </div>
    <ul class="ml-6 hidden md:ml-0 md:block" v-bind:id="title + use">
      <li v-for="item in navItems" :key="item.id" class="mb-4 list-none">
        <NuxtLink
          :to="item.href"
          :class="`text-base font-medium ${
            use === 'nav' ? 'text-fp-gray-lightest' : 'text-fp-gray-darkest'
          } dark:text-fp-gray`"
        >
          {{ item.name }}
        </NuxtLink>
      </li>
    </ul>
  </section>
</template>
