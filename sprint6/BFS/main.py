#!/usr/bin/python3

from collections import deque;

################################################################################

def BFS(v, graph, colors):
  toProcess = deque();

  toProcess.append(v);

  colors[v] = 1;

  ans = [];

  while len(toProcess) != 0:
    nv = toProcess.popleft();

    if graph[nv] != None:
      for item in graph[nv]:
        if colors[item] == 0:
          colors[item] = 1;
          toProcess.append(item);
      colors[nv] = 2;
      ans.append(nv);

  print(*ans);

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

  for item in graph:
    if item != None:
      item.sort();

  start = int(input().rstrip());

  #print(graph);
  #print(start);

  if edges == 0:
    print(1);
  else:
    BFS(start, graph, colors);

################################################################################

if __name__ == "__main__":
  main();