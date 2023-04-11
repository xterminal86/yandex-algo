#!/usr/bin/python3

import sys;

################################################################################

def main():
  s1 = list(sys.stdin.readline().rstrip());
  s2 = list(sys.stdin.readline().rstrip());

  l1 = len(s1);
  l2 = len(s2);

  i = 0;
  j = 0;

  while (i < l1 and j < l2):
    if (s1[i] == s2[j]):
      i += 1;
    j += 1;

  print(i == l1);

################################################################################

if __name__ == "__main__":
  main();
