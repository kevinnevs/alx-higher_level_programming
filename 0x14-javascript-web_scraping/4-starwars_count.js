#!/usr/bin/node
/*
script that print the num of movies where
the character "Wedge Antilles" is present
*/
const request = require('request');
const url = process.argv[2];
const characterid = '18';

request(url, function (err, response, body) {
  if (err) {
    console.log(err);
  } else if (response.statusCode === 200) {
    let count = 0;
    const films = JSON.parse(body).results;
    for (const i in films) {
      const chars = films[i].characters;
      for (const c in chars) {
        if (chars[c].includes(characterid)) {
          count++;
        }
      }
    }
    console.log(count);
  } else {
    console.log('Error code:' + response.statusCode);
  }
});
