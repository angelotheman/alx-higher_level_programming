#!/usr/bin/node

const request = require('request');
const id = process.argv[2]
const URL = 'https://swapi-api.alx-tools.com/api/films/' + id;

request(URL, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const filmData = JSON.parse(body);
    console.log(filmData.title);
  }
});
