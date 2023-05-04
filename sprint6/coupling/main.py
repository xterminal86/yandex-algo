#!/usr/bin/python3

################################################################################

ZoneCounter = 1;

def DFS(start, graph, zones, colors):
  global ZoneCounter;

  toProcess = [ start ];

  while len(toProcess) != 0:
    v = toProcess.pop();

    if colors[v] == 0:
      colors[v] = 1;
      toProcess.append(v);

      if graph[v] != None:
        for item in graph[v]:
          if colors[item] == 0:
            toProcess.append(item);

    elif colors[v] == 1:
      colors[v] = 2;
      zones[v] = ZoneCounter;

################################################################################

def main():
  global ZoneCounter;

  line = input().rstrip().split();
  vertices = int(line[0]);
  edges    = int(line[1]);

  graph = [ None ] * (vertices + 1);

  zones  = [ -1 ] * (vertices + 1);
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

  for i in range(1, vertices + 1):
    if zones[i] == -1:
      DFS(i, graph, zones, colors);
      ZoneCounter += 1;

  print(ZoneCounter - 1);

  for z in range(1, ZoneCounter + 1):
    ans = [];

    for i in range(1, vertices + 1):
      if zones[i] == z:
        ans.append(i);

    if len(ans) != 0:
      print(*ans);

################################################################################

if __name__ == "__main__":
  main();
