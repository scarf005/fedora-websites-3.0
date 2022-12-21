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
});
const emit = defineEmits(["emitToggle"]);

const toggle = ref(false);

function useToggle() {
  toggle.value = !toggle.value;
  emit("emitToggle");
}
</script>
<template>
  <button
    @click="useToggle"
    class="text-white duration-300 ease-in-out hover:opacity-50"
  >
    <Icon v-if="toggle" :name="altIcon" size="32" />
    <Icon v-else :name="icon" size="32" />
  </button>
</template>
