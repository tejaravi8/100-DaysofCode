let data=[{
    student_name:"teja",
    age:21,
    marks:89,
    skills:["python","java script"],
    address:{pincode:535578,city:"bobbili"}
}]
// {
//     student_name:"sanjeev",
//     age:26,
//     marks:93,
//     skills:["djnago","java script"],
//     address:{pincode:500078,city:"hyderabad"}
// }]

// for(let i of data){
//     for(let j in i){
//         console.log(`${j} : ${i[j]}`)
//     }
// }

let ele=document.getElementById("print")
function getdata(){
    ele.innerHTML=""
    for(let i of data){
        
    for(let j in i){
        let nameing=document.createElement("h4")
        nameing.innerText=`${j}  :  ${i[j]}`
        ele.appendChild(nameing)

        // console.log(`${j} : ${i[j]}`)
    }
    // let line=document.createElement("h4")
    //     line.innerText="_____________________________"
    //     ele.appendChild(line)
}
}