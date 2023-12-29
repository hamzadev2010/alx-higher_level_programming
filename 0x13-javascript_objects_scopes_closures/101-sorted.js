#!/usr/bin/node
// dictionary of occurrences by user id and computes a dictionary of user ids by occurrence.
const dict = require('./101-data').dict;
const ndict = {};
for ( const n in dict ) {
  if (ndict[dict[n]] === undefined) {
    ndict[dict[n]] = [n];
  }
  ndict[dict[n]].push(n);
});
console.log(ndict);
