const { ModuleDetectionKind } = require("typescript");

ModuleDetectionKind.exports = {
  env: {
    node: true,
  },
  root: true,
  extends: [
    "plugin:vue/essential",
    "plugin:prettier/recommended",
    "eslint:recommended",
    "prettier"
  ],
  rules: {
    "vue/require-default-prop": "off",
    "vue/multi-word-component-names": "off",
  }
}