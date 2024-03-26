#!/usr/bin/node

const request = require('request');
const pathURL = process.argv[2];

request(pathURL, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    console.log('code:', response.statusCode);
  }
});
