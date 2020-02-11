#!/usr/bin/node

const fs = require('fs');
const f = process.argv[2];
const data = process.argv[3];

fs.writeFile(f, data, (err) => {
  err && console.log(err);
});
