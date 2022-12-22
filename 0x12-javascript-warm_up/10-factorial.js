#!/usr/bin/node
const value = Number(process.argv[2]);

function add (a) {
  if (a === 0) {
    return (1);
  } else {
    return (a * add(a - 1));
  }
}

if (isNaN(value)) {
    console.log('1');
  } else {
    console.log(add(value));
  }
