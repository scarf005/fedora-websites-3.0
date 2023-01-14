<template>
  <div class="container mx-auto grid max-w-7xl grid-cols-2">
    <div class="col-span-2 my-5 p-2 md:col-span-1">
      <slot name="header">
        <h2 class="mb-5 text-center text-fp-blue lg:text-start">
          {{ $t("We take security seriously.") }}
        </h2>
      </slot>
      <p class="mb-5 text-fp-gray">
        {{
          $t(
            "Once you have downloaded an image, be sure to verify it for both security and integrity."
          )
        }}
      </p>
      <p class="mb-5 text-fp-gray">
        {{
          $t(
            "By calculating the image’s checksum on your own computer and comparing it to the original checksum, you can verify the image has not been tampered with or corrupted. Images are also gpg signed with Fedora keys to demonstrate their integrity."
          )
        }}
      </p>
      <i18n-t
        keypath="verify_button_instruction"
        tag="p"
        class="mb-5 text-fp-gray"
      >
        <template #verify_button>
          <Icon
            name="fa-solid:clipboard-check"
            class="!align-baseline text-fp-blue-light"
          />
        </template>
      </i18n-t>
    </div>
    <div
      class="col-span-2 my-5 flex items-center justify-center p-2 md:col-span-1"
    >
      <FpImage
        class="max-h-72 drop-shadow-lg grayscale invert dark:grayscale-0 dark:invert-0"
        src="public/assets/images/verify_download_2.png"
      />
    </div>
  </div>
</template>
