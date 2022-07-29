# Netlify CMS Usage
- Red Hat's yaml extension is helpful for working in the config.yml file
- [Article on splitting up config.yml so it's more maintainable](https://www.iliascreates.com/blog/post/splitting-netlifycms-config-to-multiple-js-files/)
  - this is for us to start thinking about the long term usage of netlify cms
- [Netlify CMS and Gitlab Authentication](https://www.netlifycms.org/docs/gitlab-backend/)
## Localhost

- To run netlify cms locally for testing and setting up content fields, [follow the steps in this article](https://www.programmingbasic.com/how-to-run-netlify-cms-admin-locally)
  1. add `local_backend: true` to the `config.yml` file
  2. run `npx netlify-cms-proxy-server` from the root of your repo (will fire up a server on port 8081)
  3. in a different terminal, run `npm run dev` to spin up nuxt
  4. in your browser, go to http://localhost:3000/admin (or whatever your dev server port is with /admin)

## Collections

- [Distinction between folder and file collections](https://www.netlifycms.org/docs/collection-types/)
  - file collections are distinct files, folder collections are for things like blogs that use the same format again and again
