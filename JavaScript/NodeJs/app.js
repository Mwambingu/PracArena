#!/usr/bin/node
// Global Object
// Instead of the window object we have the global object
// Doesn't work the same as window though
// eg. Variables can't be stored inside the global object
// Every code in Node runs with a module wrapper function
// eg. function(exports, require, module, __filename, __dirname) {Your code};
var sayHello = function (name) {
    console.log(`Hello ${name}`);
};

// window.sayHello();
// console.log(module);

// importing the logger module
// const logger = require("./logger");

// logger.log("Hi I am logger!");

// Importing a single function from a module
// const you = require("./logger");
// you("Monito");
const Logger = require("./logger");
const logger = new Logger();

logger.on("logging", (arg) => {
    console.log("Class logger working!!");
    console.log(arg);
});

logger.log("Hello ma baby!");
