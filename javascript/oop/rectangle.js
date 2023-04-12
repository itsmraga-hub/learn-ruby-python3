export default class Rectangle {
  constructor(w, h) {
    if (w > 0 && h > 0) {
        this.width = w;
        this.height = h;
    }
  }

  print() {
    // Function to print rectangle using X
    for (let i = 0; i < this.height; i++) {
      let output = "";
      for (let j = 0; j < this.width; j++) {
        output += "X";
      }
      console.log(output);
    }
  }

  rotate() {
    // Function to exchange the width and height
    let temp = this.height;
    this.height = this.width;
    this.width = temp;
  }

  double() {
    // Function that doubles the width and height by 2
    this.height *= 2;
    this.width *= 2;
  }
}


