#!/usr/bin/node
const fs = require('fs');

const args = process.argv[2];
fs.readFile(args, 'utf8', (err, data) => {
  if (err) {
    console.log(err);
    return;
  }
  console.log(data);
});
