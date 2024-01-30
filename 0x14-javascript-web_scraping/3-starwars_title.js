#!/usr/bin/node
//  a script that prints the title of a Star Wars
//  movie where the episode number matches a given integer.
const rq = require('request');
const process = require('process');
const weburl = ' https://swapi-api.alx-tools.com/api/films/'.concat(process.argv[2]);
const episodeNum = process.argv[2];

rq(weburl, function (err, response, body) {
  if (err) {
    console.log(err);
  } else if (response.statusCode === 200) {
    const jsonObj = JSON.parse(body);
    console.log(jsonObj.title);
  }
});
