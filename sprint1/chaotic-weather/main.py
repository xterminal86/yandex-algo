#!/usr/bin/python3

#
# Формат ввода
# В первой строке дано число n –— длина периода измерений в днях, 1 ≤ n ≤ 10^5.
# Во второй строке даны n целых чисел –— значения температуры в каждый из n дней.
# Значения температуры не превосходят 273 по модулю.
#
# Формат вывода
# Выведите единственное число — хаотичность за данный период.
#

import sys;

def main():
  days = int(input().rstrip());
  temp = list(map(int, sys.stdin.readline().rstrip().split()));

  chaos = 0;

  for i in range(0, days):
    cur = temp[i];
    prev = None if (i - 1) < 0 else temp[i - 1];
    next = None if (i + 1) > (days - 1) else temp[i + 1];

    if ((prev == None or cur > prev) and (next == None or cur > next)):
      chaos += 1;

  print(chaos);
  
################################################################################

if __name__ == "__main__":
  main();
