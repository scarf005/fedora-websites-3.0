import { createApp } from "vue";
import App from "@/App.vue";

// plugins
import router from "@/router";
import pinia from "@/plugins/pinia";
import head from "@/plugins/vueuse-head";
import i18n from "@/plugins/i18n";
import FontAwesomeIcon from "./plugins/fontawesome-icons";

import "@/assets/css/tailwind.css";
const app = createApp(App);

// font awesome icons
app.component("font-awesome-icon", FontAwesomeIcon);

// internationalization
i18n(app);

// core plugins
app.use(head).use(pinia).use(router);

// mount app
app.mount("#app");
