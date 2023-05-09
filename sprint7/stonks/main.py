#!/usr/bin/python3

import sys;

################################################################################

def main():
  n = int(input().rstrip());
  stonks = list( map(int, sys.stdin.readline().rstrip().split()) );

  revenue = 0;
  maxStonk = 0;

  for i in range(n - 1, -1, -1):
    if stonks[i] > maxStonk:
      maxStonk = stonks[i];
    else:
      revenue += (maxStonk - stonks[i]);
      maxStonk = stonks[i];
   
  print(revenue);

################################################################################

if __name__ == "__main__":
  main();
