#!/usr/bin/python3

import sys;

###############################################################################

Ans = 0;

def Traverse(graph, ind, end):
  global Ans;

  for v in graph[ind]:
    if v == end:
      Ans += 1;
      return;
    Traverse(graph, v, end);

###############################################################################

def main():
  sys.setrecursionlimit(10**6);

  global Ans;

  line = input().rstrip().split();
  n = int(line[0]);
  k = int(line[1]);

  mod = pow(10, 9) + 7;

  graph = [ None ] * (n + 1);

  for i in range(1, n):
    for j in range(k):
      v = (i + 1) + j;

      if v > n:
        break;

      if graph[i] == None:
        graph[i] = [ v ];
      else:
        graph[i].append(v);

  #print(graph);

  Traverse(graph, 1, n);

  print(Ans % mod);

###############################################################################

if __name__ == "__main__":
  main();
