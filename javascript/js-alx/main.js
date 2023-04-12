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


console.log(nbOccurences([1, 2, 3, 4, 5, 6], 3));
console.log(nbOccurences([3, 2, 3, 4, 5, 3, 3], 3));
console.log(nbOccurences(["S", 12, "c", "S", "School", 8], "S"));
