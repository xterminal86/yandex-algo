#!/usr/bin/python3

import sys;

################################################################################

def main():
  n = int(input().rstrip());
  m = int(input().rstrip());
  north = list( map(int, sys.stdin.readline().rstrip().split()) );
  south = list( map(int, sys.stdin.readline().rstrip().split()) );

  ans = sorted(north + south);

  ln = len(ans);
  if ln % 2 == 0:
    half = (ln // 2) - 1;
    print((ans[half] + ans[half + 1]) / 2);
  else:
    print(ans[(ln - 1) // 2]);

################################################################################

if __name__ == "__main__":
  main();
