#!/usr/bin/node
// returns the reversed version of a list.
exports.esrever = function (list) {
  const lis = [];
  for (let i = list.length - 1; i >= 0; i--) {
    lis.push(list[i]);
  }
  return lis;
};
