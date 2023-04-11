#!/usr/bin/python3

import sys;


def main():
  line = sys.stdin.readline().rstrip();
  numbers = list(map(int, line.split()));

  a = numbers[0];
  b = numbers[1];
  c = numbers[2];

  allOdd  = ((a % 2 == 0) and (b % 2 == 0) and (c % 2 == 0));
  allEven = ((a % 2 != 0) and (b % 2 != 0) and (c % 2 != 0));

  if allOdd or allEven:
    print("WIN");
  else:
    print("FAIL");

################################################################################

if __name__ == "__main__":
  main();
