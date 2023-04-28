document.addEventListener("DOMContentLoaded", () => {
  const img = document.querySelector(".img");
  const person = document.querySelector(".person");
  const main = document.querySelector(".main");
  const models = document.querySelector(".models");
  let tl = gsap.timeline();

  if (!sessionStorage.getItem("animationStarted")) {
    tl.from(
      ".left",
      {
        xPercent: -100,
        opacity: 0,
        duration: 2,
        stagger: {
          amount: 1,
          from: "left",
        },
      },
      0.5
    )
      .from(
        ".right",
        {
          xPercent: 100,
          opacity: 0,
          duration: 2,
          stagger: {
            amount: 1,
            from: "left",
          },
        },
        1
      )
      .to(".left", {
        xPercent: -100,
        opacity: 0,
        duration: 0.5,
      })
      .to(".right", {
        xPercent: 100,
        opacity: 0,
        duration: 0.5,
        ease: "power1.inOut",
      })
      .to(".img", {
        duration: 3,
        scale: 2,
      })
      .to(
        ".img2",
        {
          x: -400,
          duration: 3,
          ease: "power1.inOut",
        },
        5
      )
      .to(
        ".img3",
        {
          x: 400,
          duration: 3,
          ease: "power1.inOut",
        },
        5
      )
      .to(
        ".ten",
        {
          duration: 3,
          backgroundColor: "rgba(0, 0, 0, 1)",
        },
        5
      );

    setTimeout(() => {
      img.style.display = "none";
      person.style.display = "none";
      main.style.display = "block";
    }, 8000);
    setTimeout(() => {
      models.style.display = "none";
      sessionStorage.setItem("animationStarted", true);
    }, 13000);

    tl.from(".models img", {
      delay: 1,
      yPercent: -50,
      opacity: 0,
      duration: 1,
      ease: "power1.inOut",
      stagger: {
        amount: 1,
        from: "left",
      },
    })
      .to(".models img", {
        delay: 1,
        opacity: 0,
        duration: 1,
      })
      .to("header", {
        opacity: 1,
        duration: 0.5,
        ease: "power1.inOut",
      })
      .to("section.info", {
        opacity: 1,
        duration: 0.5,
        ease: "power1.inOut",
      });
  } else {
    img.style.display = "none";
    person.style.display = "none";
    main.style.display = "block";
    models.style.display = "none";
    tl.to(
      "header",
      {
        opacity: 1,
      },
      0
    ).to(
      "section.info",
      {
        opacity: 1,
      },
      0
    );
  }
  window.addEventListener("scroll", () => {
    let y = window.scrollY;
    if (y > 20) {
      document.querySelector("section.info").style.backgroundColor =
        "rgba(0, 0, 0, 0.5)";
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
