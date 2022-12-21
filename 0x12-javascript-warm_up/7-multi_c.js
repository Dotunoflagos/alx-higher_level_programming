#!/usr/bin/node
const value = Number(process.argv[2]);
if (value) {
  for (let i = value; i > 0; i--) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
