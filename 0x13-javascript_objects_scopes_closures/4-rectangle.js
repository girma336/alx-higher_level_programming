#!/usr/bin/node
module.exports = class Rectangle {
  constructor (w, h) {
    if (w <= 0 || w === undefined) { return this; } else if (h <= 0 || h === undefined) { return this; } else {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      console.log('X'.repeat(this.width));
    }
  }

  rotate () {
    const temp = this.width;
    this.width = this.height;
    this.height = temp;
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }
};
