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