#!/usr/bin/python3

import sys;

################################################################################

def main():
  n = int(input().rstrip());
  first = sys.stdin.readline().rstrip().split();
  m = int(input().rstrip());
  second = sys.stdin.readline().rstrip().split();

  dp = [ [0 for _ in range(m + 1)] for _ in range(n + 1)];

  for i in range(n):
    for j in range(m):
      if first[i] == second[j]:
        dp[i + 1][j + 1] = 1 + dp[i][j];
      else:
        dp[i + 1][j + 1] = max(dp[i][j + 1], dp[i + 1][j]);

  i = n;
  j = m;

  ans = [];

  while (i > 0) and (j > 0):
    if dp[i][j] == dp[i][j - 1]:
      j += -1;
    elif dp[i][j] == dp[i - 1][j]:
      i += -1;
    else:
      ans.append( (i, j) );
      i += -1;
      j += -1;

  ans.reverse();

  print(len(ans));

  out = [];

  for item in ans:
    out.append(item[0]);

  print(*out);

  out = [];

  for item in ans:
    out.append(item[1]);

  print(*out);

################################################################################

if __name__ == "__main__":
  main();
