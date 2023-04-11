#!/usr/bin/python3

import sys;

################################################################################

def LeftBinarySearch(lst, val):
  left  = -1;
  right = len(lst) - 1;

  while (left + 1 < right):
    m = left + (right - left) // 2;

    if (lst[m] < val):
      left = m;
    else:
      right = m;

  if (lst[right] >= val):
    return (right + 1);

  return -1;

################################################################################

def main():
  days = int(input().rstrip());
  lst  = list( map( int, sys.stdin.readline().rstrip().split() ) );
  cost = int(input().rstrip());

  oneBike  = LeftBinarySearch(lst, cost);
  twoBikes = LeftBinarySearch(lst, cost * 2);

  print(f"{ oneBike } { twoBikes }");

################################################################################

if __name__ == "__main__":
  main();
