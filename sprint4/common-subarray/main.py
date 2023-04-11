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

def CalculatePrefixHashes(s, a, mod):
  ln = len(s);
  ph = [0] * (ln + 1);

  for i in range(1, ln + 1):
    ph[i] = (ph[i - 1] * a + ord(s[i - 1])) % mod;

  return ph;

################################################################################

def main():
  base = 257;
  mod  = 100003;

  n = int(input().rstrip());
  scores1 = sys.stdin.readline().rstrip().replace(" ", "");
  m = int(input().rstrip());
  scores2 = sys.stdin.readline().rstrip().replace(" ", "");

  print(scores1);
  print(scores2);

  ln1 = len(scores1);
  ln2 = len(scores2);

  ph = [];
  searchIn = [];
  windowSize = 0;

  if (ln1 < ln2):
    print(f"calculating prefix hashes of '{ scores2 }'");
    ph = CalculatePrefixHashes(scores2, base, mod);
    windowSize = ln1;
    searchIn = scores2;
  elif (ln1 > ln2):
    print(f"calculating prefix hashes of '{ scores1 }'");
    ph = CalculatePrefixHashes(scores1, base, mod);
    windowSize = ln2;
    searchIn = scores1;
  else:
    print(f"calculating prefix hashes of '{ scores1 }'");
    ph = CalculatePrefixHashes(scores1, base, mod);
    windowSize = ln1;
    searchIn = scores2;

  print(ph);
  print(f"window size = { windowSize }");
  print(f"searching in '{ searchIn }'");

################################################################################

if __name__ == "__main__":
  main();
