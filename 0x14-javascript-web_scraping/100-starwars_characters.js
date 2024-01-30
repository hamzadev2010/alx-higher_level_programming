#!/usr/bin/node
//a script that displays all characters of a Star Wars movie:
const rq = require('request');
const weburl = 'https://swapi-api.hbtn.io/api/films/'.concat(process.argv[2]);

rq(weburl, function (err, response, body) {
  const characters = JSON.parse(body).characters;

  for (let i = 0; i < characters.length; ++i) {
    rq(characters[i], function (err1, response1, body1) {
      console.log(JSON.parse(body1).name);
    });
  }
});
