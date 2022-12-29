#!/usr/bin/node
// Abstraction in JS
function Circle(radius) {
  this.radius = radius;
  let defaultLocation = {x: 0, y: 0}; //Private members in JS
  let computeOptimumLocation = function() { //Private members in JS
    // ...
  };

  this.getDefaultLocation = function() {
    return defaultLocation;
  };

  this.draw = function () {
    computeOptimumLocation(0.1);
    console.log(defaultLocation);
    console.log('draw');
  };

  Object.defineProperty(this, 'defaultLocation', {
    get: function() {
      return defaultLocation;
    },
    set: function(value) {
      if (!value.x || !value.y) {
        throw new Error('Invalid location.');
      }
      defaultLocation = value;
    }
  });
}

const circle = new Circle(10);

console.log(circle);