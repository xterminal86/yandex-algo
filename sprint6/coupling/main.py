#!/usr/bin/python3

ComponentCount = 1;

################################################################################

def DFS(start, colors, graph, color):
  global ComponentCount;

  #print("processing", start);

  colors[start] = 1;

  if graph[start] != None:
    for item in graph[start]:
      if colors[item] == 0:
        DFS(item, colors, graph, color);

  #print("  finished processing", start);

  colors[start] = ComponentCount;
  color[start]  = ComponentCount;

################################################################################

def main():
  global ComponentCount;

  line = input().rstrip().split();
  vertices = int(line[0]);
  edges    = int(line[1]);

  graph = [ None ] * (vertices + 1);

  color  = [ -1 ] * (vertices + 1);
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
    if color[i] == -1:
      DFS(i, colors, graph, color);
      #print("DFS finished");
      #print("  color:", color);
      ComponentCount += 1;

  #print(color);

  print(ComponentCount - 1);

  ans = [];

  for i in range(1, ComponentCount + 1):
    for j in range(1, vertices + 1):
      if color[j] == i:
        ans.append(j);

    if len(ans) != 0:
      print(*ans);
      ans = [];

################################################################################

if __name__ == "__main__":
  main();
