#!/usr/bin/node
let url = "http://mylogger.io/log";

function log(message) {
    // Send http request
    console.log(message);
}

module.exports.log = log;
// module.exports.endPoint = url;
// console.log(module);

module.exports = function you(message) {
    console.log(`${message} you are an idiot!`);
    console.log(__dirname);
    console.log(__filename);
};
