<script setup>
const switchLocalePath = useSwitchLocalePath();

const props = defineProps({
  title: {
    type: String,
    default: "Section Title",
  },
  links: {
    type: Object,
  },
});
</script>

<template>
  <div tabindex="1" class="footer-label">
    <div class="flex w-full cursor-default items-center justify-between">
      <div class="select-none text-2xl font-semibold whitespace-nowrap">
        {{ $t(title) }}
      </div>
      <div class="ltr:hidden md:hidden">
        <Icon name="fa6-solid:chevron-left" />
      </div>
      <div class="rtl:hidden md:hidden">
        <Icon name="fa6-solid:chevron-right" />
      </div>
    </div>
    <ul class="footer-links overflow-hidden h-0 md:h-fit md:block">
      <li v-for="link in links" :key="link.id">
        <FpLink :href="link.path" v-if="!link.code">{{
          $t(link.label)
        }}</FpLink>
        <a :href="switchLocalePath(link.code)" v-if="link.code">
          {{ link.name }}
        </a>
      </li>
    </ul>
  </div>
</template>

<style>
.footer-label:hover .footer-links,
.footer-label:focus .footer-links,
.footer-label:focus-within .footer-links {
  @apply h-fit;
}
.footer-links li:hover {
  @apply underline-offset-1 
  transition duration-150 ease-in-out 
  hover:text-fp-darkblue hover:underline 
  hover:dark:text-fp-newblue;
}
</style>
