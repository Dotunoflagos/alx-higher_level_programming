#!/usr/bin/node

exports.esrever = function (list) {
  const reverse = [];
  const size = list.length;
  for (let i = size - 1; i >= 0; i--) {
    reverse.push(list[i]);
  }
  return reverse;
};
