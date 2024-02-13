#!/usr/bin/node

const squareIn = require('./5-square');

const Square = class extends squareIn {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }

    for (let i = 0; i < this.height; i++) {
      console.log(c.repeat(this.width));
    }
  }
};

module.exports = Square;
