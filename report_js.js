document.addEventListener('DOMContentLoaded', function () {
    const slides = document.querySelector('.slides'); 
    const totalImages = document.querySelectorAll('.slides img').length; 
    let index = 0; 
    function updateSlide() {
        slides.style.transform = `translateX(-${index * 50}%)`;
    }
    document.querySelector('.slider_btn.prev').addEventListener('click', function () {
        index--;
        if (index < 0) {
            index = totalImages - 1; 
        }
        updateSlide();
    });
    document.querySelector('.slider_btn.next').addEventListener('click', function () {
        index++;
        if (index >= totalImages) {
            index = 0; 
        }
        updateSlide();
    });
    setInterval(function () {
        index++;
        if (index >= totalImages) {
            index = 0; 
        }
        updateSlide();
    }, 5000); 
    updateSlide();
});

document.getElementById('reportForm').addEventListener('submit', function (event) {
    event.preventDefault();
    alert("Thank you for submitting your report!");
});
