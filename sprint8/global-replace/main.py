#!/usr/bin/python3

import re;

################################################################################

def main():
  s = input().rstrip();
  pattern = input().rstrip();
  replace = input().rstrip();

  res = re.sub(pattern, replace, s);

  print(res);

################################################################################

if __name__ == "__main__":
  main();
