#!/usr/bin/python3

import sys;

################################################################################

def main():
  line = sys.stdin.readline().rstrip().split();
  line.reverse();
  print(*line);

################################################################################

if __name__ == "__main__":
  main();
