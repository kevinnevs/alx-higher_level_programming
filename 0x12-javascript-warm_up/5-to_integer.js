#!/usr/bin/node
/*
Script that prints "My Number : <first argument converted in integer>"
If the first argument can be converted to integer
If the argument cannot be converted to integer, print "Not a number"
*/

const num = parseInt(process.argv[2]);

if (num) {
  console.log('My number : ' + num);
} else {
  console.log('Not a number');
}
