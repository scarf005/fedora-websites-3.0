import markdownParser from "@nuxt/content/transformers/markdown";

export async function mdparser(tag) {
  return await markdownParser.parse("content:dummy.md", tag);
}
