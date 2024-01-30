#!/usr/bin/node
// script that displays the number of movies
const rq = require('request');
const weburl = process.argv[2];

rq(weburl, function (err, response, body) {
  if (err) {
    console.error(err);
    return;
  }
  let cnt = 0;
  for (const film of JSON.parse(body).results) {
    for (const character of film.characters) {
      if (character.includes('18')) {
        cnt = cnt + 1;
      }
    }
  }
  console.log(cnt);});
