#!/usr/bin/python3

#
# Формат ввода
# В первой строке задано целое число M — грузоподъёмность рюкзака Гоши
# (0 ≤ M ≤ 10^8).
#
# Во второй строке дано количество куч с золотым песком — целое число
# n (1 ≤ n ≤ 10^5).
#
# В каждой из следующих n строк описаны кучи: i-ая куча задаётся двумя целыми
# числами ci и mi, записанными через пробел (1 ≤ ci ≤ 10^7, 1 ≤ mi ≤ 10^8).
#
# Формат вывода
# Выведите единственное число —– максимальную сумму (в алгосских франках),
# которую Гоша сможет вынести из пещеры в своём рюкзаке.
#

import heapq;

################################################################################

def main():
  capacity = int(input().rstrip());
  piles = int(input().rstrip());
  data = [];
  for i in range(piles):
    line = input().rstrip().split();
    c = int(line[0]);
    m = int(line[1]);
    data.append( (-c, m) );

  heapq.heapify(data);

  ans = 0;

  stop = False;

  while stop == False:
    if len(data) == 0:
      break;

    item = heapq.heappop(data);

    c = abs( item[0] );
    n = abs( item[1] );

    capacity -= n;

    if capacity >= 0:
      ans += c * n;
    else:
      ans += (c * n) - (-capacity * c);
      stop = True;

  print(ans);

################################################################################

if __name__ == "__main__":
  main();
