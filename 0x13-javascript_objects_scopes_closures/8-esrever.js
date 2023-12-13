#!/usr/bin/node
// returns the reversed version of a list.
exports.esrever = function (list) {
  const lis = [];
  for (const it of list) {
    lis.push(list[it]);
  }
  return lis;
};
