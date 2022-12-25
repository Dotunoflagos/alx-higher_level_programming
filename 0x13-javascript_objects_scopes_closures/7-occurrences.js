#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  const size = list.length;
  let occour = 0;
  for (let i = 0; i < size; i++) {
    if (list[i] === searchElement) {
      occour++;
    }
  }
  return occour;
};
