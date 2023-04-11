#!/usr/bin/python3

import sys;

from functools import cmp_to_key;

################################################################################

def main():
  segments = int(input().rstrip());
  lengths  = list( map(int, sys.stdin.readline().rstrip().split()) );

  sl = sorted(lengths,
              key = cmp_to_key(
    lambda i, j : 1 if i < j else -1
    )
  );

  # print(sl);

  # total = set();

  maxPerimeter = 0;

  for i in range(len(sl)):
    ans = [];
    ans.append(sl[i]);

    for j in range(i + 1, len(sl)):
      ans.append(sl[j]);

      for k in range(j + 1, len(sl)):
        ans.append(sl[k]);

        if (ans[0] < ans[1] + ans[2]):
          p = sum(ans);
          print(p);
          return;

        # total.add(tuple(ans));

        ans.pop();

      ans.pop();

################################################################################

if __name__ == "__main__":
  main();
