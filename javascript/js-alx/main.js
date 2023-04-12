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
console.log(list);
console.log(newList);