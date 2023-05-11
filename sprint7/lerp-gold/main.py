#!/usr/bin/python3

import sys;

################################################################################

def main():
  line = input().rstrip().split();
  n = int(line[0]);
  w = int(line[1]);

  ingots = list( map(int, sys.stdin.readline().rstrip().split() ) );

  print(ingots);

################################################################################

if __name__ == "__main__":
  main();
