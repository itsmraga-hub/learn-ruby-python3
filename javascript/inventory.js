// Challenge: 

// Compare and update the inventory stored in a 2D array against a second 2D array of a fresh delivery. Update the current existing inventory item quantities (in currentInventory). If an item cannot be found, add the new item and quantity into the inventory array. The returned inventory array should be in alphabetical order by item.


// Example inventory lists:
let currentInventory = [ [21, "Bowling Ball"], [2, "Dirty Sock"], [1, "Hair Pin"], [5, "Microphone"] ]; 

let newInventory = [ [2, "Hair Pin"], [3, "Half-Eaten Apple"], [67, "Bowling Ball"], [7, "Toothpaste"] ];

//result: currentInventory = [[88, “Bowling Ball”], [2, “Dirty Sock”], [3, “Hair Pin”], [3 “Half-Eaten Apple”], [5, “Microphone”], [7, “Toothpaste”]]


const addNewInventory = (list_1, list_2) => {
  const len = list_1.length;
  for (let i = 0; i < len; i++) {
    for (let j = 0; j < list_2.length; j++) {
      if (list_1[i][1] === list_2[j][1]) {
        list_1[i][0] += list_2[j][0];
        list_2.splice(j, 1);
      }
    }
  }
  // for (let i = 0; i < list_2.length; i++) {
  //   list_1.push(list_2[i]);
  // }
  list_1 = list_1.concat(list_2);

  list_1.sort((a, b) => {
    if (a[1] < b[1]) {
      return -1;
    }
    if (a[1] > b[1]) {
      return 1;
    }
    // a must be equal to b
    return 0;
  })
  

  return list_1;
};

console.log(addNewInventory(currentInventory, newInventory));

