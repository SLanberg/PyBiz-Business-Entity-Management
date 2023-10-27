$(document).ready(function () {
  document
    .getElementById("search-input")
    .addEventListener("keydown", function (event) {
      if (event.key === "Enter" || event.keyCode === 13) {
        // Check if the input field is not empty to avoid redirection on an empty search
        var searchInput = document.getElementById("search-input").value;

        // Construct the URL with the search query
        var searchQuery = encodeURIComponent(searchInput);

        // Replace 'your-destination-url' with the URL you want to redirect to
        var url = "company_list?q=" + searchQuery;

        // Redirect to the search results page
        window.location.href = url;
      }
    });

  particlesJS("particles-js", {
    particles: {
      number: {
        value: 170,
        density: {
          enable: true,
          value_area: 800,
        },
      },
      color: {
        value: "#ff0000",
      },
      shape: {
        type: "circle",
        stroke: {
          width: 0,
          color: "#000000",
        },
        polygon: {
          nb_sides: 5,
        },
        image: {
          src: "img/github.svg",
          width: 100,
          height: 100,
        },
      },
      opacity: {
        value: 0.4,
        random: false,
        anim: {
          enable: false,
          speed: 1,
          opacity_min: 0.1,
          sync: false,
        },
      },
      size: {
        value: 5,
        random: true,
        anim: {
          enable: false,
          speed: 1,
          size_min: 0.1,
          sync: false,
        },
      },
      line_linked: {
        enable: true,
        distance: 150,
        color: "#ff0000",
        opacity: 0.4,
        width: 1,
      },
      move: {
        enable: true,
        speed: 6,
        direction: "none",
        random: false,
        straight: false,
        out_mode: "out",
        bounce: false,
        attract: {
          enable: false,
          rotateX: 600,
          rotateY: 1200,
        },
      },
    },
    interactivity: {
      detect_on: "canvas",
      events: {
        onhover: {
          enable: true,
          mode: "repulse",
        },
        onclick: {
          enable: false,
          mode: "push",
        },
        resize: true,
      },
      modes: {
        grab: {
          distance: 400,
          line_linked: {
            opacity: 1,
          },
        },
        bubble: {
          distance: 200,
          size: 4,
          duration: 2,
          opacity: 0.5194473080642195,
          speed: 3,
        },
        repulse: {
          distance: 90,
          duration: 0.4,
        },
        push: {
          particles_nb: 4,
        },
        remove: {
          particles_nb: 2,
        },
      },
    },
    retina_detect: true,
  });
});
