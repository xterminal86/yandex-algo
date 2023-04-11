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
  base = int(input().rstrip());
  mod  = int(input().rstrip());
  str  = input().rstrip();

  t = int(input().rstrip());

  tasks = [];

  for i in range(t):
    spl = sys.stdin.readline().rstrip().split();
    i = int(spl[0]);
    j = int(spl[1]);

    tasks.append((i, j));

  ph = CalculatePrefixHashes(str, base, mod);

  ans = [];

  history = {};

  for task in tasks:
    i = task[0];
    j = task[1];

    if (i, j) in history:
      ans.append(history[(i,j)]);
    else:
      hr = ph[j];
      hl = ph[(i - 1)];
      h = ((hr + mod) - (hl * pow(base, j - i + 1, mod))) % mod;
      ans.append(h);
      history[(i,j)] = h;

  for item in ans:
    print(item);

################################################################################

if __name__ == "__main__":
  main();
