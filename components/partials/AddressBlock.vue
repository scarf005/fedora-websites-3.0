<script setup>
import FpLink from "../utilities/FpLink.vue";

const props = defineProps({
  name: String,
  street1: String,
  street2: String,
  city: String,
  state: String,
  postcode: String,
  country: String,
  url: String,
  phone_e164: String,
  phone: String,
});
</script>
<template>
  <address>
    <template v-if="name">
      <strong>
        <FpLink v-if="url" :href="url" class="underline">
          {{ name }}
        </FpLink>
        <template v-else="url">{{ name }}</template>
      </strong>
    </template>
    <br />{{ street1 }}
    <template v-if="street2"> <br />{{ street2 }} </template>
    <br />{{ city }}, {{ state }} <br />{{ postcode }} <br />{{ country }}
    <template v-if="phone && phone_e164">
      <br />Telephone:
      <FpLink :href="'tel:' + phone_e164" rel="nofollow">{{ phone }}</FpLink
      ><br />
    </template>
  </address>
</template>
