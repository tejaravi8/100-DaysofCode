async function getall(){
  let result= await fetch("https://fakestoreapi.com/products");
  let jsondata=await result.json()
  // console.log(jsondata)
  for(let i in jsondata){
    let card=document.createElement("div")
    card.setAttribute("class","division")
    let x=document.createElement("img")
    x.src=`${jsondata[i].image}`
    card.appendChild(x)
    document.body.appendChild(card)
  }
}
getall()