$(function () {
  const URL = 'https://swapi-api.alx-tools.com/api/films/?format=json';

  $.get(URL, function (data) {
    const processMovie = function (movie) {
      $('#list_movies').append('<li>' + movie.title + '</li>');
    };

    data.results.forEach(processMovie);
  });
});
