#!/usr/bin/python3

import sys;

################################################################################

def main():
  students = int(input().rstrip());
  unis = list( map(int, sys.stdin.readline().rstrip().split()) );
  k = int(input().rstrip());

  su = sorted(unis);

  ans = {};

  for i in su:
    if i not in ans:
      ans[i] = 1;
    else:
      ans[i] += 1;

  srt = sorted(ans.items(), key = lambda x : x[1], reverse = True);

  res = [];

  count = 0;
  for i in srt:
    res.append(i[0]);
    count += 1;

    if (count >= k):
      break;

  print(*res);

################################################################################

if __name__ == "__main__":
  main();
