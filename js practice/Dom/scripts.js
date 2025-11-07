let container=document.createElement("div")
container.style.display="grid"
container.style.gridTemplateColumns="repeat(4,1fr)";
let arr=["hiiii","how r u","how do you do","hiiii","hello","how r u","how do you do","hello"]
let imgarr=["https://leadschool.in/wp-content/uploads/2022/04/shutterstock_1777292972.jpg","https://www.apu.apus.edu/images/site/cards/coding-skills-apu.jpg","https://www.themuse.com/_next/image?url=https%3A%2F%2Fcms-assets.themuse.com%2Fmedia%2Flead%2F01212022-1047259374-coding-classes_scanrail.jpg&w=1920&q=75","https://img.freepik.com/free-photo/computer-program-coding-screen_53876-138060.jpg?semt=ais_hybrid&w=740&q=80","https://img.freepik.com/free-photo/computer-program-coding-screen_53876-138060.jpg?semt=ais_hybrid&w=740&q=80","https://leadschool.in/wp-content/uploads/2022/04/shutterstock_1777292972.jpg","https://www.apu.apus.edu/images/site/cards/coding-skills-apu.jpg","https://www.themuse.com/_next/image?url=https%3A%2F%2Fcms-assets.themuse.com%2Fmedia%2Flead%2F01212022-1047259374-coding-classes_scanrail.jpg&w=1920&q=75"]
for(let i=0;i<8;i++){
    let card=document.createElement("div");
let title=document.createElement("div");
title.textContent=arr[i]
title.style.color="white"
title.style.backgroundColor="black"
card.style.backgroundImage=`url(${imgarr[i]})`
card.style.height="50vh"
card.style.width="23vw"
container.appendChild(card)
card.appendChild(title)
card.style.margin="10px"
}

document.body.appendChild(container)

// let card=document.createElement("div");
// let title=document.createElement("div");
// title.textContent="hell"
// title.style.color="white"
// title.style.backgroundColor="black"
// card.style.backgroundColor="blue"
// card.style.height="50vh"
// card.style.width="50vw"
// document.body.appendChild(card)
// card.appendChild(title)
// document.body.appendChild(title)