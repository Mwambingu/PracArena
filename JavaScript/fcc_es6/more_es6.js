#!/usr/bin/node
// For of loop
let incomes = [62000, 67000, 75000];
let total = 0;

for (const income of incomes) {
  total += income;
}

console.log(total);

// Spread Operator

let example1 = [1,2,3,4,5,6];
let example2 = [...example1];

console.log(example2);

let obEx1 = {
  firstName: 'Roberto'
};

let obEx2 = {
  ...obEx1
};

console.log(obEx2);