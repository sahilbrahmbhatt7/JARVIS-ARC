window.addEventListener("load", function(){

/* JARVIS boot voice */

setTimeout(()=>{

eel.bootLoading();

},1200);


setTimeout(()=>{

let boot = document.getElementById("boot");

boot.style.opacity="0";

setTimeout(()=>{

boot.style.display="none";

/* Fade in main UI */

document.querySelector(".conatiner").style.opacity="1";

},1000);

},4500);

});