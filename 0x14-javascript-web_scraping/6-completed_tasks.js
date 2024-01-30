#!/usr/bin/node
// a script that computes the number of tasks completed by user id.
const rq = require('request');

rq(process.argv[2], function (err, response, body) {
  if (er) {
    console.log(err);
  } else {
    const dt = JSON.parse(body);
    const rsl = {};
    for (let i = 0; i < dt.length; i++) {
      if (dt[i].completed === true) {
        const todo = dt[i];
        if (rsl[todo.userId] === undefined) {
          rsl[todo.userId] = 0;
        }
        rsl[todo.userId]++;
      }
    }
    console.log(rsl);
  }
});
