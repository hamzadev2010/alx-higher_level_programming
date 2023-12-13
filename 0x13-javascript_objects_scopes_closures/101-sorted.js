#!/usr/bin/node
// dictionary of occurrences by user id and computes a dictionary of user ids by occurrence.
const dict = require('./101-data').dict;
const ndict = {};i
Object.getOwnPropertyNames(dict).forEach(n => {
  if (ndict[dict[n]] === undefined) {
    ndict[dict[n]] = [];
  }
  ndict[dict[n]].push(n);
});

console.log(ndict);
