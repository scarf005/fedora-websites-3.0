import { createApp } from "vue";
import App from "./App.vue";

// plugins
import router from "./router";
import pinia from "./plugins/pinia";
import head from "./plugins/vueuse-head";

// use plugins and mount application
const app = createApp(App);

app.use(head)
.use(pinia)
.use(router);

app.mount("#app");
