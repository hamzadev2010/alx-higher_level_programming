#!/usr/bin/node
// a script that prints the title of a Star Wars
// movie where the episode number matches a given integer
const rq = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/'  + args[2]);

rq(url, function (_err, rs, bd) {
  bd = JSON.parse(bd);
  console.log(bd.title);
});
