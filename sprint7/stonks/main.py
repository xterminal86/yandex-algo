#!/usr/bin/python3

#
# Формат ввода
# В первой строке записано количество дней n —– целое число в диапазоне от 0 до
# 10 000.
#
# Во второй строке через пробел записано n целых чисел в диапазоне от 0 до 1000
# –— цены акций.
#
# Формат вывода
# Выведите число, равное максимально возможной прибыли за эти дни.
#

import sys;

################################################################################

def main():
  n = int(input().rstrip());
  stonks = list( map(int, sys.stdin.readline().rstrip().split()) );

  revenue = 0;
  maxStonk = 0;

  for i in range(n - 1, -1, -1):
    if stonks[i] > maxStonk:
      maxStonk = stonks[i];
    else:
      revenue += (maxStonk - stonks[i]);
      maxStonk = stonks[i];
   
  print(revenue);

################################################################################

if __name__ == "__main__":
  main();
