$('ul.main-menu li').click(function(e) {
    e.preventDefault();

    if($(this).siblings('li').find('ul.submenu:visible').length) {
          $('ul.submenu').slideUp('normal');
    }
    $(this).find('ul.submenu').slideToggle('normal');
});

var t1 = new TimelineMax({paused: true});

t1.to(".menu", 0.4, {
    autoAlpha: 1
});

t1.staggerFrom(".main-menu li a:not(.submenu li a)", 1, {
    opacity: 0,
    y: 5,
    ease: Power2.easeInOut
}, 0.1);

t1.from(".submenu", 0.4, {
    autoAlpha: 0
});

t1.staggerFrom(".media ul li", 1, {
    opacity: 0,
    y: 5,
    ease: Power2.easeInOut
}, 0.1, "-=2");

t1.from(".call", 1, {
    delay: -1.6,
    opacity: 0,
    y: 5,
    ease: Power2.easeInOut
});

t1.from(".mail", 1, {
    delay: -1.2,
    opacity: 0,
    y: 5,
    ease: Power2.easeInOut
});

t1.reverse();

$(document).on("click", ".menu-btn", function() {
    t1.reversed(!t1.reversed());
});

$(document).on("click", ".close-menu", function() {
    t1.reversed(!t1.reversed());
});