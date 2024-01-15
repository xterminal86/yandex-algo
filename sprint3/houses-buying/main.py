#!/usr/bin/python3

#
# Формат ввода
# В первой строке через пробел записаны натуральные числа n и k.
#
# n — количество домов, которые рассматривает Тимофей, оно не превосходит
# 100000;
#
# k — общий бюджет, не превосходит 100000;
#
# В следующей строке через пробел записано n стоимостей домов. Каждое из чисел
# не превосходит 100000. Все стоимости — натуральные числа.
#
# Формат вывода
# Выведите одно число —– наибольшее количество домов, которое может купить
# Тимофей.
#

import sys;

################################################################################

def main():
  maxSize = 100000;

  line = input().rstrip().split();

  housesWant = int(line[0]);
  money      = int(line[1]);

  housesCost = list( map(int, sys.stdin.readline().rstrip().split()) );

  count = [0] * maxSize;

  for i in housesCost:
    ind = (i - 1);
    count[ind] += 1;

  housesBought = 0;

  for i in range(maxSize):
    if (count[i] == 0):
      continue;

    cost = (i + 1);

    while (money >= cost) and (count[i] > 0):
      money = money - cost;
      count[i] += -1;
      housesBought += 1;

  print(housesBought);

################################################################################

if __name__ == "__main__":
  main();
