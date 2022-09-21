<script setup></script>
<template>
  <header class="p-12">
    <nav class="flex flex-wrap items-center justify-between pb-16">
      <NuxtLink to="#" class="flex"
        ><img
          src="/assets/logos/fedora-blue.png"
          alt="Fedora"
          style="height: 36px"
          class="mt-0.5"
        />
        <span
          class="text-blue-dark pl-2 font-display text-2xl font-medium uppercase leading-loose tracking-normal"
          >IoT</span
        ></NuxtLink
      >
      <ul class="flex flex-wrap items-center gap-x-12">
        <li>
          <NuxtLink
            class="text-blue-light underline-offset-8 hover:underline"
            to="#"
            >Download</NuxtLink
          >
        </li>
        <li>
          <NuxtLink
            class="text-blue-light font-bold underline-offset-8 hover:underline"
            to="#"
            >Community</NuxtLink
          >
        </li>
        <li>
          <NuxtLink
            class="text-blue-light underline-offset-8 hover:underline"
            to="#"
            >Get Help</NuxtLink
          >
        </li>
        <li>
          <NuxtLink
            class="text-blue-light underline-offset-8 hover:underline"
            to="#"
            >Get Started</NuxtLink
          >
        </li>
      </ul>
    </nav>
    <section>
      <h2 class="text-purple pb-3">Community</h2>
      <p class="text-gray ml-1">
        Join a community of users and contributors focused on Fedora IoT.
      </p>
    </section>
  </header>
  <p>{{ $route.fullPath }}</p>
</template>
