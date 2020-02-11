#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request(url, (err, res, body) => {
  if (err) throw new Error(err);
  const completed = JSON.parse(body).reduce((ids, task) => {
    const i = task.userId;
    if (task.completed) { ids[i] = (ids[i] || 0) + 1; }
    return ids;
  }, {});
  console.log(completed);
});
