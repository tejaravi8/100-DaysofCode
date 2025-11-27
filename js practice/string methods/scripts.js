// // ✅ 1. length
// // let namee="LEngth";
// // console.log(namee.length)

// // // Tells how many characters are in the string.

// // ✅ 2. toUpperCase() / toLowerCase()
// // let n="TeJaa";
// // console.log(n.toUpperCase())
// // console.log(n.toLowerCase())

// // ✅ 3. trim()
// // Removes spaces at the beginning and end.

// // console.log("   hello   ".trim().length); // "hello"

// // ✅ 4. slice(start, end)
// // Cut a portion of string.
// // console.log("JavaScript".slice(0, 4)); // "Java"
// // console.log("JavaScript".slice(-10));    // "Script"

// // ✅ 5. substring(start, end)

// // Similar to slice (but does not support negative values).
// // console.log("JavaScript".substring(3,7))

// // ✅ 6. replace(old, new)

// // let string="hello world"
// // console.log(string.replace("world", "Teja")); // "hello Teja"
// // console.log(string.replace("hello","bye"));  // "bye world"

// // 7. replaceAll()
// // console.log("a bab a".replaceAll("a", "xx"));
// //              xx bxxb xx

// // ✅ 8. includes()
// // Checks if a substring exists.

// // console.log("javascript".includes("script")); // true

// // ✅ 9. indexOf()

// // Position of a character/word.

// // console.log("hello".indexOf("o"));  // 2

// // ✅ 10. split()

// // Converts a string → array.

// // console.log("apple,banana,grapes".split(","));
// // ["apple","banana","grapes"]

// // console.log(//"applebananagrapes".split()

// // console.log("tejaie".match(/[a,e,i,o,u]/gi));

// // ✅ 11. concat()

// // Add strings.

// // console.log("Hello".concat(" Tejaasdfghj"));
// // // "Hello Teja"

// // ✅ 12. charAt()

// // Get character at a position.

// console.log("Teja".charAt(4)); // "e"

// let words="hello all how r u";
// let x=["hello","hi","bye"].filter(i=>i.length>2)
// console.log(x)
// console.log(words.reduce())

let nums=[];

// let odds=nums.filter(a=>a%2==1);
// console.log(odds)

let totals = nums.reduce((acc,curr)=>acc+curr,99)

console.log(totals)