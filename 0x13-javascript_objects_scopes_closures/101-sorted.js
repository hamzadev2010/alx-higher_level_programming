#!/usr/bin/node
// dictionary of occurrences by user id
// and computes a dictionary of user ids by occurrence.
const dict = require('./101-data').dict;
const sortAndOrganize = (obj) => {
  const rs = {};
  Object.entries(obj).forEach(([k, v]) => {
    rs[v] = result[v] || [];
    rs[v].push(k);
  });

	return rs;
};
const nDict = sortAndOrganize(dict);
console.log(nDict);
