#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let i = this.height; i > 0; i--) {
      for (let j = this.width; j > 0; j--) {
        process.stdout.write('X');
      }
      console.log('');
    }
  }

  rotate () {
    const temp = this.height;
    this.height = this.width;
    this.width = temp;
  }

  double () {
    const temph = this.height;
    const tempw = this.width;
    this.height = temph * 2;
    this.width = tempw * 2;
  }
}
module.exports = Rectangle;
