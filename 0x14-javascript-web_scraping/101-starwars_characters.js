#!/usr/bin/node
//a script that prints all characters of a Star Wars movie:
const rq = require('request');
rq.get('https://swapi-api.alx-tools.com/api/' + process.argv[2] + '/', function (err, response, body) {
  if (err) {
    console.log(err);
  }
  const chac = JSON.parse(body).characters;
  for (const characterUrl of chac) {
    await new Promise((res, rej) => {
      rq(characterUrl, (err, response, body) => {
        if (err) {
          rej(err);
        } else {
          console.log(JSON.parse(body).name);
          res();
        }
      });
    });
  }
});
