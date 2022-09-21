/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./index.html", "./pages/**/*.vue", "./components/**/*.vue"],
  theme: {
    fontFamily: {
      display: ["Montserrat", "ui-sans-serif", "system-ui", "sans-serif"],
      sans: ['"Open Sans"', "ui-sans-serif", "system-ui", "sans-serif"],
      serif: ["ui-serif", "serif"],
      mono: ['"Source Code Pro"', "ui-monospace", "monospace"],
    },
    extend: {
      colors: {
        fp: {
          gray: {
            darkest: "#eff0f1",
            darker: "#dfe0e3",
            dark: "#c5c7cc",
            DEFAULT: "#9a9fa6",
            light: "#79818b",
            lightest: "#535961",
          },
          blue: {
            light: "#51a2da",
            DEFAULT: "#3c6eb4",
            dark: "#294172",
          },
          green: {
            lighest: "#e9f9dd",
            light: "#bbed97",
            DEFAULT: "#79db32",
          },
          magenta: {
            lightest: "#f9dde9",
            light: "#dc97bb",
            DEFAULT: "#db3279",
          },
          orange: {
            lightest: "#fbeedb",
            light: "#f2ca92",
            DEFAULT: "#e59728",
          },
          purple: {
            lightest: "#ece5f1",
            light: "#cfbddd",
            DEFAULT: "#a07cbc",
          },
        },
      },
    },
  },
};
