let num=0
function increment(){
    num+=1
    document.getElementById("number").innerText=num
    if(num>0){
        document.getElementById("mmm").style.color="green"
    }else if(num==0){
        document.getElementById("mmm").style.color="black"
    }

}
function reset(){
    num=0
    document.getElementById("number").innerText=num
    document.getElementById("mmm").style.color="black"
    

}
function decrement(){
    num-=1
    document.getElementById("number").innerText=num
    if(num<0){
        document.getElementById("mmm").style.color="red"
    }else if(num==0){
        document.getElementById("mmm").style.color="black"
    }
}