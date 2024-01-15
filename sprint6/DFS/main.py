#!/usr/bin/python3

#
# Формат ввода
# В первой строке дано количество вершин n (1 ≤ n ≤ 10^5) и рёбер
# m (0 ≤ m ≤ 10^5). Далее в m строках описаны рёбра графа. Каждое ребро
# описывается номерами двух вершин u и v (1 ≤ u, v ≤ n). В последней строке
# дан номер стартовой вершины s (1 ≤ s ≤ n). В графе нет петель и кратных рёбер.
#
# Формат вывода
# Выведите вершины в порядке обхода, считая что при запуске от каждой
# конкретной вершины её соседи будут рассматриваться в порядке возрастания
# (то есть если вершина 2 соединена с 1 и 3, то сначала обход пойдёт в 1,
# а уже потом в 3).
#

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

    if graph[t] == None:
      graph[t] = [ f ];
    else:
      graph[t].append(f);

  start = int(input().rstrip());

  for item in graph:
    if item != None:
      item.sort(reverse=True);

  #print(graph, start);

  toProcess = [ start ];

  ans = [];

  while len(toProcess) != 0:
    #print("toProcess: ", toProcess);

    v = toProcess.pop();

    #print("got ", v);

    if colors[v] == 0:
      ans.append(v);
      colors[v] = 1;

    if graph[v] != None:
      for item in graph[v]:
        if colors[item] == 0:
          #print("  adding", item);
          toProcess.append(item);

  print(*ans);

################################################################################

if __name__ == "__main__":
  main();
