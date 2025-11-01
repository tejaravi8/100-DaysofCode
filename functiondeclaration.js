// // // // function test(){  //func declaration
// // // //     var x=10;
// // // //     if(true){
// // // //         var x = 20;
// // // //         console.log(x,"5");
// // // //     }
// // // //     console.log(x,"7");
// // // // }
// // // // test();

// // // // function example() {
// // // //   var y = 5;
// // // //   if (true) {
// // // //     let y = 10;
// // // //     console.log(y);
// // // //   }
// // // //   console.log(y);
// // // // }
// // // // example();
// // // // // console.log(y)

// // // // function run() {
// // // //   if (true) {
// // // //     var a = 100;
// // // //     let b = 200;
// // // //     const c = 300;
// // // //   }
// // // //   console.log(a);
// // // //   console.log(typeof b);
// // // // }
// // // // run();

// // // // var x = 1;
// // // // function outer() {
// // // //   console.log(x);
// // // //   var x = 2;
// // // // }
// // // // outer();
// // // // // console.log(x)


// // // // let x = 10;
// // // // {
// // // //   const x = 20;
// // // //   {
// // // //     let x = 30;
// // // //     console.log(x);
// // // //   }
// // // //   console.log(x);
// // // // }
// // // // console.log(x);



// // // // console.log(a);
// // // // console.log(typeof b);
// // // // console.log(typeof c);
// // // // {
// // // //   let b =4;
// // // //   const c =5;
// // // // }

// // // // for (var i = 0; i < 3; i++) {}
// // // // console.log(i);

// // // // for (let j = 0; j < 3; j++) {console.log(j)}
// // // // // console.log(j);

// // // // function demo() {
// // // //   console.log(a);
// // // //   var a = 50;
// // // //   console.log(a);
// // // // }
// // // // demo();     // undefined   50

// // // // function blockTest() {
// // // //   const value = 5;
// // // //   if (true) {
// // // //     const value = 10;
// // // //     console.log(value);
// // // //   }
// // // //   console.log(value);
// // // // }
// // // // blockTest();   10 5


// // // // function testScope() {
// // // //   if (true) {
// // // //     var x = "var inside";
// // // //     let y = "let inside";
// // // //   }
// // // //   console.log(x);
// // // //   console.log(typeof y);
// // // // }
// // // // testScope();

// // // // // var inside
// // // // // undefined

// // // // let aa=function(teja){
// // // //     let a=49;
// // // //     console.log(a)
// // // // }
// // // // {console.log(typeof aa())}


// // // // let marks=39
// // // // if (marks>80 && marks<=100){
// // // //     console.log("grade A")
// // // // }
// // // // else if(marks>60 && marks<=80){
// // // //     console.log("Grade B")
// // // // }
// // // // else if(marks>=40 && marks<=60){
// // // //     console.log("Grade C")
// // // // }
// // // // else{console.log("fail")}

// // // // Use a switch case to print the day name when given a number (1–7).

// // // // let a=5

// // // // switch (a){
// // // //     case 1:
// // // //         console.log("monday")
// // // //         break
// // // //     case 2:
// // // //         console.log("tuesday")
// // // //         break
// // // //     case 3:
// // // //         console.log("Wednesday")
// // // //         break
// // // //     case 4:
// // // //         console.log("Thursday")
// // // //         break
// // // //     case 5:
// // // //         console.log("friday")
// // // //         break
// // // //     case 6:
// // // //         console.log("saturday")
// // // //         break
// // // //     case 7:
// // // //         console.log("sunday")
// // // //         break
// // // // }

// // // // let operator="*";
// // // // let a=10;
// // // // let b=5;
// // // // // let c=2

// // // // switch(operator){
// // // //     case "+":
// // // //         console.log(`addtion is ${a+b}`);
// // // //         break
// // // //     case "-":
// // // //         console.log(` substraction ${a-b}`)
// // // //         break
// // // //     case "*":
// // // //         console.log(` multiplication ${a*b}`)
// // // //         break
// // // //     case "/":
// // // //         console.log(`division ${a/b}`)
// // // //         break
// // // // }

// // // // console.log("456" || 1)
// // // // Using if...else if, check a person’s age group:
// // // // below 13 → "Child"
// // // // 13–19 → "Teen"
// // // // 20–59 → "Adult"
// // // // 60+ → "Senior"

// // // // let age=18;

// // // // if (age<13){
// // // //     console.log("Child")
// // // // }else if(age>=13 && age<=19){
// // // //     console.log("teen")
// // // // }else if(age<59 && age>=20){
// // // //     console.log("adult")
// // // // }else{
// // // //     console.log("senior")
// // // // }

// // // // let color="green"
// // // // switch(color){
// // // //     case "red":
// // // //         console.log("Stop")
// // // //         break
// // // //     case "yello":
// // // //         console.log("wait")
// // // //         break
// // // //     case "green":
// // // //         console.log("gooo")
// // // //         break
// // // // }

// // // // let a=0;
// // // // if(a) console.log("truthy");
// // // // else console.log("falsy");

// // // let value = null ?? "fault";    //nullish ( null/undefined)
// // // console.log(value);

// // // let x=0;
// // // let y = x ?? 10;
// // // console.log(y);


// // let n = 22;
// // if (n) console.log("True");
// // else console.log("False");

// let test = 0 || "fallback";
// let check = 0 ?? "fallback";
// console.log(test, check);


// let score = undefined;
// if (score ?? 0 > 50) console.log("Passed");
// else console.log("Failed");
// for(i=4;i<=5;i++){
//     for(j=2;j<=4;j++){
//         console.log(i,j)
//     }
// }

for(let i=0;i<4;i++){
    stars=""
    for(let k=0;k<3-i;k++){
        stars+=" "
    }
    for(let j=0;j<1+i;j++){
        if (i==0 || i==3 || j==0 || j==i){
        stars+=" *"
    }else{
        stars+="  "
    }
    }
    console.log(stars)
}

for (let i=0;i<3;i++){
    star=" "
    for(let k=0;k<0+i;k++){
        star+=" "
    }
    for(let j=0;j<3-i;j++){
        if(i==0 || i==3 || j==0){
            console.log(star+=" *")
        }
    }
    console.log(star)
}