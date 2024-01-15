#!/usr/bin/python3

#
# Формат ввода
# В первой строке даны два числа – количество вершин n (1 ≤ n ≤ 10^5) и
# количество рёбер m (0 ≤ m ≤ 10^5). В каждой из следующих m строк описаны рёбра
# по одному на строке. Каждое ребро представлено парой вершин (from, to),
# 1 ≤ from, to ≤ n, соответственно номерами вершин начала и конца.
#
# Формат вывода
# Выведите номера вершин в требуемом порядке.
#

################################################################################

def TopSort(v, colors, graph, order):
  colors[v] = 1;
  if graph[v] != None:
    for vert in graph[v]:
      if colors[vert] == 0:
        TopSort(vert, colors, graph, order);
  colors[v] = 2;
  order.append(v);

################################################################################

def main():
  line = input().rstrip().split();
  vertices = int(line[0]);
  edges    = int(line[1]);

  graph = [ None ] * (vertices + 1);

  colors = [0] * (vertices + 1);

  for i in range(edges):
    line = input().rstrip().split();
    f = int(line[0]);
    t = int(line[1]);

    if graph[f] == None:
      graph[f] = [ t ];
    else:
      graph[f].append(t);

  for item in graph:
    if item != None:
      item.sort();

  order = [];

  for i in range(1, vertices + 1):
    if colors[i] == 0:
      TopSort(i, colors, graph, order);

  ans = [];

  while len(order) != 0:
    ans.append(order.pop());

  print(*ans);

################################################################################

if __name__ == "__main__":
  main();
