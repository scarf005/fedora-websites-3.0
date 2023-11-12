// vim:set ts=2 sw=2 et:

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
}
