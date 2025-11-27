// let arr=["teja","pablo","bro"];

let par=document.createElement("div");
par.style.border="2px red solid"
par.style.height="300px"
// heading
let h=document.createElement("h3");
h.innerText="To do list"
par.appendChild(h)

// box
let field=document.createElement("input");
field.placeholder="enetr task";
field.type="text"
field.setAttribute("id","taskadd")
let task=document.getElementById("taskadd").value();
let button=document.createElement("button");
console.log(task)

button.onclick=function(){
    // arr.push(task)
    for(i of arr){
    console.log(i)}
}
button.innerText="add task"
par.append(field,button)

//
document.body.appendChild(par);
