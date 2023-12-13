#!/usr/bin/node
// returns the number of occurrences in a list.
exports.nbOccurences = function (list, searchElement) {
  let l = 0;
  let i;
  for (i = 0; i < list.length; i++) {
    if (list[i] === searchElement) {
      l += 1;
    }
  }
  return l;
};
