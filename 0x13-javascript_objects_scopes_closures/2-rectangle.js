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
};
