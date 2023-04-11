#!/usr/bin/python3

# contest id = 83946279

import sys;

################################################################################

def main():
  n = int(input().rstrip());
  nums = list( map(int, sys.stdin.readline().rstrip().split()) );

  maxVal = pow(10, 9);
  
  ans = [0] * n;

  if nums[0] == 0:
    ans[0] = 0;
  else:
    ans[0] = maxVal;

  for i in range(1, n):
    if (nums[i] == 0):
      ans[i] = 0;
    else:
      ans[i] = ans[i - 1] + 1;

  if (nums[n - 1] == 0):
    ans[n - 1] = 0;
    
  for i in range(n - 2, -1, -1):
    ans[i] = min(ans[i], ans[i + 1] + 1);
    
    if (nums[i] == 0):
      ans[i] = 0;
      
  print(*ans);

################################################################################
  
if __name__ == "__main__":
  main();
