#!/usr/bin/node
// Square of 5-square.js
const Sqr = require('./5-square.js');
class Square extends Sqr {
	 charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    process.stdout.write((c.repeat(this.width) + '\n').repeat(this.height));
  }
};
