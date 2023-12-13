#!/usr/bin/node
// Square of 5-square.js
const Sqr = require('./5-square');
module.exports = class Square extends Sqr {
	 charPrint (c) {
    for (let i = 0; i < this.width; i++) {
      if (c === undefined) {
        console.log('X'.repeat(this.height));
      } else {
        console.log(c.repeat(this.height));
      }
    }
  }
}
