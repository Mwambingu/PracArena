#!/usr/bin/node
// Template Literals
let robber = 'Mwizi';

arrest = function () {
  console.log("Uwizi utawacha shenzi");
  return 'Umbwa!!';
}

console.log(`Tumekushika ${robber} ${arrest()}`);

// Destructuring Objects
const personalInformation = {
  firstName:'Isaiah',
  lastName:'Cabbages',
  city:'Jerusalem',
  country: 'Israel'
}

const {firstName: fn, lastName: ln} = personalInformation;

console.log(`${fn} ${ln}`);

// Destructuring Arrays
let [firstName, midName, lastName] = ['Cabbageman', 'Cabbage God', 'Israelite'];
console.log(firstName, midName, lastName);

// Object Literals
function addressMaker(city, state) {
  // const newAdress = {newCity: city, newState: state};
  const newAdress = {city, state};

  console.log(newAdress);
}

addressMaker('Austin', 'Texas');

function destro(obj) {
  let {firstName, lastName, city} = obj;
  const aadd = {firstName, lastName, city};
  console.log(aadd)
}

destro(personalInformation);