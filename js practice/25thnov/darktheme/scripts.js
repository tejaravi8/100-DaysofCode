let data=document.getElementById("text")
let prev_saved=localStorage.getItem("input")
data.value=prev_saved

function send(){
localStorage.setItem("input",data.value)
}

let bt_name=document.getElementsByClassName("dark")
let t=localStorage.getItem("theme")

if (t=="dark"){
    document.body.style.backgroundColor="black"
    document.body.style.color="white"
}

function theme(){
    document.body.style.backgroundColor="black"
    document.body.style.color="white"
    // bt_name[0].innerText="light"
    localStorage.setItem("theme","dark")

}