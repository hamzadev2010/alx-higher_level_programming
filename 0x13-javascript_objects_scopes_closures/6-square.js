#!/usr/bin/node
// Square of 5-square.js
const sq = require('./5-square.js');
class Square extends sq {
  charPrint (ch) {
	  if (!ch) {
    c = 'X';
  }
  for (let i = 0; i < this.width; i++) {
    console.log(ch.repeat(this.width));
  }
};

module.exports = Square;
