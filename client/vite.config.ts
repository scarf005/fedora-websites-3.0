import { defineConfig } from "vite";

// plugins
import vue from "@vitejs/plugin-vue";
import Pages from "vite-plugin-pages";
import * as path from "path";

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [vue(), Pages()],
  resolve: {
    alias: {
      "@": path.resolve(__dirname, './src')
    }
  }
});

