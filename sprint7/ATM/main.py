#!/usr/bin/python3

import sys;

################################################################################

def CoinChange(coins, target):
  dp = [0] * (target + 1);
  dp[0] = 1;
  for coin in coins:
    for i in range(coin, target + 1):
      dp[i] += dp[i - coin];
  return dp[target];

################################################################################

def main():
  m = int(input().rstrip());
  n = int(input().rstrip());

  coins = list( map(int, sys.stdin.readline().rstrip().split()) );

  ans = CoinChange(coins, m);

  print(ans);

################################################################################

if __name__ == "__main__":
  main();
