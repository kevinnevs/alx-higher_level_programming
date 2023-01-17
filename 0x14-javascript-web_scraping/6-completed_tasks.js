#!/usr/bin/node
/*
script that computes the num of tasks completed bu user id
*/
const url = process.argv[2];
const request = require('request');

request(url, function (err, response, body) {
  if (err) {
    console.log(err);
  } else if (response.statusCode === 200) {
    const completedTask = JSON.parse(body);
    const allDone = {};
    for (const i in completedTask) {
      if (completedTask[i].completed) {
        if (allDone[completedTask[i].userId] === undefined) {
          allDone[completedTask[i].userId] = 1;
        } else {
          allDone[completedTask[i].userId]++;
        }
      }
    }
    console.log(allDone);
  } else {
    console.log('Error code: ' + response.statusCode);
  }
});
