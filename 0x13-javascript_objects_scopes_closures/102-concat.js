#!/usr/bin/node
// script that concats 2 files.
const fs = require('fs');
const db1 = fs.readFileSync(process.argv[2], 'utf-8');
const db2 = fs.readFileSync(process.argv[3], 'utf-8');
fs.writeFileSync(process.argv[4], db1 + db2, 'utf-8');
