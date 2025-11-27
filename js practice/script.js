

// // // // // // // "use strict"
// // // // // // // // "use strict";

// // // // // // // function foo(){
// // // // // // //     a = 2
// // // // // // //   }
// // // // // // //   foo()
// // // // // // //   console.log(a); 


// // // // // // var answer = 0;
// // // // // // const baseValue = value => multipleValue => value * multipleValue;
// // // // // // const multiple = baseValue(2);
// // // // // // answer = multiple(5);
// // // // // // console.log(answer);


// // // // // let data=[
// // // // //   {
// // // // //     "id": 1,
// // // // //     "title": "Fjallraven - Foldsack No. 1 Backpack, Fits 15 Laptops",
// // // // //     "price": 109.95,
// // // // //     "description": "Your perfect pack for everyday use and walks in the forest. Stash your laptop (up to 15 inches) in the padded sleeve, your everyday",
// // // // //     "category": "men's clothing",
// // // // //     "image": "https://fakestoreapi.com/img/81fPKd-2AYL._AC_SL1500_t.png",
// // // // //     "rating": {
// // // // //       "rate": 3.9,
// // // // //       "count": 120
// // // // //     }
// // // // //   },
// // // // //   {
// // // // //     "id": 2,
// // // // //     "title": "Mens Casual Premium Slim Fit T-Shirts ",
// // // // //     "price": 22.3,
// // // // //     "description": "Slim-fitting style, contrast raglan long sleeve, three-button henley placket, light weight & soft fabric for breathable and comfortable wearing. And Solid stitched shirts with round neck made for durability and a great fit for casual fashion wear and diehard baseball fans. The Henley style round neckline includes a three-button placket.",
// // // // //     "category": "men's clothing",
// // // // //     "image": "https://fakestoreapi.com/img/71-3HjGNDUL._AC_SY879._SX._UX._SY._UY_t.png",
// // // // //     "rating": {
// // // // //       "rate": 4.1,
// // // // //       "count": 259
// // // // //     }
// // // // //   },
// // // // //   {
// // // // //     "id": 3,
// // // // //     "title": "Mens Cotton Jacket",
// // // // //     "price": 55.99,
// // // // //     "description": "great outerwear jackets for Spring/Autumn/Winter, suitable for many occasions, such as working, hiking, camping, mountain/rock climbing, cycling, traveling or other outdoors. Good gift choice for you or your family member. A warm hearted love to Father, husband or son in this thanksgiving or Christmas Day.",
// // // // //     "category": "men's clothing",
// // // // //     "image": "https://fakestoreapi.com/img/71li-ujtlUL._AC_UX679_t.png",
// // // // //     "rating": {
// // // // //       "rate": 4.7,
// // // // //       "count": 500
// // // // //     }
// // // // //   },
// // // // //   {
// // // // //     "id": 4,
// // // // //     "title": "Mens Casual Slim Fit",
// // // // //     "price": 15.99,
// // // // //     "description": "The color could be slightly different between on the screen and in practice. / Please note that body builds vary by person, therefore, detailed size information should be reviewed below on the product description.",
// // // // //     "category": "men's clothing",
// // // // //     "image": "https://fakestoreapi.com/img/71YXzeOuslL._AC_UY879_t.png",
// // // // //     "rating": {
// // // // //       "rate": 2.1,
// // // // //       "count": 430
// // // // //     }
// // // // //   },
// // // // //   {
// // // // //     "id": 5,
// // // // //     "title": "John Hardy Women's Legends Naga Gold & Silver Dragon Station Chain Bracelet",
// // // // //     "price": 695,
// // // // //     "description": "From our Legends Collection, the Naga was inspired by the mythical water dragon that protects the ocean's pearl. Wear facing inward to be bestowed with love and abundance, or outward for protection.",
// // // // //     "category": "jewelery",
// // // // //     "image": "https://fakestoreapi.com/img/71pWzhdJNwL._AC_UL640_QL65_ML3_t.png",
// // // // //     "rating": {
// // // // //       "rate": 4.6,
// // // // //       "count": 400
// // // // //     }
// // // // //   }
// // // // // ]

// // // // // for(let i=0;i<data;i++){
// // // // //     console.log(data[i].rating)
// // // // // }


// // // // // let obj = {
// // // // //   namee:"teja"
// // // // // }
// // // // // obj.freeze
// // // // // console.log(obj,"hii")
// // // // // // console.log(obj.namee)
// // // // // delete obj.namee

// // // // // console.log(obj)

// // // // let obj = {a:1, a:2};
// // // // console.log(obj.a);

// // // let user = {
// // //   name:"Ram",
// // //   greet(){ return "Hi " + this.name }
// // // }; 
// // // structuredClone
// // // console.log(user.greet());


// // // let obj=new Object({name:"sanjeev"})
// // // // let c={...obj}
// // // // let new=Object.assign({},obj)

// // // c.name="ravi"
// // // console.log(obj,c)

// // // ar=[]

// // // ar.push(2,3)
// // // console.log(ar)


// // // console.log(Object.entries(c))

// // // let obj={
// // //   name:"teja",
// // //   roll:"21673"
// // // }

// // // console.log(Object.entries(obj))
// // // console.log()

// // // let obj=new Object({age:21,namee:"teja"})
// // // let c=Object.assign([],obj)
// // // let x=Object.assign({},obj)

// // // // Object.seal(obj)
// // // Object.freeze(obj)
// // // // used to prevent adding/removing properties , but can modify\update the value
// // // // read only purpose , can't remove/add or change the values
// // // // obj.namee="tejjj"
// // // console.log(Object.isFrozen(c))

// // // delete obj.namee
// // // console.log(obj)

// // // c.age=22
// // // console.log(c)
// // // console.log(x)

// // let ab={
// //   name:"hello",
// //   role:"trainer",
// //   work:"teaching"
// // }

// // for(let i in ab){
// //   console.log(i)
// // }

// // console.log(a)
// // const a=10;

// var a = 10;

// {
//   let a = 20; // ❌ Not allowed
// }

// console.log(a)

let element=document.getElementsByTagName("div")
element[0].addEventListener("click",function(){
    console.log("first")
})

element[1].addEventListener("click",function(){
    console.log("middle")
})

element[2].addEventListener("click",function(){
    console.log("last")
})