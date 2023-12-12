#!/usr/bin/node
// Display and sorted the biggest number
const num = process.argv;
if (num.length <= 3) {
  console.log(0);
} else {
  console.log(num.sort((a, b) => b - a).slice(3)[0]);
}
