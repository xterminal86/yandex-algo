#!/usr/bin/python3

import sys;

################################################################################

def main():
  n  = int(input().rstrip());
  s  = int(input().rstrip());
  ar = list( map(int, sys.stdin.readline().rstrip().split()) );

  list.sort(ar);

  ans = [];

  i = 0;

  while (i < n):

    j = i + 1;

    while (j < n):
      end     = n - 1;
      start   = j + 1;
      nTarget = s - ar[i] - ar[j];

      while (start < end):

        if (ar[start] + ar[end]) == nTarget:

          ans.append([ar[i], ar[j], ar[start], ar[end]]);

          third  = ar[start];
          fourth = ar[end];

          while (start < end) and (ar[start] == third):
            start += 1;

          while (start < end) and (ar[end] == fourth):
            end += -1;

        elif (ar[start] + ar[end]) > nTarget:
          end += -1;
        else:
          start += 1;

      t = ar[j];

      while (j < n) and (ar[j] == t):
        j += 1;

    t2 = ar[i];

    while (i < n) and (ar[i] == t2):
      i += 1;

  print(len(ans));

  for item in ans:
    print(*item);

################################################################################

if __name__ == "__main__":
  main();
