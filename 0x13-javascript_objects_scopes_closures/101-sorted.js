#!/usr/bin/node
const dict = require('./101-data').dict;
const sortedDict = Object.entries(dict).reduce((acc, cur) => {
  const ids = !acc[cur[1]] ? [] : acc[cur[1]];
  acc[cur[1]] = ids.concat(cur[0]);
  return acc;
}, {});
console.log(sortedDict);
