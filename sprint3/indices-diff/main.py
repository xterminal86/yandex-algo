#!/usr/bin/python3

#
# Формат ввода
# В первой строке записано натуральное число n –— количество островов в
# архипелаге (2 ≤ n ≤ 100 000).
#
# В следующей строке через пробел записаны n площадей островов — n натуральных
# чисел, каждое из которых не превосходит 1 000 000.
#
# В последней строке задано число k. Оно находится в диапазоне от 1 до
# n(n - 1) / 2.
#
# Формат вывода
# Выведите одно число –— k-ую минимальную разницу.
#

import sys;

################################################################################

def IsSmallerPair(ar, k, mid):
  count = 0;
  left = 0;
  ln = len(ar);
  for i in range(1, ln):
    while ((ar[i] - ar[left]) > mid):
      left += 1;
    count += i - left;
  return (count >= k);

################################################################################

def Find(areas, k):
  areas = sorted(areas);

  ln = len(areas);

  left = 0;
  right = areas[-1] - areas[0];
  while (left < right):
    mid = (left + right) // 2;
    if (IsSmallerPair(areas, k, mid)):
      right = mid;
    else:
      left = mid + 1;

  return left;

################################################################################

def RunTest(ar, k, expected):
  ans = Find(ar, k);
  assert (ans == expected);

################################################################################

def RunTests():
  RunTest([ 2, 3, 4 ], 2, 1);
  RunTest([ 1, 3, 1 ], 1, 0);
  RunTest([ 1, 3, 5 ], 3, 4);
  RunTest([ 9, 6, 10, 3 ], 3, 3);

################################################################################

def main():
  n = int(input().rstrip());
  areas = list( map(int, sys.stdin.readline().rstrip().split()) );
  k = int(input().rstrip());

  # RunTests();

  ans = Find(areas, k);

  print(ans);

################################################################################

if __name__ == "__main__":
  main();
