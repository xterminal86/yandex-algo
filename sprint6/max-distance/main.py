#!/usr/bin/python3

from collections import deque;

################################################################################

def BFS(v, graph, colors, distances):
  maxDistance = 0;

  toProcess = deque();

  toProcess.append(v);

  colors[v] = 1;

  while len(toProcess) != 0:
    nv = toProcess.popleft();

    if graph[nv] != None:
      for item in graph[nv]:
        if colors[item] == 0:
          colors[item] = 1;
          distances[item] = distances[nv] + 1;
          if distances[item] > maxDistance:
            maxDistance = distances[item];
          toProcess.append(item);

  return maxDistance;

################################################################################

def main():
  line = input().rstrip().split();
  vertices = int(line[0]);
  edges    = int(line[1]);

  graph = [ None ] * (vertices + 1);

  colors = [0] * (vertices + 1);
  distances = [0] * (vertices + 1);

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

  #print(graph);
  #print(start);

  ans = BFS(start, graph, colors, distances);

  print(ans);

################################################################################

if __name__ == "__main__":
  main();