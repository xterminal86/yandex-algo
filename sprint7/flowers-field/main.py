#!/usr/bin/python3

import sys;

################################################################################

def main():
  line = sys.stdin.readline().rstrip().split();
  x = int(line[0]);
  y = int(line[1]);

  mx = x;
  my = y;

  grid = [ [ 0 for i in range(y) ] for j in range(x) ];

  cx = 0;
  for i in range(x):
    line = sys.stdin.readline().rstrip();
    cy = 0;
    for c in line:
      grid[cx][cy] = 0 if c == '0' else 1;
      cy += 1;
    cx += 1;

  for y in range(my):
    for x in range(mx - 1, -1, -1):
      ly = y - 1;
      hx = x + 1;

      costLeft = 0;
      costDown = 0;

      if (x >= 0 and x < mx) and (ly >= 0 and ly < my):
        costLeft = grid[x][ly];

      if (hx >= 0 and hx < mx) and (y >= 0 and y < my):
        costDown = grid[hx][y];

      cost = max(costLeft, costDown);

      grid[x][y] += cost;

  print(grid[0][ my - 1 ]);

################################################################################

if __name__ == "__main__":
  main();
