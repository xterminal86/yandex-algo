#!/usr/bin/python3

import sys;

################################################################################

def main():
  n = int(input().rstrip());
  nums = list( map(int, sys.stdin.readline().rstrip().split()) );

  if len(nums) == 2:
    if (nums[0] == 0 and nums[1] == 1) or (nums[1] == 0 and nums[0] == 1):
      print(2);
    else:
      print(0);

    return;

  sum = 0;
  maxLen = 0;
  d = {};

  ind = 0;
  for i in nums:
    if i == 0:
      sum += -1;
    else:
      sum += 1;

    if (sum == 0):
      maxLen = ind + 1;

    if sum not in d:
      d[sum] = ind;
    else:
      maxLen = max(maxLen, ind - d[sum]);

    ind += 1;

  print(maxLen);

################################################################################

if __name__ == "__main__":
  main();