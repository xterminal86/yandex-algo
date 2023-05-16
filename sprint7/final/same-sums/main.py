#!/usr/bin/python3

import sys;

################################################################################

def main():
  n = int(input().rstrip());

  scores = list( map(int, sys.stdin.readline().rstrip().split()) );

  total = sum(scores);

  if total % 2 != 0:
    print("False");
    return;

  limit = total // 2;

  dp = [ False ] * (limit + 1);

  dp[0] = True;

  for score in scores:
    #print(f"new score = { score }");
    for i in range(limit, score - 1, -1):
      #print(f"  i = { i }, score = { score }, i - score = { i - score }");
      if dp[limit] == True:
        print("True");
        return;

      dp[i] = (dp[i] or dp[i - score]);
      #print("  ", dp);

  if dp[limit] == True:
    print("True");
  else:
    print("False");

################################################################################

if __name__ == "__main__":
  main();
