#!/usr/bin/node

function factorial (n) {
  if (isNaN(n) || n <= 1) {
    return 1;
  }
  return factorial(n - 1) * n;
}

const var1 = process.argv[2];
console.log(factorial(var1));
