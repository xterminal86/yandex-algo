#!/usr/bin/python3
#
# fuck this shit

import sys;

class Solution:
    def fourSum(self, nums, target):
        nums.sort()
        n = len(nums)
        result = []
        for i in range(n - 3):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for j in range(i + 1, n - 2):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                l, r = j + 1, n - 1
                while l < r:
                    s = nums[i] + nums[j] + nums[l] + nums[r]
                    if s == target:
                        result.append([nums[i], nums[j], nums[l], nums[r]])
                        while l < r and nums[l] == nums[l + 1]:
                            l += 1
                        while l < r and nums[r] == nums[r - 1]:
                            r -= 1
                        l += 1
                        r -= 1
                    elif s < target:
                        l += 1
                    else:
                        r -= 1
        return result

if __name__ == "__main__":
  n  = int(input().rstrip());
  s  = int(input().rstrip());
  ar = list( map(int, sys.stdin.readline().rstrip().split()) );

  sln = Solution();
  ans = sln.fourSum(ar, s);

  l = len(ans);

  print(l);

  for i in ans:
    print(*i);
