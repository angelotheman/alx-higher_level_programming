#!/usr/bin/node

const callMeMoby = (x, theFunction) => {
  while (x > 0) {
    theFunction();
    x--;
  }
};

module.exports = { callMeMoby };
