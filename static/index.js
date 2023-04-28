document.addEventListener("DOMContentLoaded", () => {
  window.addEventListener("scroll", () => {
    let y = window.scrollY;
    if (y > 20) {
      document.querySelector("section.info").style.backgroundColor =
        "rgba(0, 0, 0, 0.7)";
      document.querySelector("section.info .title h1").style.color = "white";
      document.querySelector("header").style.top = "0%";
      document.querySelector("header").style.background = "black";
    } else {
      document.querySelector("section.info").style.backgroundColor = "";
      document.querySelector("section.info .title h1").style.color = "";
      document.querySelector("header").style.top = "-20%";
      document.querySelector("header").style.background = "";
    }
  });
});

