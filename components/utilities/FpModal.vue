<script setup>
const props = defineProps({
  show: {
    type: Boolean,
    default: false,
  },
});
const verifyModal = useState("verifyModal");
</script>
<template>
  <div class="fixed inset-0 z-10 overflow-y-auto">
    <div class="flex min-h-full items-center justify-center text-center sm:p-4">
      <!-- backdrop overlay -->
      <div
        class="fixed inset-0 bg-white/40 backdrop-blur-md dark:bg-black/50"
        @click="verifyModal.show = false"
      ></div>
      <!-- modal -->
      <div
        class="relative w-full transform overflow-hidden rounded-md border bg-white text-left text-black shadow-xl transition-all dark:border-gray-600 dark:bg-neutral-900 dark:text-gray-300 sm:my-8 sm:max-w-3xl"
      >
        <div class="flex flex-col justify-between">
          <header class="border-b p-3 dark:border-gray-600">
            <slot name="header">
              <h5>Title</h5>
            </slot>
          </header>
          <div class="p-3"><slot /></div>
          <footer class="flex justify-end border-t p-3 dark:border-gray-600">
            <slot name="footer">
              <button
                @click="verifyModal.show = false"
                class="rounded bg-fp-blue-light py-1 px-2 text-sm text-white hover:bg-fp-blue"
              >
                Close
              </button>
            </slot>
          </footer>
        </div>
      </div>
    </div>
  </div>
</template>
