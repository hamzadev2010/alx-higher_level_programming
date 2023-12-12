#!/usr/bin/node
// Display and sorted the biggest number
const num = process.argv;
if (num.length < 4) {
  console.log(0);
} else {
const sortedArgs = num.slice(2).map(Number).sort((x, y) => y - x);
  console.log(sortedArgs.length < 4 ? sortedArgs[2] : 0);
	}
