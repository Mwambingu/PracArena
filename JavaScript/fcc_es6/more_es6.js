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

// Rest Operator
function add(...nums) {
  let sumNum = 0;
  for (let num of nums) {
    sumNum += num;
  }
  return sumNum;
}

console.log(add(1,3,5,6,0,29,44));

// Arrow Functions
function add2(...nums) {
  // let total = nums.reduce(function (x, y) {return x+y;});
  let total = nums.reduce((x, y) => x + y);
  console.log(total);
}

add2(4, 5, 7, 8, 12);
