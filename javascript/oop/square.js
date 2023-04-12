import Rectangle from './rectangle.js';

export default class Square extends Rectangle {
  constructor(size) {
    super(size, size);
  }

  charPrint(c) {
    if (c === undefined) {
      super.print();
    } else {
      this.print(c);
    }
  }

  print(c) {
    // Function to print rectangle using X
    for (let i = 0; i < this.height; i++) {
      let output = "";
      for (let j = 0; j < this.width; j++) {
        output += c;
      }
      console.log(output);
    }
  }
}
