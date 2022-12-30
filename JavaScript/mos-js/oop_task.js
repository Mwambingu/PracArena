#!/usr/bin/node
// StopWatch Class
// --start() --> method that starts the timer
// --stop() --> method that stops the timer
// --reset() --> method that resets the timer

function StopWatch() {
  let time = 0;
  let count = 0;
  let stopInterval;
  let started;
  let countTimer = function () {
    count += 1;
  };
  this.start = function () {
    if (started) {
      throw new Error('Timer already started'); 
    }
    stopInterval = setInterval(countTimer, 1);
    started = true;
  };
  this.stop = function () {
    if (started === false) {
      throw new Error('Timer already stopped'); 
    }
    clearInterval(stopInterval);
    started = false;
  };
  this.duration = function () {
    time = (count / 1000)
    console.log(time);
  };
  this.reset = function() {
    count = 0;
  };
}

const skippity = new StopWatch();
console.log(skippity);
skippity.start();