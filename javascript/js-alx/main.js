// TODO: Task 7
// const nbOccurences = (arr, item) => {
//   const newArr = arr.filter((obj) => obj === item);
//   return newArr.length;
// };

const nbOccurences = (arr, item) => {
  let count = 0;
  for (let i = 0; i < arr.length; i++) {
    if (arr[i] === item) {
      count++;
    }
  }
  return count;
}

// console.log(nbOccurences([1, 2, 3, 4, 5, 6], 3));
// console.log(nbOccurences([3, 2, 3, 4, 5, 3, 3], 3));
// console.log(nbOccurences(["S", 12, "c", "S", "School", 8], "S"));


// TODO: Task 8
const esrever = (list) => {
  let newArr = [];
  for (let i = list.length - 1; i >= 0; i--) {
    newArr.push(list[i]);
  }
  return newArr;
}

// console.log(esrever([1, 2, 3, 4, 5]));
// console.log(esrever(["School", 89, { id: 12 }, "String"]));


// TODO: Task 9
var count = 0;
const logMe = (item) => {
  console.log(count + ": " + item);
  count++;
}

// logMe("Hello");
// logMe("Best");
// logMe("School");


// TODO: Task 10
const converter = (base) => {
  return function (num) {
    return num.toString(base);
  }
}

// let myConverter = converter(10);

// console.log(myConverter(2));
// console.log(myConverter(12));
// console.log(myConverter(89));


// myConverter = converter(16);

// console.log(myConverter(2));
// console.log(myConverter(12));
// console.log(myConverter(89));


// TODO: Task 11
const list = [1, 2, 3, 4, 5];
const newList = list.map((num, i) => num * i);
// console.log(list);
// console.log(newList);


// TODO: Task 12
const dict = {
  89: 1,
  90: 2,
  91: 1,
  92: 3,
  93: 1,
  94: 2
};

// const obj = {};

// const keys = Object.values(dict);

// const objKeys = Object.assign(...keys, {});
// for (let key of keys) {
//   obj[key] = []
// }
const computeDict = arr => {
  let obj = {};
  const keys = Object.values(dict);
  // console.log(keys)
  for (let key of keys) {
    obj[key] = []
  }
  for (let i = 0; i < arr.length; i++) {
    if (arr[i][1] in obj) {
      obj[arr[i][1]].push(arr[i][0]);
    }
  }
  return obj;
}

const arr = Object.entries(dict);
const obj = computeDict(arr);
console.log(obj);