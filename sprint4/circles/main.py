#!/usr/bin/python3

import sys;

################################################################################

def main():
  n = int(input().rstrip());

  d = {};

  for i in range(n):
    name = sys.stdin.readline().rstrip();
    d[name] = name;

  for k,v in d.items():
    print(k);

################################################################################

if __name__ == "__main__":
  main();
