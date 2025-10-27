// // const x= function(a,b){
// //     return a+b
// // };

// // let c=x(2,4);

// // console.log(c);
// // ()

// // (function (){
// //     console.log("hello Raviteja")
// // })
// // ();

// // // ()
// // console.log("hey swami");

// // function myfunction(a,b){
// //     return a*b;
// // }

// // let x=myfunction(3,2)+100

// // console.log(x)

// let myFunction = () => "hello";
// console.log(myFunction())

// function test(callback1, callback2) { 
// callback1(); 
// console.log("2"); 
// callback1(); 
// console.log("8"); 
// callback2(); 
// console.log("9"); 
// callback2(); 
// } 
// test(() => console.log("3"), () => console.log("6"));

// function calculate(callback) { 
// let result = callback(5, 15, 25); 
// console.log(result); 
// } 
// calculate(function (x, y, z) { 
// return x * y - z; 
// }); 

// function sumValues(callback) { 
// let result = callback(2, 3, 4); 
// console.log(result); 
// } 
// sumValues((a, b, c) => a + b * c);

// function print(callback) { 
// callback(); 
// console.log("Finished"); 
// } 
// print(() => console.log("Started"));

// function execute(callback1, callback2) { 
// callback1(); 
// console.log("Middle"); 
// callback2(); 
// } 
// execute(() => console.log("First"), () => console.log("Second")); 

// function operation(callback) { 
// let result = callback(8, 4); 
// console.log(result); 
// } 
// operation((a, b) => a / b);

// function runProcess(callback) { 
// callback(); 
// console.log("Running..."); 
// } 
// runProcess(() => console.log("Started")); 
// runProcess(() => console.log("In Progress"));

// function calc(callback) { 
// let result = callback(10, 5); 
// console.log(result); 
// } 
// calc(function (x, y) { 
// return x - y; 
// });

// function sum(callback) { 
// let result = callback(12, 8, 4); 
// console.log(result); 
// } 
// sum((x, y, z) => x + y - z); 

// function multiply(callback) { 
// let result = callback(3, 5); 
// console.log(result); 
// } 
// multiply((x, y) => x * y); 

// function subtract(callback) { 
// let result = callback(9, 4); 
// console.log(result); 
// } 
// subtract((a, b) => a - b);

// function execute(callback1, callback2) { 
// callback1(); 
// console.log("Step"); 
// callback2(); 
// } 
// execute(() => console.log("Start"), () => console.log("End"));

// function sumValues(callback) { 
// let result = callback(2, 4); 
// console.log(result); 
// } 
// sumValues((x, y) => x + y);

// function divide(callback) { 
// let result = callback(20, 4); 
// console.log(result); 
// } 
// divide((x, y) => x / y);

// function showMessage(callback) { 
// callback(); 
// console.log("Message shown"); 
// } 
// showMessage(() => console.log("Alert!"));

// function calculateResult(callback) { 
// let result = callback(8, 2, 1); 
// console.log(result); 
// } 
// calculateResult((a, b, c) => a - b + c); 

// function funcA(callback1, callback2) { 
// callback1(); 
// console.log("A1"); 
// callback2(); 
// console.log("A2"); 
// } 
// function funcB(callback) { 
// console.log("B1"); 
// callback(); 
// console.log("B2"); 
// } 
// funcA(() => funcB(() => console.log("Inside B")), () => console.log("End of A"));

// function outerFunc(callback) { 
// console.log("Outer Start"); 
// callback(); 
// console.log("Outer End"); 
// } 
// function innerFunc(callback) { 
// console.log("Inner Start"); 
// callback(); 
// console.log("Inner End"); 
// } 
// outerFunc(() => innerFunc(() => console.log("Innermost")));

// function processA(callback1, callback2) { 
// callback1(); 
// callback2(); 
// console.log("ProcessA Done"); 
// } 
// function processB(callback) { 
// console.log("Start ProcessB"); 
// callback(); 
// console.log("End ProcessB"); 
// } 
// processA(() => processB(() => console.log("Inside ProcessB")), () => console.log("End of ProcessA")); 

// function action1(callback1, callback2) { 
// callback1(); 
// console.log("Action 1"); 
// callback2(); 
// } 
// function action2() { 
// console.log("Action 2"); 
// } 
// function action3(callback) { 
// callback(); 
// console.log("Action 3"); 
// } 
// action1(() => action3(() => console.log("Start")), action2); 

// function step1(callback) { 
// console.log("Step 1"); 
// callback(); 
// } 
// function step2(callback1, callback2) { 
// callback1(); 
// console.log("Step 2"); 
// callback2(); 
// } 
// step2(() => step1(() => console.log("Inner Step 1")), () => console.log("Inner Step 2"));

// function first(callback) { 
// console.log("First"); 
// callback(); 
// } 
// function second(callback) { 
// console.log("Second"); 
// callback(); 
// } 
// function third() { 
// console.log("Third"); 
// } 
// first(() => second(third));

// function alpha(callback1, callback2) { 
// console.log("Alpha Start"); 
// callback1(); 
// console.log("Alpha Middle"); 
// callback2(); 
// console.log("Alpha End"); 
// } 
// function beta(callback) { 
// console.log("Beta Start"); 
// callback(); 
// console.log("Beta End"); 
// } 
// function gamma() { 
// console.log("Gamma"); 
// } 
// alpha(() => beta(gamma), () => console.log("Delta"));

// function run1(callback) { 
// console.log("Run1 Start"); 
// callback(); 
// console.log("Run1 End"); 
// } 
// function run2(callback1, callback2) { 
// console.log("Run2 Start"); 
// callback1(); 
// console.log("Run2 Middle"); 
// callback2(); 
// console.log("Run2 End"); 
// } 
// run2(() => run1(() => console.log("Run1 Inner")), () => console.log("Run2 Inner"));

// function firstAction(callback) { 
// console.log("Action 1"); 
// callback(); 
// } 
// function secondAction() { 
// console.log("Action 2"); 
// } 
// function thirdAction(callback) { 
// console.log("Action 3"); 
// callback(); 
// } 
// firstAction(() => thirdAction(secondAction));

// function start(callback1, callback2) { 
// callback1(); 
// console.log("Start"); 
// callback2(); 
// } 
// function middle(callback) { 
// console.log("Middle"); 
// callback(); 
// } 
// function end() { 
// console.log("End"); 
// } 
// start(() => middle(() => console.log("Beginning")), end);

// function funcA(callback1, callback2, callback3) { 
//   console.log("A1"); 
//   callback1(() => { 
//       console.log("A2"); 
//       callback2(); 
//       console.log("A3"); 
//   }); 
//   console.log("A4"); 
//   callback3(); 
//  } 
 
//  function funcB(callback) { 
//   console.log("B1"); 
//   callback(); 
//   console.log("B2"); 
//  } 
 
//  function funcC() { 
//   console.log("C1"); 
//  } 
 
//  funcA((innerCallback) => funcB(innerCallback), () => console.log("End of B"), funcC);

// function firstStep(callback1, callback2) { 
// console.log("First Step Start"); 
// callback1(() => { console.log("First Step Mid"); 
// callback2(); 
// }); 
// console.log("First Step End"); 
// } 
// function secondStep(callback) { 
// // console.log("Second Step Start"); 
// // callback(); 
// // console.log("Second Step End"); 
// // } 
// // function thirdStep(callback) { 
// // console.log("Third Step Start"); 
// // callback(); 
// // console.log("Third Step End"); 
// // } 
// // firstStep(() => secondStep(() => console.log("Inside Second Step")), () => thirdStep(() => console.log("Inside Third Step")));

// function alpha(callback1, callback2, callback3) { 
//   console.log("Alpha Start"); 
//   callback1(() => { 
//       console.log("Alpha Mid"); 
//       callback2(() => { 
//           console.log("Alpha End"); 
//           callback3(); 
//       }); 
//   }); 
//  } 
 
//  function beta(callback) { 
//   console.log("Beta Start"); 
//   callback(); 
//   console.log("Beta End"); 
//  } 
 
//  function gamma() { 
//   console.log("Gamma Start"); 
//   console.log("Gamma End"); 
//  } 
 
//  alpha((innerCallback) => beta(innerCallback), (innerCallback) => beta(innerCallback), gamma); 

// function outer(callback1, callback2, callback3) { 
//   console.log("Outer Start"); 
//   callback1(() => { 
//       console.log("Outer Mid"); 
//       callback2(() => { 
//           console.log("Outer End"); 
//           callback3(); 
//       }); 
//   }); 
//  } 
 
//  function middle(callback) { 
//   console.log("Middle Start"); 
//   callback(); 
//   console.log("Middle End"); 
//  } 
 
//  function inner() { 
//   console.log("Inner Action"); 
//  } 
 
//  outer((cb) => middle(cb), (cb) => middle(cb), inner);


function main(callback1, callback2, callback3) { 
    console.log("Main Start"); 
    callback1(() => { 
        console.log("Main Mid"); 
        callback2(() => { 
          console.log("Main End"); 
          callback3(); 
        }); 
    }); 
} 

function sub1(callback) { 
    console.log("Sub1 Start"); 
    callback(); 
    console.log("Sub1 End"); 
} 

function sub2() { 
    console.log("Sub2 Start"); 
    console.log("Sub2 End"); 
} 

main((cb) => sub1(cb), (cb) => sub1(cb), sub2);