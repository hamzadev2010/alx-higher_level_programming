#!/usr/bin/node
// dictionary of occurrences by user id
// and computes a dictionary of user ids by occurrence.
const dict = require('./101-data').dict;
Object.keys(dict).map(function (n, index) { {
  n[index[1]] = (n[index[1]] || []).concat(index[0]);
  return n;
}, {}));
