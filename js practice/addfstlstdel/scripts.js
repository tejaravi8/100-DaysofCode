
let arr=[]
let div_el=document.getElementsByClassName("divisio")
let valu=document.getElementsByTagName("input")

function action(condition){
    if (condition=="addFirst"){
        arr.unshift(valu[0].value)
        clearip()
        console.log(arr)

    }else if(condition=="addLast"){
        arr.push(valu[0].value)
        clearip()
        console.log(arr)

    }else if(condition=="deleteFirst"){
        arr.shift()
        console.log(arr)

    }else{
        arr.pop()
        console.log(arr)
    }
    display()
}

function display(){
    div_el[0].innerHTML=""
    for(let i=0;i<arr.length;i++){
        let p=document.createElement("p")
        p.innerText=arr[i]
        div_el[0].appendChild(p)
    }
}
function clearip(){
    valu[0].value=""
}
