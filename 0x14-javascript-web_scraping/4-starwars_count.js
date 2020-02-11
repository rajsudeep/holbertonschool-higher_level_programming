#!/usr/bin/node

const request = require('request');
const swapi = `${process.argv[2]}`;

request(swapi, (err, res, body) => {
  if (err) throw new Error(err);
  const amount = JSON.parse(body).results.reduce((i, e) => {
    e.characters.forEach((e) => { if (e.includes(18)) { i++; } });
    return i;
  }, 0);
  console.log(amount);
});
