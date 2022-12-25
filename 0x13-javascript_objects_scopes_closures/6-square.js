#!/usr/bin/node
const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (c !== undefined) {
      for (let i = this.height; i > 0; i--) {
        for (let j = this.width; j > 0; j--) {
          process.stdout.write('C');
        }
        console.log('');
      }
    } else {
      this.print();
    }
  }
}
module.exports = Square;
