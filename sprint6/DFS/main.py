#!/usr/bin/python3

################################################################################

def PrintArray(ar):
  ln = len(ar);
  out = "";
  for x in range(1, ln):
    for y in range(1, ln):
      out += f"{ ar[x][y] } ";
    out += "\n";
  print(out);

################################################################################

def MatrixSolution():
  line = input().rstrip().split();
  vertices = int(line[0]);
  edges    = int(line[1]);

  mtx = [ [0 for x in range(vertices + 1)] for y in range(vertices + 1) ];

  colors = [0] * (vertices + 1);

  for i in range(edges):
    line = input().rstrip().split();
    from_ = int(line[0]);
    to    = int(line[1]);

    mtx[from_][to] = 1;
    mtx[to][from_] = 1;

  #PrintArray(mtx);

  start = int(input().rstrip());

  toProcess = [ start ];

  ans = [ start ];

  while len(toProcess) != 0:
    #print("toProcess = ", toProcess);

    v = toProcess.pop();
    #print("got ", v);

    if colors[v] == 0:
      colors[v] = 1;

    if (colors[v] != 2):
      #print("  adding ", v);
      toProcess.append(v);

    found = False;

    for i in range(1, vertices + 1):
      newVert = mtx[v][i];
      #print(f"  processing [{ v }][{ i }]");
      if (newVert == 1) and (colors[i] == 0):
        toProcess.append(i);
        found = True;
        #print("  adding ", i);
        ans.append(i);
        break;

    if not found:
      #print("  no vertices for ", v);
      colors[v] = 2;

  print(*ans);

################################################################################

def BullshitSolution():
  line = input().rstrip().split();
  vertices = int(line[0]);
  edges    = int(line[1]);

  graph = {};

  colors = [0] * (vertices + 1);

  for i in range(edges):
    line = input().rstrip().split();
    f = int(line[0]);
    t = int(line[1]);

    if f not in graph:
      graph[f] = [ t ];
    else:
      graph[f].append(t);

    if t not in graph:
      graph[t] = [ f ];
    else:
      graph[t].append(f);

  for k in graph.keys():
    graph[k].sort();

  start = int(input().rstrip());

  #print(graph, start);

  toProcess = [ start ];

  ans = [ start ];

  while len(toProcess) != 0:
    v = toProcess.pop();

    #print("got ", v);

    if colors[v] == 0:
      colors[v] = 1;

    if colors[v] != 2:
      toProcess.append(v);

    found = False;

    if v in graph:
      for item in graph[v]:
        if colors[item] == 0:
          found = True;
          #print("  found ", item);
          ans.append(item);
          toProcess.append(item);
          break;

    if not found:
      colors[v] = 2;

  print(*ans);

################################################################################

def main():
  #MatrixSolution();
  BullshitSolution();

################################################################################

if __name__ == "__main__":
  main();
