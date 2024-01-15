#!/usr/bin/python3

#
# Формат ввода
# В первой строке — длина списочной формы числа X. На следующей строке — сама
# списочная форма с цифрами записанными через пробел.
#
# В последней строке записано число K, 0 ≤ K ≤ 10000.
#
# Формат вывода
# Выведите списочную форму числа X+K.
#

import sys;

def main():
  ln = int(input().rstrip());
  num = int(sys.stdin.readline().rstrip().replace(" ", ""));
  k = int(input().rstrip());

  res = str(num + k);

  output = "";

  for c in res:
    output += f"{ c } ";

  output = output[:-1];

  print(output);

################################################################################

if __name__ == "__main__":
  main();
