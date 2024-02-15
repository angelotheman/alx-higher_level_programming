#!/usr/bin/node

const dict = require('./101-data').dict;
const userOccurrences = {};

for (const userId in dict) {
  const occurrences = dict[userId];

  if (!userOccurrences[occurrences]) {
    userOccurrences[occurrences] = [];
  }

  userOccurrences[occurrences].push(userId);
}

console.log(userOccurrences);
