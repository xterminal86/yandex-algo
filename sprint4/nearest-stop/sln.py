#!/usr/bin/python3

#
# Формат ввода
# В первой строке дано количество выходов из метро –— натуральное число
# n (1 ≤ n ≤ 10^4). В следующих n строках даны координаты выходов из метро.
# Каждый выход описывается двумя координатами x и y, записанными через пробел.
#
# В следующей строке дано количество автобусных остановок —– натуральное число
# m (1 ≤ m ≤ 10^6). В следующих m строках заданы координаты остановок. Каждая
# остановка описывается двумя числами —– своими x и y координатами, записанными
# через пробел.
#
# Все координаты —– целые числа, не превосходящие 10^9 по модулю. Единицы
# измерения —– метры.
#
# Формат вывода
# Выведите единственное число –— номер того выхода из метро, рядом с которым
# расположено больше всего остановок. Номер выхода –— его порядковый номер во
# входных данных (нумерация с единицы).
#
# Если подходящих выходов из метро несколько, выведите тот, который встречается
# раньше во входных данных.
#

################################################################################

def GetPointsAroundZero(radius):
  ans = {};
  squared = pow(radius, 2);

  for x in range(-radius, radius + 1, 1):
    for y in range(-radius, radius + 1, 1):
      r = pow(x, 2) + pow(y, 2);
      if (r <= squared):
        ans[(x, y)] = (x, y);

  return ans;

################################################################################

def main():
  searchRadius = 20;

  area = GetPointsAroundZero(searchRadius);

  n = int(input().rstrip());

  exits = [ None ] * n;

  for i in range(n):
    s = input().rstrip().split();
    ex = ( int(s[0]), int(s[1]) );
    exits[i] = ex;

  m = int(input().rstrip());

  stops = {};

  for i in range(m):
    s = input().rstrip().split();
    st = ( int(s[0]), int(s[1]) );
    if st in stops:
      stops[st] += 1;
    else:
      stops[st] = 1;

  exitFound = -1;
  stopsMax  = 0;

  #
  # O(n*k) k = len(area)
  #

  exitInd = 0;
  for ex in exits:
    stopsCnt = 0;
    for p in area:
      x = ex[0] + p[0];
      y = ex[1] + p[1];
      if (x, y) in stops:
        stopsCnt += stops[(x, y)];
    if (stopsCnt > stopsMax):
      stopsMax = stopsCnt;
      exitFound = exitInd;
    exitInd += 1;

  print(exitFound + 1);

################################################################################

if __name__ == "__main__":
  main();
