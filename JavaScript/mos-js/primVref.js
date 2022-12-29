#!/usr/bin/node
// Primitives vs Reference Types
// Primitives are independent of each other
let x = 10;
let y = x;

x = 20;

console.log(x);
console.log(y);
// References point to a location of item in memory
// When reasigned we actually share the location rather than copying the value
let xOb = {value: 10};
let yOb = xOb;

xOb.value = 20;

console.log(xOb.value);
console.log(yOb.value);

let number = 10;
let numOb = {value: 10};

function increase(jsType) {
  if (typeof(jsType) === 'object') {
    jsType.value++;
  }else {
    jsType++;
  }
}

increase(number);
console.log(number);

increase(numOb);
console.log(numOb.value);