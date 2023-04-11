#!/usr/bin/python3

import sys;

################################################################################

def main():
  n = int(input().rstrip());
  colors = sys.stdin.readline().rstrip().split();

  count = [0, 0, 0];

  for i in colors:
    if (i == "0"):
      count[0] += 1;
    elif (i == "1"):
      count[1] += 1;
    elif (i == "2"):
      count[2] += 1;

  ans = [];

  item = 0;

  for i in count:
    for j in range(i):
      ans.append(item);

    item += 1;

  print(*ans);

################################################################################

if __name__ == "__main__":
  main();
