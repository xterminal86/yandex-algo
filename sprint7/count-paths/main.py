#!/usr/bin/python3

###############################################################################

Ans = 0;

def Traverse(graph, ind, end):
  global Ans;

  if graph[ind] != None:
    for v in graph[ind]:
      if v == end:
        Ans += 1;
        return;
      Traverse(graph, v, end);

###############################################################################

def main():
  global Ans;

  line = input().rstrip().split();
  n = int(line[0]);
  m = int(line[1]);

  mod = pow(10, 9) + 7;

  graph = [ None ] * (n + 1);

  for i in range(m):
    line = input().rstrip().split();

    f = int(line[0]);
    t = int(line[1]);

    if graph[f] == None:
      graph[f] = [ t ];
    else:
      graph[f].append(t);

  line = input().rstrip().split();

  a = int(line[0]);
  b = int(line[1]);

  #print(graph);
  #print(a, b);

  Traverse(graph, a, b);

  print(Ans % mod);

###############################################################################

if __name__ == "__main__":
  main();
