<script setup>
const { t } = useI18n();
const slots = useSlots();
const props = defineProps({
  buildid: {
    type: String,
  },
  buildDetails: {
    type: Object,
    default: null,
  },
  buildInfo: {
    type: Object,
  },
});

function prettyDateTime(ts) {
  const date = new Date(ts);
  const year = new Intl.DateTimeFormat("en", { year: "numeric" }).format(date);
  const month = new Intl.DateTimeFormat("en", { month: "short" }).format(date);
  const day = new Intl.DateTimeFormat("en", { day: "2-digit" }).format(date);

  return `${month} ${day}, ${year}`;
}

function getPkgNevraFull(tuple) {
  if (tuple[1] != 0) {
    return `${tuple[0]}-${tuple[1]}:${tuple[2]}-${tuple[3]}.${tuple[4]}`;
  }
  return `${tuple[0]}-${tuple[2]}-${tuple[3]}.${tuple[4]}`;
}

function getPkgNevra(tuple) {
  return `${tuple[0]}-${tuple[1]}.${tuple[2]}`;
}

function getPkgEvra(tuple) {
  return `${tuple[1]}.${tuple[2]}`;
}
</script>

<template>
  <div class="py-8">
    <FpObserver @intersect="$emit('loadBuild', buildid)" />
    <h3
      class="pb-3 text-center text-fp-blue dark:text-fp-newblue sm:text-start"
    >
      {{ buildid }}
    </h3>
    <template v-if="buildDetails">
      <div class="mb-4 flex gap-2">
        <div class="">Release Date:</div>
        <div class="font-bold">
          {{
            prettyDateTime(
              buildDetails["meta"]?.["coreos-assembler.build-timestamp"]
            )
          }}
        </div>
      </div>
      <div class="mb-4 flex flex-wrap items-baseline gap-x-1">
        <div v-if="buildInfo?.issues.length === 0">
          No specific issues fixed in this release.
        </div>
        <div v-else-if="buildInfo?.issues.length">
          <div class="font-bold">Issues fixed:</div>
          <ul class="ml-8 list-[square]">
            <li v-for="issue in buildInfo?.issues" class="text-base">
              <a
                :href="issue.url"
                class="text-sm underline underline-offset-1"
                target="_blank"
                >{{ issue.text }}</a
              >
            </li>
          </ul>
        </div>
        <div v-else class="font-bold">
          Release notes for this release are still pending review.
        </div>
      </div>
      <div class="mb-4 flex flex-wrap items-baseline gap-x-4">
        <div v-for="pkg in buildDetails['pkglist']">
          {{ pkg[0] }} <b>{{ pkg[2] }}</b>
        </div>
      </div>
      <div class="">
        <FpCollapse>
          <template #head>
            <div class="font-bold">
              {{ buildDetails.commitmeta["rpmostree.rpmdb.pkglist"].length }}
              packages included
            </div>
          </template>
          <div class="my-2 border border-gray-600 bg-neutral-900 p-2">
            <ul class="list-none font-mono">
              <li
                class="text-sm"
                v-for="pkg in buildDetails.commitmeta[
                  'rpmostree.rpmdb.pkglist'
                ]"
              >
                {{ getPkgNevraFull(pkg) }}
              </li>
            </ul>
          </div>
        </FpCollapse>
        <ul class="ml-12 list-outside list-[square]">
          <template v-for="(diff, diffType) in buildDetails.pkgdiff">
            <li v-if="diff.length">
              <FpCollapse>
                <template #head> {{ diff.length }} {{ diffType }} </template>
                <div class="my-2 border border-gray-600 bg-neutral-900 p-2">
                  <ul class="list-none font-mono">
                    <template v-if="diffType == 'added'">
                      <li class="text-sm" v-for="pkg in diff">
                        {{ getPkgNevra(pkg[2].NewPackage) }}
                      </li>
                    </template>
                    <template v-if="diffType == 'removed'">
                      <li class="text-sm" v-for="pkg in diff">
                        {{ getPkgNevra(pkg[2].PreviousPackage) }}
                      </li>
                    </template>
                    <template
                      v-if="diffType == 'upgraded' || diffType == 'downgraded'"
                    >
                      <li class="text-sm" v-for="pkg in diff">
                        {{ getPkgNevra(pkg[2].PreviousPackage) }} ⟶
                        {{ getPkgEvra(pkg[2].NewPackage) }}
                      </li>
                    </template>
                  </ul>
                </div>
              </FpCollapse>
            </li>
          </template>
        </ul>
      </div>
    </template>
    <template v-else>
      <CoreOsBuildInfoLoading />
    </template>
  </div>
</template>
