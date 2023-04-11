#!/usr/bin/python3

import sys;

################################################################################

def CalculatePrefixHashes(s, a, mod):
  ln = len(s);
  ph = [0] * (ln + 1);

  for i in range(1, ln + 1):
    ph[i] = (ph[i - 1] * a + ord(s[i - 1])) % mod;

  return ph;

################################################################################

def main():
  base  = 345;
  mod   = 5608713984039443;

  spl = input().rstrip().split();
  n = int(spl[0]);
  k = int(spl[1]);
  s = sys.stdin.readline().rstrip();

  ph = CalculatePrefixHashes(s, base, mod);

  ln = len(s);

  power = pow(base, n, mod);

  ans = {};

  for i in range(ln - n + 1):
    l = i;
    r = l + n;

    hl = ph[l];
    hr = ph[r];

    h = ((hr + mod) - (hl * power)) % mod;

    if h in ans:
      ans[h][1] += 1;
    else:
      ans[h] = [ l, 1 ];

  out = [];

  for key,value in ans.items():
    if (value[1] >= k):
      out.append(value[0]);

  print(*out);

################################################################################

if __name__ == "__main__":
  main();
