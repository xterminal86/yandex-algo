#!/usr/bin/python3

import sys;

def main():
  textLen = int(input().rstrip());
  text    = sys.stdin.readline().rstrip().split();

  lenSoFar = 0;

  res = {};

  for str in text:
    ln = len(str);

    if ln > lenSoFar:
      lenSoFar = ln;
      res[ln] = str;

  if (res):
    print(res[lenSoFar]);
  else:
    print("");

  print(lenSoFar);

if __name__ == "__main__":
  main();
