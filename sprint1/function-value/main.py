#!/usr/bin/python3

#
# Формат ввода
# На вход через пробел подаются целые числа a, x, b, c. В конце ввода находится
# перенос строки.
#
# Формат вывода
# Выведите одно число — значение функции в точке x.
#

import sys;

def main():
  line = sys.stdin.readline().rstrip();
  numbers = list(map(int, line.split()));

  # a x b c
  a = numbers[0];
  x = numbers[1];
  b = numbers[2];
  c = numbers[3];

  res = a * pow(x, 2) + b * x + c;

  print(res);

################################################################################

if __name__ == "__main__":
  main();
