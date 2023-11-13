<script setup>
const { t } = useI18n();
const slots = useSlots();
const props = defineProps({
  gpgs: {
    type: Object,
  },
});

function splitkey(key) {
  return key.match(/[\S]{1,4}/g) || [];
}
</script>

<template>
  <div
    class="container mx-auto grid max-w-max divide-y divide-dotted divide-fp-gray text-fp-gray dark:text-fp-gray-light"
  >
    <div v-for="gpg in gpgs" class="py-8">
      <h3 class="pb-3 text-center text-fp-blue sm:text-start">
        {{ gpg.name }}
      </h3>
      <div>
        <span class="font-bold">id:</span
        ><code class="ml-[1.25ex] text-xs text-fp-gray sm:text-base">{{
          gpg.id
        }}</code>
      </div>
      <div class="flex flex-wrap items-baseline">
        <span class="font-bold">Fingerprint:</span>
        <div
          class="ml-[1.25ex] inline relative text-xs text-fp-gray sm:text-base"
        >
          <code class="-ml-[1.25ex] absolute text-transparent">
            <span class="ml-[1.25ex]" v-for="kp in splitkey(gpg.fingerprint)">
              {{ kp }}
            </span>
          </code>
          <code class="-ml-[1.25ex] select-none">
            <span class="ml-[1.25ex]">
              {{ splitkey(gpg.fingerprint).join(" ") }}
            </span>
          </code>
        </div>
      </div>
      <div
        v-if="gpg.openpgpkey"
        class="flex flex-wrap items-baseline gap-x-[1.25ex]"
      >
        <span class="font-bold">DNS OpenPGPKey:</span
        ><code class="break-all text-xs text-fp-gray sm:text-base">{{
          gpg.openpgpkey
        }}</code>
      </div>
    </div>
  </div>
</template>
