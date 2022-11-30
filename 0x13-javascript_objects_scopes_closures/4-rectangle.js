#!/usr/bin/node
/*
Class rectangle that defines a rectangle
*/
module.exports = class Rectangle {
  constructor (w, h) {
    if (w && h > 0) {
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
    this.width = [this.height, this.height = this.width][0];
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }
};
