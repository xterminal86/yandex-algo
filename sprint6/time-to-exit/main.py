#!/usr/bin/python3

################################################################################

Counter = 0;
Entry = [];
Leave = [];

def DFS(v, graph, colors):
  global Counter;
  global Entry;
  global Leave;

  Counter += 1;
  Entry[v] = Counter;

  colors[v] = 1;

  if graph[v] != None:
    for item in graph[v]:
      if colors[item] == 0:
        DFS(item, graph, colors);

  Counter += 1;
  Leave[v] = Counter;
  colors[v] = 2;

  #print("  entry:", Entry);
  #print("  leave:", Leave);

################################################################################

def main():
  global Entry;
  global Leave;
  global Counter;

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
      item.sort();

  #print(graph);

  DFS(1, graph, colors);

  for i in range(1, vertices + 1):
    print(Entry[i] - 1, Leave[i] - 1);

################################################################################

if __name__ == "__main__":
  main();
