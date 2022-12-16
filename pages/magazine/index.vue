<script setup>
import { decode } from "html-entities";

const { data: page } = await useAsyncData("page-data", () => {
  return queryContent()
    .where({ _file: "community/magazine/home.yml" })
    .findOne();
});

useContentHead(page);

const path = useRoute().path;
const page_num = parseInt(useRoute().query.page_num);

const getArticles = async (count, page_num) => {
  let api = page.value.api;

  let posts_raw = await $fetch.raw(
    `${api}/posts?context=embed&per_page=${count}&page=${page_num}`
  );

  let posts = posts_raw._data;
  let pages = posts_raw.headers.get("x-wp-totalpages");

  let page_links = [];
  for (let i = page_num - 2; i <= page_num + 2; i++) {
    if (i < 1) {
      continue;
    }
    if (i > pages) {
      continue;
    }
    page_links.push(i);
  }
  if (page_links[0] != 1) {
    if (page_links[0] != 2) {
      page_links.unshift("…");
    }
    page_links.unshift(1);
  }
  if (page_links[page_links.length - 1] != pages) {
    if (page_links[page_links.length - 1] != pages - 1) {
      page_links.push("…");
    }
    page_links.push(pages);
  }

  let articles = [];
  for (const p of posts) {
    let [featured] = await $fetch(`${api}/media?include=${p.featured_media}`);
    let image_url = null;
    if (featured) {
      if (featured.media_details.sizes["post-image-thumbnail"]) {
        image_url =
          featured.media_details.sizes["post-image-thumbnail"].source_url;
      }
    }

    let comments = await $fetch.raw(`${api}/comments?per_page=1&post=${p.id}`);
    articles.push({
      image: image_url,
      title: decode(p.title.rendered),
      link: `${path}/${p.slug}`,
      date: new Date(p.date).toLocaleDateString("en-us", {
        month: "long",
        day: "numeric",
        year: "numeric",
      }),
      comments: comments.headers.get("x-wp-total"),
    });
  }

  return {
    articles: articles,
    page_links: page_links,
  };
};

let articles;
let page_links;
try {
  ({ articles, page_links } = await getArticles(
    18,
    page_num > 0 ? page_num : 1
  ));
} catch (e) {
  console.log(e);
}
</script>

<template>
  <main class="mt-8 flex flex-col items-center">
    <div class="mb-4 w-10/12 border-b-2 pb-4">
      <p class="italic">{{ page.description }}</p>
    </div>
    <div class="w-10/12">
      <div class="grid grid-cols-3 gap-8">
        <div
          v-for="a in articles"
          class="mx-auto max-w-[472px] border-b-2 pb-4"
        >
          <article>
            <div class="pb-4">
              <NuxtLink :to="a.link"
                ><img
                  :src="a.image"
                  class="rounded-lg"
                  width="472"
                  height="200"
              /></NuxtLink>
            </div>
            <div>
              <NuxtLink
                :to="a.link"
                class="text-xl font-bold no-underline hover:underline"
                >{{ a.title }}</NuxtLink
              >
            </div>
            <div class="text-slate-500">
              <NuxtLink
                :to="a.link"
                class="text-base no-underline hover:underline"
                >{{ a.date }}</NuxtLink
              >
              –
              <NuxtLink
                :to="a.link"
                class="text-base no-underline hover:underline"
                >{{ a.comments }} Comments</NuxtLink
              >
            </div>
          </article>
        </div>
      </div>
    </div>
    <div class="my-4 w-10/12 border-y-2 p-4">
      <div class="flex justify-between font-bold text-slate-500">
        <div>
          <a
            v-if="page_links[3] !== '…'"
            :href="
              path +
              '?page_num=' +
              (page_links.indexOf('…') > 1
                ? page_links[page_links.length - 6]
                : page_links[3])
            "
            >← Previous</a
          >
        </div>
        <div>
          <span v-for="p in page_links"
            ><a :href="path + '?page_num=' + p">{{ ` ${p} ` }}</a></span
          >
        </div>
        <div>
          <a
            v-if="page_links[page_links.length - 4] !== '…'"
            :href="
              path +
              '?page_num=' +
              (page_links.indexOf('…') > 1
                ? page_links[page_links.length - 4]
                : page_links[5])
            "
            >Next →</a
          >
        </div>
      </div>
    </div>
  </main>
</template>
