setTimeout(function(){
    $('#message').fadeOut('slow');
}, 3000);
    


const hamburger = document.querySelector(".hamburger");
const navMenu = document.querySelector(".nav-menu");

hamburger.addEventListener("click", mobileMenu);

function mobileMenu() {
hamburger.classList.toggle("active");
navMenu.classList.toggle("active");
}

const navLink = document.querySelectorAll(".nav-link");

navLink.forEach(n => n.addEventListener("click", closeMenu));

function closeMenu() {
hamburger.classList.remove("active");
navMenu.classList.remove("active");
};




window.addEventListener('scroll', function() {
let scrollMenu = document.querySelector(".nav-menu2");
scrollMenu.classList.toggle("scrolling", window.scrollY > 0);
})

    
    


function myFunction() {
/* Get the text field */
const copyText = document.getElementById("myInput");

/* Select the text field */
copyText.select();
copyText.setSelectionRange(0, 99999); /* For mobile devices */

/* Copy the text inside the text field */
navigator.clipboard.writeText(copyText.value);

/* Alert the copied text */
alert("Copied: " + copyText.value);
}


var swiper = new Swiper(".mySwiper", {
effect: "coverflow",
grabCursor: true,
centeredSlides: true,
slidesPerView: "auto",
loop: true,
autoplay:true,
coverflowEffect: {
rotate: 0,
stretch: 10,
depth: 200,
modifier: 2,
slideShadows: true,
},
});




