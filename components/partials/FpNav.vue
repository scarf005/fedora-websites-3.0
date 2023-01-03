<script setup>
const props = defineProps({
  global: { type: Boolean, default: false },
  home: {
    type: Object,
    default() {
      return {
        url: "/",
        label: "",
      };
    },
  },
  navLinks: {
    type: Object || Array,
  },
  textColor: {
    type: String,
    default: "text-white",
  },
});
</script>
<template>
  <nav>
    <!-- Home Link for Local Navigation -->
    <div v-if="!global">
      <NuxtLink :to="home.url" class="font-display text-xl font-semibold"
        >{{ home.label.toUpperCase() }}
      </NuxtLink>
    </div>
    <ul class="flex gap-4 text-white">
      <li v-for="link in navLinks" :key="link.id">
        <!-- Event Listener -->
        <button @click.prevent="emitToggle" v-if="global">
          <div class="lg:hidden">
            <Icon :name="link.icon" size="32" />
          </div>
          <p>{{ link.label }}</p>
        </button>
        <!-- No Event Listener-->
        <NuxtLink
          v-else
          :to="link.url"
          class="block p-2 text-center hover:opacity-75"
          :class="textColor"
        >
          <span class="lg:hidden">
            <Icon :name="link.icon" size="32" />
          </span>
          <span>{{ link.label }}</span>
        </NuxtLink>
      </li>
    </ul>
    <slot></slot>
  </nav>
</template>
