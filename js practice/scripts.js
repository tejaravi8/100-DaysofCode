// // // // // for(let i=1;i<=2;i++){
// // // // //     for(let j=1 ;j<=4;j++){
// // // // //         console.log(i,j)
// // // // //     }
// // // // // }

// // // // // for(let i = 1; i <= 3; i++){
// // // // //   for(let j = 1; j <= i; j++){
// // // // //     console.log(i,j)
// // // // //   }
// // // // // }

// // // // // for(let i = 1; i <= 3; i++){
// // // // //   for(let j = 1; j <= 3; j++){
// // // // //     if(j === 2) {continue};
// // // // //     console.log(i, j);
// // // // //   }
// // // // // }

// // // // // for(let i = 1; i <= 3; i++){
// // // // //   for(let j = 1; j <= 3; j++){
// // // // //     if(j === 2) break;
// // // // //     console.log(i, j);
// // // // //   }
// // // // // }

// // // // // for(let i = 2; i < 3; i++){
// // // // //   for(let j = 0; i < 3; j++){
// // // // //     console.log(i, j);
// // // // //     i++
// // // // //   }
// // // // // }

// // // // // for(let i = 3; i > 0; i--){
// // // // //   for(let j = i; j > 0; j--){
// // // // //     console.log(i, j);
// // // // //   }
// // // // // }

// // // // // for(let i = 0; i < 3; i++){
// // // // //   for(let j = 0; j < 2; j++){
// // // // //     console.log(i, j);
// // // // //     i++;
// // // // //   }
// // // // // }

// // // // // for(let i = 1; i <= 3; i++){
// // // // //   for(let j = 1; j <= 3; j++){
// // // // //     console.log(i * j);
// // // // //   }
// // // // // }

// // // // // for(let i = 1; i <= 3; i++){
// // // // //   for(let j = i; j <= 3; j++){
// // // // //     console.log(i, j);
// // // // //   }
// // // // // }

// // // // for(let i = 1; i <= 3; i++){
// // // //   for(let j = 1; j <= 3; j++){
// // // //     if(i + j > 3) console.log(i, j);
// // // //   }
// // // // }

// // // // console.log("body")

// // // // console.log(document.getElementById("demo"))
// // // console.log(document.getElementsByClassName("teja")[0].textContent)
// // // // console.log(document.getElementById("demo").innerText)

// // console.log(document.getElementById("teja").innerText)

// // Prime Number
// let number=5;
// function primecheck(num){
//     if (num<2){
//         return false
//     }else{
//         for(let i=2;i<=num;i++){
//             if(num%i==0){
//                 return false
//             }
//         else{
//             return true
//         }
//         }
//     }

// }
// primecheck(number)
// // Palindrome 
// // Armstrong number 
// // Factorial 
// // Swap two numbers 
// // Fibonacci 
// // Largest ,smallest ,second smallest ,second largest ,third smallest ,third largest in an array
// // Patterns like (square ,pyramid,triangle ,reverse triangle,) 
// // Anagrams
// // Matrix problems like (Transpose of a matrix)

// let number=153;
// let st=number.tostring(number);
// console.log(st)

// let arr=[3,4,57,9,1,7];
// let first=second=0

// for(let i of arr){
//     console.log(i)
// }
// // let number=8;
// // console.log(checkprime(number))
// // function checkprime(num){
// //     if (num<2){
// //         return "not aprime"
// //     }else{
// //         for(let i=2;i<num;i++){
// //             if (num%i==0){
// //                 return "not a prime"
// //             }
// //             else{
// //                 return "prime"
// //             }
// //         }
// //     }
// // }

// // Palindrome 
// // let name="madah";
// // let newname="";
// // for(let i=name.length-1;i>=0;i--){
// //     newname+=name[i]
// // }
// // if(name==newname){
// //     console.log("palindrome")
// // }else{
// //     console.log("not a palindrome")
// // }

// // let name="madam";
// // let rev="";
// // for(i of name){
// //     rev=i+rev
// // }
// // console.log(rev==name)
// //string not supporting
// // Armstrong number
// let num=153;
// let st=num.tostring();
// console.log(st)
// // c=0
// // for(let i in string(num)){
// //     console.log(i)
// // }

// let arr=[3,4,57,19,1,7];
// let first=second=Infinity
// for(let i of arr){
//     if(i<first){
//         second=first
//         first=i
//     }else if(first<i && i<second){
//         second=i
//     }
// }
// console.log(second)
// console.log(second)

// let arr=[0,1,false, 2,'', 3];
// for(let i of arr){
//     if(typeof(Boolean(i))==false){
//         console.log(i)
//     }
// }
// console.log(Boolean(5))/