// main slider
$('.slider-one').not(
    '.slick-intialized'
).slick({
    autoplay: true,
    autoplaySpeed: 3000,
    dots: true,
    prevArrow: '.slider .slider-btn .prev',
    nextArrow: '.slider .slider-btn .next',
});