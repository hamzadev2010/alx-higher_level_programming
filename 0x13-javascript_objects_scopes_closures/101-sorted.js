#!/usr/bin/node
// dictionary of occurrences by user id
// and computes a dictionary of user ids by occurrence.
const dict = require('./101-data').dict;
console.log(Object.entries(dict).reduce(function (n, index) { {
  n[index[1]] = (n[index[1]] || []).concat(index[0]);
  return n;
}, {}));
