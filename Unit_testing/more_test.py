#!/usr/bin/env python3

import os

def rm(filename):
  os.remove(filename)

if __name__ == "__main__":
  test_str = "hello"
  rm(test_str)