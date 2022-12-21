#!/usr/bin/node
const value = Number(process.argv[2]);
let total = 1;

function add (a) {
  if (!a) {
    return;
  }
  total = total * a;
  add(a - 1);
}

add(value);
console.log(total);
