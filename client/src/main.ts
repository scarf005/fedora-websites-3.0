import { createApp } from "vue";
import App from "./App.vue";
import router from "./router";

const app  = createApp(App)

// Add plugins to the application

app.use(router);

// mount application
app.mount("#app")