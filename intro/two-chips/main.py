#!/usr/bin/python3

#
# Формат ввода
# В первой строке записано количество фишек n, 2 ≤ n ≤ 10^4.
#
# Во второй строке записано n целых чисел —– очки на фишках Риты в диапазоне
# от -10^5 до 10^5.
#
# В третьей строке —– загаданное Гошей целое число k, -10^5 ≤ k ≤ 10^5.
#
# Формат вывода
# Нужно вывести два числа —– очки на двух фишках, в сумме дающие k.
#
# Если таких пар несколько, то можно вывести любую из них.
#
# Если таких пар не существует, то вывести «None».
#

def FindChips(chipsList, sumToAchieve):
  for i in range(len(chipsList)):
    for j in range(i + 1, len(chipsList)):
      sum_ = chipsList[i] + chipsList[j];
      if sum_ == sumToAchieve:
        return chipsList[i], chipsList[j];

  return None, None;

################################################################################

if __name__ == "__main__":
  chipsNumber  = int(input());
  chipsCost    = list(map(int, input().split()));
  sumToAchieve = int(input());

  v1, v2 = FindChips(chipsCost, sumToAchieve);

  if (v1 != None):
    print(f"{ v1 } { v2 }");
  else:
    print(f"{ v1 }");
