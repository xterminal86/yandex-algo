#!/usr/bin/python3

#
# Обратите внимание на ограничения в этой задаче.
#
# Формат ввода
# В первой строке записано количество фишек n, 2 ≤ n ≤ 10^5.
#
# Во второй строке записано n целых чисел в порядке неубывания —– очки на фишках
# Риты в диапазоне от -10^5 до 10^5.
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
  s = 0;
  e = len(chipsList) - 1;

  while s != e:
    start = chipsList[s];
    end   = chipsList[e];

    sum = start + end;

    if sum == sumToAchieve:
      return start, end;
    elif sum < sumToAchieve:
      s += 1;
    elif sum > sumToAchieve:
      e -= 1;

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
