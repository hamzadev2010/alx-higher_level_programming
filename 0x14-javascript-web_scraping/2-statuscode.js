#!/usr/bin/node
//  a script that display the status code of a GET request.
const rq = require('request');

rq.get(process.argv[2]).on('response', function (response) {
    console.log(`code: ${response.statusCode}`);
  });
