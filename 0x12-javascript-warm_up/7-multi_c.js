#!/usr/bin/node
// Display c is fun specifique time
let displayss = parseInt(process.argv[2]);
if (isNaN(displayss)) {
  console.log('Missing number of occurences');
} else {
  while (displayss > 0) {
    console.log('C is fun');
    displayss--;
  }
}
