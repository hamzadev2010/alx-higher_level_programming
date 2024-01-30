#!/usr/bin/node
//a script that writes a string to a file
const fs = require('fs');
const cn = process.argv[3];

fs.writeFile(process.argv[2], cn, function (err) {
  if (err) {
    console.log(err);
  }
});
