#!/usr/bin/node
// Reference Types
// Objects in JS
let person = {
  firstName: 'Roberto',
  secondName: 'Notcarlos',
  age: 44
};

console.log(person);
// dot notation
console.log(person.firstName);
// bracket notation
console.log(person['secondName']);

//Arrays
let selectedColors = ['red', 'blue', 'yellow'];
console.log(selectedColors);
console.log(selectedColors.length);
selectedColors.push("Brown");
console.log(selectedColors);

//Functions
// Backticks are template literals
function youSuck(name) {
  console.log(`${name} You Suck soooo much!!`);
}

youSuck("Roberto");

// console.log(console); -> is an object

if (5 > 6) {
  console.log("wow!");
}else{
  console.log("Nope!");
}