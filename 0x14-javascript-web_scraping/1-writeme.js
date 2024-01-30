#!/usr/bin/node
//a script that writes a string to a file

const fs = require('fs');
const cn = process.argv[3];
const cn2 = process.argv[2];

fs.writeFile(cn2, cn, 'utf8', function (err) {
  if (err) {
    console.log(err);
  }
});
