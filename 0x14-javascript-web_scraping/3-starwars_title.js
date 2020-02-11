#!/usr/bin/node

const request = require('request');
const swapi = 'http://swapi.co/api/films/:id';

request(swapi, (err, res, body) => {
  err ? console.log(err) : console.log(JSON.parse(body).title);
});
