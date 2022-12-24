#!/usr/bin/node
const int = process.argv;
const length = int.length;
let bigest = Number(int[2]);
let bigest2nd = 0;

if (int === undefined || length < 4) {
  console.log(0);
} else {
  for (let i = 2; i < length; i++) {
    if (Number(int[i]) > bigest) {
      bigest = int[i];
    }
  }
  for (let i = 2; i < length; i++) {
    if (Number(int[i]) < bigest && Number(int[i]) > bigest2nd) {
      bigest2nd = int[i];
    }
  }
  console.log(bigest2nd);
}
