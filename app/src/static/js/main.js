const filterOpen = document.getElementById("filter-open");
const filterClose = document.getElementById("filter-close");
const filterOffcanvas = document.getElementById("filter-offcanvas");

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

var themeToggleDarkIcon = document.getElementById("theme-toggle-dark-icon");
var themeToggleLightIcon = document.getElementById("theme-toggle-light-icon");

// Change the icons inside the button based on previous settings
if (
  localStorage.getItem("color-theme") === "dark" ||
  (!("color-theme" in localStorage) &&
    window.matchMedia("(prefers-color-scheme: dark)").matches)
) {
  themeToggleLightIcon.classList.remove("hidden");
} else {
  themeToggleDarkIcon.classList.remove("hidden");
}

var themeToggleBtn = document.getElementById("theme-toggle");

themeToggleBtn.addEventListener("click", function () {
  // toggle icons inside button
  themeToggleDarkIcon.classList.toggle("hidden");
  themeToggleLightIcon.classList.toggle("hidden");

  // if set via local storage previously
  if (localStorage.getItem("color-theme")) {
    if (localStorage.getItem("color-theme") === "light") {
      document.documentElement.classList.add("dark");
      localStorage.setItem("color-theme", "dark");
    } else {
      document.documentElement.classList.remove("dark");
      localStorage.setItem("color-theme", "light");
    }

    // if NOT set via local storage previously
  } else {
    if (document.documentElement.classList.contains("dark")) {
      document.documentElement.classList.remove("dark");
      localStorage.setItem("color-theme", "light");
    } else {
      document.documentElement.classList.add("dark");
      localStorage.setItem("color-theme", "dark");
    }
  }
});

const mainBody = document.getElementById("main-body");
const filterContainer = document.getElementById("filter-container");
const offcanvasFilterContainer = document.getElementById(
  "offcanvas-filter-container"
);
const filters = document.getElementById("filters");
const search = document.getElementById("search");

filters.reset();
search.value = "";

const resizeObserver = new ResizeObserver((entries) => {
  const width = entries[0].borderBoxSize[0].inlineSize;
  if (width < 1024) {
    offcanvasFilterContainer.appendChild(filters);
  } else {
    filterContainer.appendChild(filters);
  }
});

resizeObserver.observe(mainBody);

const lastSortByEl = document.getElementById("last_sort_by");

function getSortOrder(e) {
  const value = e.target.value;
  const id = `sort-${value}`
  const el = document.getElementById(id);
  const sort_order = el.querySelector('input');
  const new_sort_order = sort_order.value != "asc" ? "asc" : "desc";
  e.detail.parameters[`sort_order_${value}`] = new_sort_order;
  e.detail.parameters[`last_sort_by`] = value;
  // console.log(new_sort_order);
  // sort_order.value = new_sort_order;
  // console.log(sort_order.value);
}