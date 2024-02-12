#!/usr/bin/node

const arg = process.argv[2];
let num = parseInt(arg);

if (isNaN(num)) {
  console.log('Missing number of occurrences');
}

while (num > 0) {
  console.log('C is fun');
  num--;
}
