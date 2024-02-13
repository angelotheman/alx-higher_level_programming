#!/usr/bin/node

const addMaybe = (number, theFunction) => {
  number++;
  theFunction(number);
};

module.exports = { addMaybe };
