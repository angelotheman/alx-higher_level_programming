#!/usr/bin/node

const Rectangle = class {
  width;
  height;

  constructor (w, h) {
    this.width = w;
    this.height = h;
  }
};

module.exports = Rectangle;
