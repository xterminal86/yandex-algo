#!/usr/bin/python3

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

  print(graph);

  order = [];

  for i in range(1, vertices + 1):
    if colors[i] == 0:
      TopSort(i, colors, graph, order);

  print(*order);

################################################################################

if __name__ == "__main__":
  main();
