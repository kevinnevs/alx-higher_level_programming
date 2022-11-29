#!/usr/bin/node
/*
script that prints a square
if the first argument can't be converted to an integer,
print 'Missing size'
*/
const num = parseInt(process.argv[2]);

if (num) {
  for (let i = 0; i < process.argv[2]; i++) {
    console.log('X'.repeat(num));
  }
} else if (num < 0) {
  console.log('');
} else {
  console.log('Missing size');
}
