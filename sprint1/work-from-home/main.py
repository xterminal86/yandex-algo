#!/usr/bin/python3

import sys;

def main():
  numDec = int(input().rstrip());

  if numDec == 0:
    print(0);
    exit(0);

  bin = "";

  while True:
    if numDec == 0:
      break;

    if numDec % 2 == 0:
      bin = "0" + bin;
    else:
      bin = "1" + bin;

    numDec = int(numDec / 2);

  print(bin);

if __name__ == "__main__":
  main();
