<script setup>
import { decode } from "html-entities";

const { data: page } = await useAsyncData("page-data", () => {
  return queryContent()
    .where({ _file: "community/magazine/home.yml" })
    .findOne();
});

useContentHead(page);

const { slug } = useRoute().params;

const getArticle = async (slug) => {
  let api = page.value.api;

  let [post] = await $fetch(`${api}/posts?slug=${slug}`);

  let author = await $fetch(`${api}/users/${post.author}`);

  let date = new Date(post.date).toLocaleDateString("en-us", {
    month: "long",
    day: "numeric",
    year: "numeric",
  });

  let [media] = await $fetch(`${api}/media?include=${post.featured_media}`);

  return {
    title: decode(post.title.rendered),
    author: author.name,
    author_description: author.description,
    date: date,
    image: media.source_url,
    image_caption: media.caption.rendered,
    content: post.content.rendered,
  };
};

let article;
try {
  article = await getArticle(slug);
} catch (e) {
  console.log(e);
}
</script>

<template>
  <main class="mt-8 flex flex-col items-center">
    <article class="w-1/2" v-if="article">
      <header>
        <h1 class="mb-4 border-b-2 py-2 text-4xl font-bold">
          {{ article.title }}
        </h1>
        <p class="mb-4">Posted by {{ article.author }} on {{ article.date }}</p>
        <img class="mb-4" :src="article.image" />
        <div class="mb-4" v-html="article.image_caption"></div>
      </header>
      <div class="mb-4" v-html="article.content"></div>
      <footer>
        <div class="mb-4 bg-gray-200 py-2 px-4">
          <p class="font-bold text-fp-gray-darkest">{{ article.author }}</p>
          <p>{{ article.author_description }}</p>
        </div>
      </footer>
    </article>
  </main>
</template>
