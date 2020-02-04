#!/usr/bin/node

function add (a, b) {
  return parseInt(a) + parseInt(b);
}

const var1 = process.argv[2];
const var2 = process.argv[3];
console.log(add(var1, var2));
