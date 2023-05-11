<template>
  <div
    class="container mx-auto flex max-w-7xl flex-row flex-wrap justify-center gap-8 lg:flex-nowrap"
  >
    <div class="my-5">
      <slot name="header">
        <h2
          class="mb-5 text-center text-fp-blue dark:text-gray-200 lg:text-start"
        >
          {{ $t("But wait! There's more.") }}
        </h2>
      </slot>
      <p class="mb-5 text-fp-gray">
        {{
          $t(
            "Need something a bit different? Check out our other downloads below, featuring alternative architectures, torrents and network-based installation images."
          )
        }}
      </p>
      <FpBtn
        href="https://alt.fedoraproject.org"
        color="text-center bg-white dark:bg-fp-darkblue-700 dark:border-fp-darkblue-700 dark:!text-white"
      >
        {{ $t("See More") }}
      </FpBtn>
    </div>
  </div>
</template>
