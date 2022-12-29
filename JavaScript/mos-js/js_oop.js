#!/usr/bin/node
// OOP IN JS
let baseSalary = 30_000;
let overTime = 10;
let rate = 20;

function getWage(baseSalary, overTime, rate) {
  return baseSalary + (overTime * rate);
}
// encapsulation
let employee = {
  baseSalary: 30_000,
  overTime: 10,
  rate: 20,
  getWage: function() {
    return this.baseSalary + (this.overTime * this.rate);
  }
};

console.log(employee.getWage());

// Objects like a dictionary in python
const circle = {
  radius: 1,
  location: {
    x: 1,
    y: 1
  },
  draw: function() {
    console.log('draw');
  }
};

circle.draw();

// Factories and Constructors
// Factory Function
function createCircle(radius) {
  return {
    // radius: radius,
    radius, //new es6 standard --> only if key and value are the same
    draw: function() {
      console.log('draw');
    }
  };
};

const circleR5 = createCircle(5);
console.log(circleR5.radius);
circleR5.draw();

// Constructor Function
function Circle(radius) {
  this.radius = radius;
  this.draw = function() {
    console.log('draw');
  }
  console.log(this);
}
const circleR7 = new Circle(7);
console.log(circleR7.radius);

// New ES6 version
class Circle2 {
  constructor(radius) {
    this.radius = radius;
    this.draw = function () {
      console.log('draw');
    };
    console.log(this);
  }
}
const circleR8 = new Circle2(8);
console.log(circleR8.radius);
console.log(circleR8.name);

// Adding properties to objects
const circle1 = new Circle(10);
circle1.location = {x: 1};
console.log(circle1);
circle1.area = function () {
  console.log(3.14 * this.radius * this.radius);
}
console.log(circle1.area())

// deleting properties from objects
delete circle1.area;
console.log(circle1);

// iterating through properties
for (let key in circle1) {
  console.log(key, circle1[key]);
}

const keys = Object.keys(circle1);
console.log(keys);

if ('radius' in circle1) {
  console.log('Radius found!!');
}