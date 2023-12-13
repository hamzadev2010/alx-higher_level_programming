#!/usr/bin/node
// dictionary of occurrences by user id
// and computes a dictionary of user ids by occurrence.
const dict = require('./101-data').dict;
const nDict = {};
for (const i in dict) { {
	if (nDict[dict[`${i}`]] === undefined) {
    nDict[dict[`${i}`]] = [];
  }
  nDict[dict[`${i}`]].push(i);
}
console.log(nDict);
