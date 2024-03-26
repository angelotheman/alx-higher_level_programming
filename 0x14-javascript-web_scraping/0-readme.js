#!/usr/bin/node

const fs = require('fs');
const filePath = process.argv[2];

fs.readFile(filePath, { encoding: 'utf-8' }, function (err, data) {
  if (err) return console.error(err);
  console.log(data);
});
