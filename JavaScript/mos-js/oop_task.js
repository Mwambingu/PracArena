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

// Solution implementation
function Stopwatch2() {
  let startTime, endTime, running, duration = 0;

  this.start = function() {
    if (running) {
      throw new Error('StopWatch has already started.');
    }

    running = true;

    startTime = new Date();
  };

  this.stop = function () {
    if (!running) {
      throw new Error('StopWatch is not started.');
    }

    running = false;

    endTime = new Date();

    const seconds = (endTime.getTime() - startTime.getTime()) / 1000;
    duration += seconds;
  };

  this.reset = function () {
    startTime = null;
    endTime = null;
    running = false;
    duration = 0;
  };

  Object.defineProperty(this, 'duration', {
    get: function () { return duration;}
  });
}