#!/usr/bin/node

function checkMax (a, b) {
  return a > b ? a : b;
}

const args = process.argv;

if (args.length <= 3) {
  console.log(0);
} else {
  let max = args[2];

  for (let i = 3; i < args.length; i++) {
    max = checkMax(max, args[i]);
  }

  console.log(max);
}
