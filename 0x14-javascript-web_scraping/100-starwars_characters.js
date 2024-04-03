#!/usr/bin/node

const request = require('request');
const movie_id = process.argv[2]
const apiUrl = 'https://swapi-api.alx-tools.com/api/films/' + movie_id;

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  const filmData = JSON.parse(body);

	const characterUrls = filmData.characters;

	characterUrls.forEach(characterUrl => {
		request(characterUrl, (error, response, body) => {
			if (error) {
				console.error(error);
				return;
			}

			const characterData = JSON.parse(body);

			console.log(characterData.name);
		});
	});
  const characterUrls = filmData.characters;

  characterUrls.forEach(characterUrl => {
    request(characterUrl, (error, response, body) => {
      if (error) {
        console.error(error);
        return;
      }

      const characterData = JSON.parse(body);

      console.log(characterData.name);
    });
  });
});
