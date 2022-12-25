#!/usr/bin/node
const par = require('./5-square.js');

class Square extends par {

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
