#!/usr/bin/node

const fs = require('fs');
const request = require('request');
const url = process.argv[2];
const f = process.argv[3];

request(url).pipe(fs.createWriteStream(f));
