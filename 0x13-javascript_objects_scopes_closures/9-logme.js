#!/usr/bin/node
/*
function that prints no of arguments already printed & the new arg
*/
let n = 0;
exports.logMe = function (item) {
  console.log(n + ' : ' + item);
  n++;
};
