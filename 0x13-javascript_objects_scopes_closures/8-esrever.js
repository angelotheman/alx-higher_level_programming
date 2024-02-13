#!/usr/bin/node

exports.esrever = function (list) {
  const reversed = [];
  let i = list.length - 1;

  while (i >= 0) {
    reversed.push(list[i]);
    i--;
  }

  return reversed;
};
