#!/usr/bin/node
/*
Javascript scrip that prints the following :
If no arguments are passed to the script print "No argument"
If argument is passed to the script print "Argument found"
Otherwise print "Arguments found"
*/

if (process.argv.length === 2) {
  console.log('No argument');
} else if (process.argv.length === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
