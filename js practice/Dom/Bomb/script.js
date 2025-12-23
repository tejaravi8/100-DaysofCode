let time=document.getElementsByTagName("h1")
let a=document.getElementsByTagName("input");
let button=document.getElementById("button")

let timeLeft = 5; // seconds

const countdown = setInterval(() => {
    time[0].innerHTML=timeLeft
    console.log(timeLeft);
    timeLeft--;

    if ((timeLeft < 0) && a[0].value==10) {
        // console.log("Boom");
        time[0].innerHTML="boom"
        clearInterval(countdown);
    }
}, 1000);
