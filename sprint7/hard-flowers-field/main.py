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

  if (x == 1) and (y == 1):
    print(1);
    return;

  '''
  for line in grid:
    print(line);

  print("-"*80);
  '''

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

  '''
  for line in grid:
    print(line);

  print("-"*80);
  '''

  print(grid[0][ my - 1 ]);

  x = 0;
  y = my - 1;

  maxCost = grid[0][ my - 1 ];

  path = "";

  maxVal = 10**6;

  while True:
    c = grid[x][y];

    #print(x, y);

    left = maxVal;
    down = maxVal;

    if y - 1 >= 0:
      left = grid[x][y - 1];

    if x + 1 < mx:
      down = grid[x + 1][y];

    dl = c - left;
    dd = c - down;

    #print(f"dl = { dl } dd = { dd }");

    if dl >= 0 and left > down:
      path += "R";
      y = y - 1;
    elif dd >= 0 and down > left:
      path += "U";
      x = x + 1;
    else:
      if y - 1 >= 0:
        path += "R";
        y = y - 1;
      elif x + 1 < mx:
        path += "U";
        x = x + 1;

    if (x == mx - 1) and (y == 0):
      break;

  print(path[::-1]);

################################################################################

if __name__ == "__main__":
  main();
