<template>
  <section
    class="bg-gradient-to-b from-white to-fp-newblue-100 py-12 dark:from-fp-darkblue-500 dark:to-neutral-900 md:py-36"
  >
    <div
      class="container mx-auto flex max-w-7xl flex-row flex-wrap justify-center gap-16 lg:flex-nowrap"
    >
      <div
        class="flex w-[200px] flex-none shrink items-center justify-center sm:shrink-0 md:w-[400px]"
      >
        <FpImage class="max-h-96" src="public/assets/images/panda_404.png" />
      </div>
      <div class="max-w-sm">
        <h2
          class="text-center text-8xl leading-none text-fp-newblue-500 md:text-[7rem]"
        >
          404
        </h2>
        <p
          class="mb-10 text-center font-display text-xl font-normal leading-none text-fp-newblue-500 md:text-5xl"
        >
          {{ $t("Page not found") }}
        </p>
        <p
          class="mb-16 text-center text-xl text-fp-gray-400 dark:text-fp-gray-200"
        >
          {{ $t("We think Panda lost it.") }}
        </p>
        <p class="text-center">
          <FpLink
            href="/"
            class="rounded-md bg-fp-newblue-500 px-6 py-2 text-xl font-medium text-white duration-300 ease-in-out hover:bg-fp-blue dark:bg-fp-darkblue-500 dark:hover:bg-fp-blue"
            >{{ $t("Go Home") }}</FpLink
          >
        </p>
      </div>
    </div>
  </section>
</template>
