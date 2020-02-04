#!/usr/bin/node

let str = 'No argument';
if (process.argv.length === 3) {
  str = 'Argument found';
} else if (process.argv.length > 3) {
  str = 'Arguments found';
}
console.log(str);
