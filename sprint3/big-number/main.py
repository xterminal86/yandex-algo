#!/usr/bin/python3

import sys;

from functools import cmp_to_key;

################################################################################

def main():
  n    = int(input().rstrip());
  nums = list( map(int, sys.stdin.readline().rstrip().split()) );

  res = sorted(nums, key = cmp_to_key(
    lambda i, j: -1 if str(j) + str(i) < str(i) + str(j) else 1)
  );

  out = "";

  for i in res:
    out += f"{ i }";

  print(out);

################################################################################

if __name__ == "__main__":
  main();
