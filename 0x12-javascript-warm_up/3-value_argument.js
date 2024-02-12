#!/usr/bin/node

const arg = process.argv;

if (arg[2] === undefined) {
  console.log('No Argument');
} else {
  console.log(arg[2]);
}
