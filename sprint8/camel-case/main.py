#!/usr/bin/python3

import re;

################################################################################

def Transform(pattern, strs):
  rePat = ""

  ln = len(pattern);

  success = False;

  for i in range(ln):
    rePat += f"{ pattern[i] }.*";

  for s in strs:
    res = re.search(rePat, s);
    if res != None:
      success = True;
      print(res.group());

  return success;

################################################################################

def main():
  n = int(input().rstrip());

  strs = [ None ] * n;

  for i in range(n):
    strs[i] = input().rstrip();

  strs.sort();

  j = int(input().rstrip());

  for i in range(j):
    pattern = input().rstrip();
    succ = Transform(pattern, strs);
    #if succ == False:
    #  print("");

################################################################################

if __name__ == "__main__":
  main();
