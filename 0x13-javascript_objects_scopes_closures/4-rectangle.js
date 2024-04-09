#!/usr/bin/node
module.exports = class Rectangle {
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
    let rotate = this.height;
    this.height = this.width;
    this.width = rotate;
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }
};
