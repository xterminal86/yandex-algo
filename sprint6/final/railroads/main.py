#!/usr/bin/python3

# contest id = 87050258

# Временная сложность - O(V + E), где V - кол-во вершин, E - кол-во рёбер
# Пространственная - O(V)

#
# Для решения задачи положим, что "дороги" типа R являются рёбрами графа,
# направленными в одну сторону, а типа B - в обратную.
# Тогда задача сводится к поиску цикла в графе.
#

import sys;

################################################################################

def AddToGraph(graph, townFrom, townTo, value):
  if value == "R":
    if graph[townFrom] == None:
      graph[townFrom] = [ townTo ];
    else:
      graph[townFrom].append(townTo);
  elif value == "B":
    if graph[townTo] == None:
      graph[townTo] = [ townFrom ];
    else:
      graph[townTo].append(townFrom);

################################################################################

def DFS(v, graph, colors):
  colors[v] = 1;

  if graph[v] != None:
    for vert in graph[v]:
      if colors[vert] == 1:
        return True;

      if ( colors[vert] == 0 ) and ( DFS(vert, graph, colors) == True ):
        return True;

  colors[v] = 2;

  return False;

################################################################################

def FindLoop(graph) -> bool:
  vertices = len(graph);
  colors = [ 0 ] * vertices;

  for v in range(1, vertices):
    if colors[v] == 0:
      if DFS(v, graph, colors) == True:
        return True;

  return False;

################################################################################

def main():
  sys.setrecursionlimit(10**6);

  towns = int(input().rstrip());

  graph = [ None ] * (towns + 1);

  for i in range(towns - 1):
    line = input().rstrip();
    ln = len(line);
    townFrom = i + 1;
    for j in range(ln):
      townTo = townFrom + j + 1;
      AddToGraph(graph, townFrom, townTo, line[j]);

  ans = FindLoop(graph);

  if ans == True:
    print("NO");
  else:
    print("YES");

################################################################################

if __name__ == "__main__":
  main();
