#!/usr/bin/node
/*
script that prints the title of Star Wars movie
where the episode number matches a given integer
*/
const ID = process.argv[2];
const request = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films/' + ID;
request(url, function (err, response, body) {
  if (err) {
    console.log(err);
  } else if (response.statusCode === 200) {
    body = JSON.parse(body);
    console.log(body.title);
  } else {
    console.log('Error code"' + response.statusCode);
  }
});
