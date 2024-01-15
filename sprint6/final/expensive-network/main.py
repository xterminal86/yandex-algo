#!/usr/bin/python3

# contest id = 86947243
#
# Формат ввода
# В первой строке дано количество вершин n и ребер m графа (1 ≤ n ≤ 1000,
# 0 ≤ m ≤ 100000).
#
# В каждой из следующих m строк заданы рёбра в виде троек чисел u, v, w.
# u и v — вершины, которые соединяет это ребро. w — его вес
# ( 1 ≤ u, v ≤ n, 0 ≤ w ≤ 10000). В графе могут быть петли и кратные ребра.
# Граф может оказаться несвязным.
#
# Формат вывода
# Если максимальное остовное дерево существует, то выведите его вес. Иначе (если в графе несколько компонент связности) выведите фразу «Oops! I did it again».
#
# Временная сложность - O(E*logV), где E - кол-во рёбер, V - кол-во вершин
# Пространственная - O(3V + E + HQ), где 3V состоит из массива для хранения
#                    всех вершин, массива keys и массива processed.
#                    E - для хранения рёбер.
#                    HQ - стоимость хранения кучи.

import heapq;

################################################################################

def AddToGraph(f, t, w, graph):
  if graph[f] == None:
    graph[f] = [ (t, w) ];
  else:
    graph[f].append( (t, w) );

  if graph[t] == None:
    graph[t] = [ (f, w) ];
  else:
    graph[t].append( (f, w) );

################################################################################

def PrintGraph(graph):
  ln = len(graph);

  for v in range(1, ln):
    out = "";

    if graph[v] != None:
      for to in graph[v]:
        out += f"({ to[0] } : { to[1] }) ";

    print(f"{ v } -> { out }");

################################################################################

def MST(graph):
  MaxWeight = 10001;

  #
  # Это куча.
  #
  tasks = [];

  #
  # <кол-во вершин> + 1
  #
  ln = len(graph);

  processed = [ False ] * ln;

  #
  # Массив, индексированный по номеру вершины, который будет хранить минимальную
  # стоимость для перехода в соответствующую вершину.
  #
  keys = [ MaxWeight ] * ln;

  #
  # ( <вес>, <номер вершины> )
  #
  heapItem = ( 0, 1 );

  heapq.heappush(tasks, heapItem);

  ans = 0;

  iterations = 0;

  while len(tasks) != 0:
    w,v = heapq.heappop(tasks);

    if processed[v] == False:
      iterations += 1;
      ans += w;

    processed[v] = True;

    if graph[v] != None:
      for vert,wght in graph[v]:
        if (processed[vert] == False) and (wght < keys[vert]):
          keys[vert] = wght;
          heapItem = (wght, vert);
          heapq.heappush(tasks, heapItem);

  ans = abs(ans);

  #
  # Если в процессе работы алгоритма мы затронули не все вершины графа,
  # то это провал.
  #
  if (iterations != (ln - 1)):
    print("Oops! I did it again");
  else:
    print(ans);

################################################################################

def main():
  line = input().rstrip().split();

  vertices = int(line[0]);
  edges    = int(line[1]);

  graph = [ None ] * (vertices + 1);

  for i in range(edges):
    line = input().rstrip().split();
    f = int(line[0]);
    t = int(line[1]);

    #
    # heapq только возрастающая, подсунуть ей какой-то свой компаратор
    # я не нашёл как, поэтому просто сделаем веса отрицательными,
    # чтобы самый "дорогой" элемент был наверху.
    #
    w = -int(line[2]);

    AddToGraph(f, t, w, graph);

  #PrintGraph(graph);

  #
  # M в названии можно удачно расшифровывать и как Minimum, и как Maximum,
  # поэтому название подойдёт для обоих вариантов реализации. )
  #
  MST(graph);

################################################################################

if __name__ == "__main__":
  main();
