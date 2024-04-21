const filterOpen = document.getElementById("filter-open");
const filterClose = document.getElementById("filter-close");
const filterOffcanvas = document.getElementById("filter-offcanvas");
const sortToggle = document.getElementById("sort-toggle");
const sortMenu = document.getElementById("sort-menu");
const hamburgerButton = document.getElementById("hamburger-button");
const hamburgerMenu = document.getElementById("hamburger-menu");

const accordions = document.getElementsByClassName("accordion");

for (let i = 0; i < accordions.length; i++) {
  accordions[i].addEventListener("click", () => {
    accordions[i].nextElementSibling.classList.toggle("hidden");
    const icons = accordions[i].getElementsByClassName("icon");
    for (let j = 0; j < icons.length; j++) {
      icons[j].classList.toggle("hidden");
    }
  });
}

filterOpen.addEventListener("click", () => {
  filterOffcanvas.classList.remove("hidden");
});

filterClose.addEventListener("click", () => {
  filterOffcanvas.classList.add("hidden");
});

sortToggle.addEventListener("click", () => {
  sortMenu.classList.toggle("hidden");
});

hamburgerButton.addEventListener("click", () => {
  hamburgerMenu.classList.toggle("hidden");
});
