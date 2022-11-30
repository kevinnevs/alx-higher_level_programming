#!/usr/bin/node
/*
function that converts num frm base 10 to another base passsed as argument
*/
exports.converter = function (base) {
  return function mainConvert (num) {
    return num.toString(base);
  };
};
