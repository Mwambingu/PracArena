#!/usr/bin/node
// Challenge 1
// function addressMaker(address) {
//   const newAddress = {
//     city: address.city,
//     state: address.state,
//     country: 'United States'
//   };

// }

// addressMaker({city: 'Austin', state: 'Texas'});

// My Solution -> Object Literals + Destructuring
function addressMaker(address) {
  let country = 'United States', {city, state} = address;
  const newAddress = {city, state, country};
  console.log(newAddress);
}

addressMaker({city: 'Austin', state: 'Texas'});

// Challenge 2
let incomes = [62000, 67000, 75000];

for (let income of incomes) {
  income += 5000;
}

console.log(incomes);
