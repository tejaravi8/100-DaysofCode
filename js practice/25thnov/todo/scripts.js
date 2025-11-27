let arr=[]
let input=document.getElementById("input")
let disp=document.getElementById("display")

function addTask(){
    disp.innerHTML=""
    arr.push(input.value)
    input.value="";
    for(let i in arr){
        let p=document.createElement("p")
        p.innerHTML=arr[i]
        let but=document.createElement("button")
        but.innerText="remove"
        but.addEventListener("click",function(){
            console.log("button click")
            but.remove()
            p.remove()
            arr.splice(i,1)
        })
        disp.append(p,but)
        document.body.appendChild(disp)
    }
    
}

// localStorage.setItem("data",JSON.stringify(arr))