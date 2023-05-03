#!/usr/bin/python3

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
