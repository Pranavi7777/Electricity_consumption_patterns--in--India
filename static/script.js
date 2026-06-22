/* ==========================================
   Electricity Analytics Project
   Developed by Pranavi
========================================== */

// ----------------------------
// Loader
// ----------------------------

window.addEventListener("load", function () {

    const loader = document.getElementById("loader");

    if (loader) {

        loader.style.opacity = "0";

        setTimeout(() => {

            loader.style.display = "none";

        }, 500);

    }

});

// ----------------------------
// Theme Toggle
// ----------------------------

const body = document.body;

const savedTheme = localStorage.getItem("theme");

if (savedTheme === "dark") {

    body.classList.add("dark-mode");

}

function toggleTheme() {

    body.classList.toggle("dark-mode");

    if (body.classList.contains("dark-mode")) {

        localStorage.setItem("theme", "dark");

    } else {

        localStorage.setItem("theme", "light");

    }

}

// ----------------------------
// Sidebar Mobile
// ----------------------------

function toggleSidebar() {

    const sidebar = document.querySelector(".sidebar");

    if (sidebar) {

        sidebar.classList.toggle("active");

    }

}

// ----------------------------
// Active Navigation
// ----------------------------

const currentPage = window.location.pathname;

document.querySelectorAll(".sidebar a").forEach(link => {

    if (link.getAttribute("href") === currentPage) {

        link.classList.add("active");

    }

});

// ----------------------------
// Scroll Animation
// ----------------------------

const observer = new IntersectionObserver((entries)=>{

entries.forEach(entry=>{

if(entry.isIntersecting){

entry.target.classList.add("fade-up");

}

});

});

document.querySelectorAll(".card,.dashboard-container,.about-container,.hero").forEach(el=>{

observer.observe(el);

});

// ----------------------------
// Smooth Button Hover
// ----------------------------

document.querySelectorAll(".btn,.btn2,.login-btn").forEach(button=>{

button.addEventListener("mouseenter",()=>{

button.style.transition=".3s";

});

});

// ----------------------------
// Scroll to Top
// ----------------------------

const topButton=document.createElement("button");

topButton.innerHTML="↑";

topButton.id="topButton";

document.body.appendChild(topButton);

topButton.style.position="fixed";

topButton.style.bottom="25px";

topButton.style.right="25px";

topButton.style.width="50px";

topButton.style.height="50px";

topButton.style.borderRadius="50%";

topButton.style.border="none";

topButton.style.background="#0B5ED7";

topButton.style.color="white";

topButton.style.cursor="pointer";

topButton.style.display="none";

topButton.style.fontSize="22px";

topButton.style.boxShadow="0 10px 20px rgba(0,0,0,.25)";

window.addEventListener("scroll",()=>{

if(window.scrollY>250){

topButton.style.display="block";

}else{

topButton.style.display="none";

}

});

topButton.onclick=function(){

window.scrollTo({

top:0,

behavior:"smooth"

});

};

// ----------------------------
// Welcome Console
// ----------------------------

console.log("⚡ Electricity Consumption Analytics");

console.log("Developed by Pranavi");

console.log("Powered by Flask + Tableau");