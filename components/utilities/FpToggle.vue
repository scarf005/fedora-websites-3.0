<script setup>
defineProps({
  icon: {
    type: String,
    default: "fa6-solid:bars",
  },
  altIcon: {
    type: String,
    default: "line-md:close",
  },
  iconToggle: {
    type: Boolean,
    default: false,
  },
});
const emit = defineEmits(["emitToggle"]);

function useToggle() {
  emit("emitToggle");
}
</script>
<template>
  <button
    @click="useToggle"
    class="text-white duration-300 ease-in-out hover:opacity-50"
  >
    <Icon v-if="iconToggle" :name="altIcon" size="32" />
    <Icon v-else :name="icon" size="32" />
  </button>
</template>
