{
  const setupGalleries = () => {
    for (const gallery of document.querySelectorAll(".citation-figures")) {
      const viewport = gallery.querySelector("[data-gallery-viewport]");
      const previous = gallery.querySelector('[data-gallery-direction="-1"]');
      const next = gallery.querySelector('[data-gallery-direction="1"]');

      const updateControls = () => {
        previous.disabled = viewport.scrollLeft <= 1;
        next.disabled = viewport.scrollLeft + viewport.clientWidth >= viewport.scrollWidth - 1;
      };

      const move = (direction) => {
        viewport.scrollBy({ left: direction * viewport.clientWidth, behavior: "smooth" });
      };

      previous.addEventListener("click", () => move(-1));
      next.addEventListener("click", () => move(1));
      viewport.addEventListener("scroll", updateControls, { passive: true });
      window.addEventListener("resize", updateControls);
      updateControls();
    }
  };

  window.addEventListener("load", setupGalleries);
}
