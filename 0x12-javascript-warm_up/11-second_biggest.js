#!/usr/bin/node

let num = 0;
if (process.argv.length >= 4) {
  num = process.argv.slice(2).sort((a, b) => b - a)[1];
}
console.log(num);
