#!/usr/bin/python3

import sys;

def main():
  days = int(input().rstrip());
  temp = list(map(int, sys.stdin.readline().rstrip().split()));

  chaos = 0;

  for i in range(0, days):
    cur = temp[i];
    prev = None if (i - 1) < 0 else temp[i - 1];
    next = None if (i + 1) > (days - 1) else temp[i + 1];

    if ((prev == None or cur > prev) and (next == None or cur > next)):
      chaos += 1;

  print(chaos);

if __name__ == "__main__":
  main();
