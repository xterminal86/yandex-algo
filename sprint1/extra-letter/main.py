#!/usr/bin/python3

#
# Формат ввода
# На вход подаются строки s и t, разделённые переносом строки. Длины строк не
# превосходят 1000 символов. Строки не бывают пустыми.
#
# Формат вывода
# Выведите лишнюю букву.
#

import sys;

def main():
  s1 = sys.stdin.readline().rstrip();
  s2 = sys.stdin.readline().rstrip();

  cost1 = 0;
  cost2 = 0;

  for c in s1:
    cost1 += ord(c);

  for c in s2:
    cost2 += ord(c);

  addedLetter = chr(cost2 - cost1);

  print(addedLetter);

################################################################################

if __name__ == "__main__":
  main();
