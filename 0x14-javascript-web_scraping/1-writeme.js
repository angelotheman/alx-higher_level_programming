#!/usr/bin/node

const fs = require('fs');
const filePath = process.argv[2];
const content = process.argv[3];

fs.writeFile(filePath, content, { encoding: 'utf-8' }, function (err, data) {
  if (err) return console.error(err);
  console.log(data);
});
