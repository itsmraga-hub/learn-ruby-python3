// Define variables
// let, const, var
// let and const are block scoped {}
// let - can be reassigned 

let name = "William"
name = "Charles"

const num = 4

// if (num == 4) {
//   var v = "charles"
//   console.log(v)
// } else {
//   console.log(name)
//   console.log(v)
// }

// console.log(v)

// Datatypes
// Number - 6, 9.0
// String -"jsjadhs"
// Array - []
// Set
// Objects - Dictionaries key, value
// 

let str = []

const obj = {
  name: "William",
  age: 25,
  course: "Mathematics"
}

// obj = 9

// console.log(obj.name)
// obj.name = "Charles"
// console.log(obj.name)


// const arr = [1, 2, 3, 4, 5, 6];
// for (let i = arr.length - 1; i >= 0; i--) {
//   // console.log(i)
//   console.log(arr[i])
// }

// For loop
// While loop
// do... while
// let i = 1
// for (; i <= 50;) {
//   console.log(i)
//   i = i * 3
// }

// let flag = true;
// let count = 0
// while (flag) {
//   console.log(`${count}: You Win!!!`)
//   count++;
//   if (count == 10) {
//     break;
//   } else {
//     // 
//     // 
//     if () {
//       continue;
//     } else
//   }
// }


// let a = 5
// let b = 9
// let c = a + b;

let a = 90;
let b = 89;
// let c = a + b;

const add = function (a, b) {
  return a + b;
}

let c = add(90, 78);
console.log(c);


const arr = [1, 2, 3, 4, 5, 6];

function addArray(arr) {
  let sum = 0;
  for (let i = 0; i < arr.length; i++) {
    sum += arr[i];
  }
  return sum;
}

const total = addArray([9, 8, 6]);
const t = addArray([5, 9, 89, 78, 45, 23])
console.log(total)
console.log(t)