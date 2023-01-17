#!/usr/bin/node
/*
script that gets contents of a webpage and stores in a file
*/
const url = process.argv[2];
const filePath = process.argv[3];
const fs = require('fs');
const request = require('request');

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    fs.writeFile(filePath, body, 'utf8', function (error, result) {
      if (error) {
        console.log('error', error);
      }
    });
  }
});
