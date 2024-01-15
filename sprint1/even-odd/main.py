#!/usr/bin/python3

#
# Формат ввода
# В первой строке записаны три случайных целых числа a, b и c.
# Числа не превосходят 10^9 по модулю.
#
# Формат вывода
# Выведите «WIN», если игрок выиграл, и «FAIL» в противном случае.
#

import sys;

def main():
  line = sys.stdin.readline().rstrip();
  numbers = list(map(int, line.split()));

  a = numbers[0];
  b = numbers[1];
  c = numbers[2];

  allOdd  = ((a % 2 == 0) and (b % 2 == 0) and (c % 2 == 0));
  allEven = ((a % 2 != 0) and (b % 2 != 0) and (c % 2 != 0));

  if allOdd or allEven:
    print("WIN");
  else:
    print("FAIL");

################################################################################

if __name__ == "__main__":
  main();
