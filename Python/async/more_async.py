#!/usr/bin/env python3
# Working with Generators
import random import randint
import time
import asyncio
from typing import Generator

def odds(start: int, stop: int) -> Generator[int, None, None]:
  for odd in range(start, stop+1, 2):
    yield odd

def randin():
  time sleep(3)
  return randint(1, 10)

def main():
  odd_values = [odd for odd in odds(3, 15)]
  odds2 = tuple(odds(21, 29))
  print(odd_values)
  print(odds2)

if __name__ == "__main__":
  main()