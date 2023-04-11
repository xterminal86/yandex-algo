#!/usr/bin/python3

import sys;

################################################################################

def main():
  n = int(input().rstrip());

  segments = [];

  for i in range(n):
    coords = list( map(int, sys.stdin.readline().rstrip().split()) );
    segments.append(coords);

  segments = sorted(segments);

  stack = [];

  stack.append(segments[0]);

  for i in segments[1:]:
    x = stack[-1][0];
    y = stack[-1][1];

    if (x <= i[0]) and (i[0] <= y):
      stack[-1][1] = max(stack[-1][1], i[1]);
    else:
      stack.append(i);

  for item in stack:
    print(*item);

################################################################################

if __name__ == "__main__":
  main();
