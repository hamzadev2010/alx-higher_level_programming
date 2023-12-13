#!/usr/bin/node
//  prints the number of arguments already printed and the new argument value.
let t = 0;
exports.logMe = function (item) {
  console.log(t + ': ' + item);
  t++;
};
