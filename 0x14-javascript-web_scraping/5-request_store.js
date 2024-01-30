#!/usr/bin/node
// a script that gets the contents of a webpage and stores it in a file.
const rq = require('request');
const fs = require('fs');

rq(process.argv[2], function (_err, response, body) {
  fs.writeFile(process.argv[3], body, 'utf8', function (err) {
    if (err) {
      console.log(err);
    }
  });
});
