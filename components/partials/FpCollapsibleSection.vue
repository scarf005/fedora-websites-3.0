<script setup>
defineProps({
  title: String,
  navItems: Array,
  use: String,
});
const open = useState("collapseopen" + Math.random(), () => false);
</script>

<template>
  <section>
    <div
      class="ml-6 mb-2 mr-6 flex cursor-pointer items-start justify-between md:ml-0 md:mr-0 lg:mb-4"
      @click="open = !open"
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
        size="24"
        :class="`${
          use === 'nav' ? 'text-fp-gray-lightest' : 'text-fp-gray-darkest'
        } ${!open && 'rotate-90'} transition md:invisible`"
      />
    </div>
    <ul :class="`ml-6 ${!open && 'hidden'} md:ml-0 md:block`">
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
