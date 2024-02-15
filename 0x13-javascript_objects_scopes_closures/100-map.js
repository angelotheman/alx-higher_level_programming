#!/usr/bin/node

const list = require('./100-data').list;
const newList = list.map((x, y) => x * y);

console.log(list);
console.log(newList);
