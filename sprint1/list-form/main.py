#!/usr/bin/python3

import sys;

def main():
  ln = int(input().rstrip());
  num = int(sys.stdin.readline().rstrip().replace(" ", ""));
  k = int(input().rstrip());

  res = str(num + k);

  output = "";

  for c in res:
    output += f"{ c } ";

  output = output[:-1];

  print(output);

if __name__ == "__main__":
  main();
