#!/usr/bin/node
// Script for x time
exports.callMeMoby = function (x, theFunction) {
  let i;
  for (i = 0; i < x; i++) {
    theFunction();
  }
};
