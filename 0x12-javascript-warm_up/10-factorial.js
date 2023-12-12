#!/usr/bin/node
// Dispyql factorial
const c = parseInt(process.argv[2]);
function Facto (c) {
  if ((Number.isNaN(c)) || (c === 1)) {
    return 1;
  }
  return Facto(c - 1) * c;
}
console.log(Facto(c));
