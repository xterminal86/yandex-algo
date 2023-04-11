#!/usr/bin/python3

import sys;

################################################################################

def HornerHash(s, base, mod):
  ln = len(s);

  if (ln == 1):
    return (ord(s) % mod);

  res = ord(s[0]);

  for i in range(1, ln):
    res = ( ord(s[i]) + res * base ) % mod;

  return res;

################################################################################

def main():
  base = int(input().rstrip());
  mod  = int(input().rstrip());
  str  = sys.stdin.readline().rstrip();

  if len(str) == 0:
    print(0);
    return;
  
  res = HornerHash(str, base, mod);

  print(res);

################################################################################

if __name__ == "__main__":
  main();
