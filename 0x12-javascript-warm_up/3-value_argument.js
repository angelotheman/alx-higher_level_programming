#!/usr/bin/node

const arg = process.argv;

if (!arg[2]) {
  console.log('No argument');
} else {
  console.log(arg[2]);
}
