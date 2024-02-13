#!/usr/bin/node

const args = process.argv;

if (args.length <= 3) {
  console.log(0);
} else {
  let max = args[2];
  let secondMax = args[3];

  for (let i = 3; i < args.length; i++) {
    const current = args[i];
    if (current > max) {
      secondMax = max;
      max = current;
    } else if (current > secondMax && current !== max) {
      secondMax = current;
    }
  }

  console.log(secondMax);
}
