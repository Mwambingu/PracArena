#!/usr/bin/node
// Path Module
const path = require("path");

let pathobj = path.parse(__filename);

console.log(pathobj);

// Os Module
const os = require("os");

let memTot = os.totalmem();
let freeMem = os.freemem();

console.log(`Total Memory: ${memTot}`);
console.log(`Free Memory: ${freeMem}`);

// FS module (File System)
const fs = require("fs");

let readFile = fs.readdirSync("./");

console.log(readFile);

fs.readdir("./", function (err, asyncReadFile) {
    if (err) console.log("Error", err);
    else console.log("Result", asyncReadFile);
});

// Events Module
const EventEmitter = require("events");
const emitter = new EventEmitter();

// Register a listener
emitter.on("messageLogged", function (eventArg) {
    console.log("Event Raised!!");
    console.log(eventArg);
});
//  ES6 Version
emitter.on("messageLogged", (eventArg) => {
    console.log("Listener called!");
    console.log(eventArg);
});

// Raise event
emitter.emit("messageLogged", { id: 1, url: "http://" });

// Raise: logging (data: message)
emitter.on("logging", (eventArg) => {
    console.log("Event has been logged");
    console.log(eventArg);
});

emitter.emit("logging", { data: "Event log horizon is imminent!" });
