# Vue Router
_Notes and help on navigating the vue router_

## TODOS and Dev Ideas
- 22-07-06 (lilyx): Concerned about the router index file becoming too bloated, See articles below that adress this. Consider splitting routes into multiple files
- 22-07-08 (lilyx): Set up a rerouting system so that we can link to pages not in vue yet using `beforeEnter(){}` syntax.
  - this is one half of the puzzle, the other half is having a reusable component that can be dropped into the pages not in this repo.
    - An important point here is that this could be a problem if we have to change the links in multiple spots, if we are able to reduce this to 1-3 spots for all of the pages, that would be optimum, but I'm not too sure how we would do that.
## Articles and Docs
- [Vue Router Homepage](https://router.vuejs.org/)
- [Medium Article on Vue Routing](https://medium.com/@disjfa/lets-route-a-vue-app-aa9c3f3dbdf8)
- [Stack Overflow Question on lots of routes](https://stackoverflow.com/questions/48264980/splitting-routes-into-separate-files)