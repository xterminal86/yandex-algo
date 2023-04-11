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

def PrintUsage(obj):
  kb = sys.getsizeof(obj) // 1024;
  mb = kb // 1024;

  print(f"{ type(obj) } size is { kb } KB, { mb } MB");

################################################################################

def PrintUsageBig(lst):
  totalBytes = 0;

  for item in lst:
    totalBytes += sys.getsizeof(item);

  totalBytes += sys.getsizeof(lst);

  kb = totalBytes // 1024;

  print(f"big ass size = { kb } KB");

################################################################################

def main():
  prime = 1000003;

  base  = 100003;
  mod   = prime;

  maxSize = prime;

  spl = input().rstrip().split();
  n = int(spl[0]);
  k = int(spl[1]);
  s = sys.stdin.readline().rstrip();

  d = [ None ] * (maxSize + 1);

  ln = len(s);

  for i in range(ln - n + 1):
    ss = s[ i:(i + n) ];
    h = HornerHash(ss, base, mod);
    #print(f"  '{ ss }' = { h }");
    if d[h] == None:
      d[h] = [ i, 1 ];
    else:
      d[h][1] += 1;

  ans = [];

  for item in d:
    if item != None:
      if item[1] >= k:
        ans.append(item[0]);

  print(*ans);

  #PrintUsageBig(d);

################################################################################

if __name__ == "__main__":
  main();
