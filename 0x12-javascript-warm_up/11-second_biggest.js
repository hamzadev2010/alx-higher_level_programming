#!/usr/bin/node
// Display and sorted the biggest number
if (process.argv.length < 4) {
  console.log('0');
} else {
  const num = process.argv.slice(2).map(Number);
  const numsort = num.sort((a, b) => b - a);
  console.log(num.length >= 3 ? num[2] : '0');
}
