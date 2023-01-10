#!/usr/bin/env python3
# Working with Generators
from typing import Generator

def odds(start: int, stop: int) -> Generator[int, None, None]:
  for odd in range(start, stop+1, 2):
    yield odd

def main():
  odd_values = [odd for odd in odds(3, 15)]
  odds2 = tuple(odds(21, 29))
  print(odd_values)
  print(odds2)

if __name__ == "__main__":
  main()