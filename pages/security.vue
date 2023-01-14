<script setup>
const data = await getCMS("security");
if (data._value.packageSection.content) {
  data._value.packageSection.contentMd = await mdparser(
    data._value.packageSection.content
  );
}
if (data._value.bugSection.description) {
  data._value.bugSection.descriptionMd = await mdparser(
    data._value.bugSection.description
  );
}
const obsolete_keys = useState("obsolete_keys", () => false);
useContentHead(data);
</script>
<template>
  <main class="fp-security md:mt-2">
    <!-- TITLE -->
    <section class="py-12 text-center dark:bg-neutral-800 lg:text-start">
      <div class="container mx-auto max-w-7xl">
        <h1 class="mb-4 text-4xl text-black dark:text-white">
          {{ $t(data.title) }}
        </h1>
        <p class="text-fp-gray dark:text-fp-gray-light">
          {{ $t(data.description) }}
        </p>
      </div>
    </section>

    <section class="bg-blue-50 py-6 dark:bg-neutral-900">
      <CoreOsVerifySection>
        <template #header>
          <h2 class="mb-5 text-center text-fp-blue lg:text-start">
            {{ $t("Verify your download") }}
          </h2>
        </template>
      </CoreOsVerifySection>
    </section>

    <section class="bg-blue-50 py-6 dark:bg-neutral-900">
      <div class="container mx-auto mb-8 max-w-7xl">
        <div class="mb-6 text-center lg:text-start">
          <h2 class="mb-4 text-fp-blue">
            {{ $t(data.verifySection.title) }}
          </h2>
          <p class="text-start text-fp-gray dark:text-fp-gray-light">
            {{ $t(data.verifySection.description) }}
          </p>

          <ul
            class="list-outside list-decimal pl-8 pt-2 text-fp-gray-darkest dark:text-fp-gray-light"
          >
            <li>
              <p class="mb-2">{{ $t("Import Fedora's GPG key(s)") }}</p>
              <pre
                class="mb-1 bg-slate-100 px-4 text-sm text-gray-800"
              ><code>curl -O https://getfedora.org/static/fedora.gpg</code></pre>
              <p class="mb-4 text-sm">
                <Icon name="fa-solid:info-circle" class="mx-2 !align-sub" />

                {{ $t("You can verify the details of the GPG key(s) below.") }}
              </p>
            </li>
            <li>
              <p class="mb-2">{{ $t("Verify the CHECKSUM file is valid") }}</p>
              <pre
                class="mb-4 bg-slate-100 px-4 text-sm text-gray-800"
              ><code>gpgv --keyring ./fedora.gpg *-CHECKSUM</code></pre>
            </li>
            <li>
              <p class="mb-2">{{ $t("Verify the checksum matches") }}</p>
              <pre
                class="mb-4 bg-slate-100 px-4 text-sm text-gray-800"
              ><code>sha256sum -c *-CHECKSUM</code></pre>
            </li>
          </ul>
          <p>
            {{
              $t(
                "If the output states that the file is valid, then it's ready to use!"
              )
            }}
          </p>
        </div>
      </div>
    </section>

    <section class="bg-gray-50 py-12 dark:bg-neutral-800">
      <div class="container mx-auto mb-8 max-w-7xl">
        <div class="mb-6 text-center lg:text-start">
          <h2 class="mb-4 text-fp-blue">
            {{ $t(data.packageSection.title) }}
          </h2>
          <p class="font-display text-xl text-fp-gray">
            {{ $t(data.packageSection.description) }}
          </p>
          <ContentRenderer
            class="mt-2 text-start text-fp-gray-dark dark:text-fp-gray-light"
            v-if="data.packageSection.contentMd"
            tag="p"
            :value="data.packageSection.contentMd"
          />
        </div>
      </div>
    </section>

    <section class="bg-white py-8 dark:bg-neutral-900">
      <div class="container mx-auto max-w-7xl">
        <div class="text-center lg:text-start">
          <h2 class="text-fp-blue">
            {{ $t("Current GPG keys") }}
          </h2>
        </div>
      </div>
      <div
        class="container mx-auto grid max-w-max divide-y divide-dotted divide-fp-gray text-fp-gray dark:text-fp-gray-light"
      >
        <div v-for="gpg in data.gpg_keys.current" class="py-8">
          <h3 class="pb-3 text-fp-blue">{{ gpg.name }}</h3>
          <p>
            <span class="font-bold">id: </span
            ><code class="text-fp-gray">{{ gpg.id }}</code>
          </p>
          <p>
            <span class="font-bold">Fingerprint: </span
            ><code class="text-fp-gray">{{ gpg.fingerprint }}</code>
          </p>
          <p>
            <span class="font-bold">DNS OpenPGPKey: </span
            ><code class="text-fp-gray">{{ gpg.openpgpkey }}</code>
          </p>
        </div>
      </div>
    </section>

    <section class="bg-gray-50 py-12 dark:bg-neutral-800">
      <div class="container mx-auto max-w-7xl">
        <div
          class="flex cursor-pointer items-center justify-center gap-4 lg:justify-start"
          @click="obsolete_keys = !obsolete_keys"
        >
          <h2 class="text-fp-blue">
            {{ $t("Obsolete GPG keys") }}
          </h2>
          <Icon name="fa-solid:chevron-right" size="24" v-if="!obsolete_keys" />
          <Icon name="fa-solid:chevron-down" size="24" v-if="obsolete_keys" />
        </div>
      </div>
      <div
        v-if="obsolete_keys"
        class="container mx-auto grid max-w-max divide-y divide-dotted divide-fp-gray text-fp-gray dark:text-fp-gray-light"
      >
        <div v-for="gpg in data.gpg_keys.obsolete" class="py-8">
          <h3 class="pb-3 text-fp-blue">{{ gpg.name }}</h3>
          <p>
            <span class="font-bold">id: </span
            ><code class="text-fp-gray">{{ gpg.id }}</code>
          </p>
          <p>
            <span class="font-bold">Fingerprint: </span
            ><code class="text-fp-gray">{{ gpg.fingerprint }}</code>
          </p>
          <p v-if="gpg.openpgpkey">
            <span class="font-bold">DNS OpenPGPKey: </span
            ><code class="text-fp-gray">{{ gpg.openpgpkey }}</code>
          </p>
        </div>
      </div>
    </section>

    <section class="py-12 dark:bg-black">
      <div class="container mx-auto mb-8 max-w-7xl">
        <div class="mb-6 text-center lg:text-start">
          <h2 class="mb-4 text-fp-blue">
            {{ $t(data.bugSection.title) }}
          </h2>
          <ContentRenderer
            class="mt-2 text-start text-fp-gray-dark dark:text-fp-gray-light"
            v-if="data.bugSection.descriptionMd"
            tag="p"
            :value="data.bugSection.descriptionMd"
          />
        </div>
      </div>
    </section>
  </main>
</template>

<style>
main.fp-security a {
  @apply text-fp-blue dark:text-fp-blue-light;
}
</style>
