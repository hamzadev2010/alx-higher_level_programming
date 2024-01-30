#!/usr/bin/node
// reads and display the content of a file.
const fs = require('fs');
const arg = process.argv;

fs.readFile(arg[2], 'utf-8', (err, data) => {
  if (err) { console.log(err); } else {
    console.log(data);
  }
});
