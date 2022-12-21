#!/usr/bin/node
const value = Number(process.argv[2]);
if (value) {
  for (let i = value; i > 0; i--) {
    for (let j = value; j > 0; j--) {
      process.stdout.write('x');
    }
    console.log('');
  }
} else {
  console.log('Missing size');
}
