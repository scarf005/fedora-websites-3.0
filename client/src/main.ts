import { createApp } from "vue";
import App from "@/App.vue";

// plugins
<<<<<<< HEAD
import router from "./router";
import pinia from "./plugins/pinia";
import head from "./plugins/vueuse-head";
import i18n from "./plugins/i18n";

// styles
import "./assets/css/tailwind.css";

=======
import router from "@/router";
import pinia from "@/plugins/pinia";
import head from "@/plugins/vueuse-head";
import i18n from "@/plugins/i18n";
>>>>>>> 5f08b267d7efe56737d15dd7506c3787f03a884b
// use plugins and mount application
const app = createApp(App);

app.use(head).use(pinia).use(router);

i18n(app.mount("#app"));
