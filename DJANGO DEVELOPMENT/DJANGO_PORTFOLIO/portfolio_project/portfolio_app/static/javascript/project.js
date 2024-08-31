document.addEventListener("DOMContentLoaded", function () {
    let slideIndex = 1;
    showSlides(slideIndex);

    function moveSlide(n) {
        slideIndex += n;
        showSlides(slideIndex);
    }

    function showSlides(n) {
        const slides = document.getElementsByClassName("carousel-item");
        if (n > slides.length) {
            slideIndex = 1;
        }
        if (n < 1) {
            slideIndex = slides.length;
        }

        for (let i = 0; i < slides.length; i++) {
            slides[i].style.display = "none";
        }
        slides[slideIndex - 1].style.display = "block"; // Change to "block" for visibility
    }

    document.querySelector(".carousel-control-prev").addEventListener("click", function () {
        moveSlide(-1);
    });

    document.querySelector(".carousel-control-next").addEventListener("click", function () {
        moveSlide(1);
    });
});
