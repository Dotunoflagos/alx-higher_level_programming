#!/usr/bin/node

function add (a, b) {
  console.log(a + b);
}

const value = Number(process.argv[2]);
const value2 = Number(process.argv[3]);
if (value && value2) {
  add(value, value2);
} else {
  console.log('NaN');
}
