let arr=[];
let val=document.getElementsByTagName("input")
let cldiv=document.getElementById("main")
function addItem(){
    arr.push(val[0].value)
    cldiv.innerHTML=""
    showElements()
    val[0].value=""
}

function showElements(){
    for(let i=0;i<arr.length;i++){
        let el=document.createElement("p")
        el.innerText=arr[i]
        let bt=document.createElement("button")
        bt.innerText="remove"
        let box=document.createElement("div")
        box.setAttribute("class","box")
        box.append(el,bt)
        cldiv.appendChild(box)
        document.body.append(cldiv)
        bt.addEventListener("click",function(){
            box.remove()
            arr.splice(i,1)

        })
    }
}
