#!/usr/bin/python3

import sys;

def main():
  numBin1 = int(input().rstrip(), 2);
  numBin2 = int(input().rstrip(), 2);

  numRes = numBin1 + numBin2;

  print(bin(numRes)[2:]);

if __name__ == "__main__":
  main();
