#!/usr/bin/python3

#
# Формат ввода
# В первой строке дано число вершин n (1 ≤ n ≤ 2 * 10^5) и рёбер
# (0 ≤ m ≤ 2 * 10^5). В каждой из следующих m строк записаны рёбра графа в виде
# пар (from, to), 1 ≤ from ≤ n — начало ребра, 1 ≤ to ≤ n — его конец.
# Гарантируется, что в графе нет петель и кратных рёбер.
#
# Формат вывода
# Выведите n строк, в каждой из которых записана пара чисел tini, touti — время
# входа и выхода для вершины i.
#

################################################################################

def main():
  line = input().rstrip().split();
  vertices = int(line[0]);
  edges    = int(line[1]);

  graph = [ None ] * (vertices + 1);

  colors = [0] * (vertices + 1);
  Entry = [0] * (vertices + 1);
  Leave = [0] * (vertices + 1);

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
      item.sort(reverse=True);

  #print(graph);

  toProcess = [ 1 ];

  entry = [ 0 ] * (vertices + 1);
  leave = [ 0 ] * (vertices + 1);

  cnt = 0;

  while len(toProcess) != 0:
    #print("toProcess: ", toProcess);

    v = toProcess.pop();

    #print("got ", v);

    if colors[v] == 0:
      colors[v] = 1;
      #print(f"  setting entry { cnt } for { v }");
      entry[v] = cnt;
      cnt += 1;
      toProcess.append(v);

      if graph[v] != None:
        for item in graph[v]:
          if colors[item] == 0:
            #print("  adding", item);
            toProcess.append(item);

    elif colors[v] == 1:
      colors[v] = 2;
      leave[v] = cnt;
      #print(f"  setting leave { cnt } for { v }");
      cnt += 1;

  for i in range(1, vertices + 1):
    print(entry[i], leave[i]);

################################################################################

if __name__ == "__main__":
  main();
