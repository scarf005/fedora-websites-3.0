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
