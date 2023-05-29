#!/usr/bin/python3

import sys;

################################################################################

def main():
  line = sys.stdin.readline().rstrip().split();
  n = int(line[0]);
  c = int(line[1]);
  
  ingots = list( map(int, sys.stdin.readline().rstrip().split()) );
  
  dp = [ False ] * (c + 1);
  dp[0] = True;
  
  for ingot in ingots:
    if ingot > c:
      continue;
    for j in range(c, ingot - 1, -1):      
      dp[j] = (dp[j] or dp[j - ingot]);

  for i in range(c, 0, -1):
    if dp[i] == True:
      print(i);
      return;

  print(0);
  
################################################################################

if __name__ == "__main__":
  main();
