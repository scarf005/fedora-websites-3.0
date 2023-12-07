// https://stackoverflow.com/a/60994204 (CC BY-SA 4.0)
window.addEventListener("beforeunload", function () {
  const page = document.getElementById("startpage");
  for (const child of page.children) {
    child.style.opacity = 0;
  }
  history.scrollRestoration = "manual";
  window.scrollTo(0, 0);
});

// https://stackoverflow.com/a/43043658 (CC BY-SA 4.0)
window.addEventListener("pageshow", function (event) {
  var historyTraversal =
    event.persisted ||
    (typeof window.performance != "undefined" &&
      window.performance.navigation.type === 2);
  if (historyTraversal) {
    window.location.reload();
  }
});

const sidebars = new URLSearchParams(window.location.search).get("sidebars");

if (sidebars != "0") {
  const s_columns = document.getElementsByClassName("sp_sidebar");
  for (let i = 0; i < s_columns.length; i++) {
    s_columns[i].classList.add("xl:block");
  }
}

document.getElementById("sp_spinner").style.visibility = "visible";

const s_elements = document.getElementsByClassName("sp_static");
for (let i = 0; i < s_elements.length; i++) {
  s_elements[i].style.display = "none";
}

const c_elements = document.getElementsByClassName("sp_pulser_container");
for (let i = 0; i < c_elements.length; i++) {
  c_elements[i].style.display = "block";
}

const p_elements = document.getElementsByClassName("sp_pulser");
for (let i = 0; i < p_elements.length; i++) {
  p_elements[i].style.visibility = "visible";
  p_elements[i].style.position = "static";
}
