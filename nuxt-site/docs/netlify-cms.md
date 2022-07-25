# Netlify CMS Usage

## Localhost
- To run netlify cms locally for testing and setting up content fields, [follow the steps in this article](https://www.programmingbasic.com/how-to-run-netlify-cms-admin-locally)
  1. add `local_backend: true` to the `config.yml` file
  2. run `npx netlify-cms-proxy-server` from the root of your repo (will fire up a server on port 8081)
  3. in a different terminal, run `npm run dev` to spin up nuxt
  4. in your browser, go to http://localhost:3000/admin (or whatever your dev server port is with /admin)