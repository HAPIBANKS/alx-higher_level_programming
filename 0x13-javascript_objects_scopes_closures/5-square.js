#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let j;
    for (j = 0; j < this.height; j++) {
      console.log('X'.repeat(this.width));
    }
  }

  rotate () {
    const rotate = this.height;
    this.height = this.width;
    this.width = rotate;
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }
}
module.exports = class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }
};
