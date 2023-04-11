#!/usr/bin/python3

import sys;

################################################################################

def main():
  n = int(input().rstrip());
  strings = sys.stdin.readline().rstrip().split();

  d = {};

  count = 0;

  for s in strings:
    ss = "".join(sorted(s));
    if ss not in d:
      d[ss] = [count];
    else:
      d[ss].append(count);

    count += 1;

  for k,v in d.items():
    print(*v);

################################################################################

if __name__ == "__main__":
  main();
