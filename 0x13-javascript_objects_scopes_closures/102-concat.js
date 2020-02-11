#!/usr/bin/node
const fs = require('fs');
const f1 = process.argv[2];
const f2 = process.argv[3];
const fNew = process.argv[4];
fs.writeFileSync(fNew, fs.readFileSync(f1) + fs.readFileSync(f2));
