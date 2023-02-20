#!/usr/bin/node
const EventEmitter = require("events");
// const emitter = new EventEmitter();
let url = "http://mylogger.io/log";

// function log(message) {
//     // Send http request
//     console.log(message);
//     // Raise event
//     emitter.emit("messageLogged", { id: 1, url: "http://" });
// }

// module.exports.log = log;
// module.exports.endPoint = url;
// console.log(module);

// module.exports = function you(message) {
//     console.log(`${message} you are an idiot!`);
//     console.log(__dirname);
//     console.log(__filename);
// };

class Logger extends EventEmitter {
    log(message) {
        // Send http request
        console.log(message);
        // Raise event
        this.emit("logging", { id: 1, url: "http://" });
    }
}

module.exports = Logger;
