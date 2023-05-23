#!/usr/bin/python3

import sys;

################################################################################

def main():
  strings = ["", ""];

  ind = 0;

  for line in sys.stdin:
    for c in line:
      if (ord(c) % 2 == 0) and (c != '\n'):
        strings[ind] += c;

    ind += 1;

  if strings[0] == strings[1]:
    print("0");
  elif strings[0] > strings[1]:
    print("1");
  else:
    print("-1");

################################################################################

if __name__ == "__main__":
  main();
