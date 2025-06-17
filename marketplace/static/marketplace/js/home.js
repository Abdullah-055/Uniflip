// Highlight active link on the sidebar
document.addEventListener("DOMContentLoaded", () => {
  const links = document.querySelectorAll(".sidebar a");
  links.forEach((link) => {
    link.addEventListener("click", () => {
      links.forEach((l) => l.classList.remove("active"));
      link.classList.add("active");
    });
  });
});
