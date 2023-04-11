#!/usr/bin/python3

import sys;
import math;

################################################################################

def GetPointsAroundZero(radius):
  ans = {};
  squared = pow(radius, 2);

  for x in range(-radius, radius + 1, 1):
    for y in range(-radius, radius + 1, 1):
      r = pow(x, 2) + pow(y, 2);
      if (r <= squared):
        ans[(x, y)] = (x, y);

  return ans;

################################################################################

def IsPointInside(origin, point, zeroArea):
  translated = ( point[0] - origin[0], point[1] - origin[1] );
  #print(f"  point = { point }, center = { origin }, translated = { translated }");
  return translated in zeroArea;

################################################################################

def RunTestsR4():
  area = GetPointsAroundZero(4);

  testCases = [
    (-4, 0), (-3, 0), (-2, 0), (-1, 0), (0, 0),
    (1, 0), (2, 0), (3, 0), (4, 0),
    (-3, 1), (-2, 1), (-1, 1), (0, 1), (1, 1), (2, 1), (3, 1),
    (-3, -1), (-2, -1), (-1, -1), (0, -1), (1, -1), (2, -1), (3, -1),
    (-3, 2), (-2, 2), (-1, 2), (0, 2), (1, 2), (2, 2), (3, 2),
    (-3, -2), (-2, -2), (-1, -2), (0, -2), (1, -2), (2, -2), (3, -2),
    (-2, 3), (-1, 3), (0, 3), (1, 3), (2, 3),
    (-2, -3), (-1, -3), (0, -3), (1, -3), (2, -3),
    (0, 4), (0, -4)
  ];

  print("Run tests for r = 4...");

  for point in testCases:
    assert( IsPointInside((0, 0), point, area) == True );

  print("OK");

################################################################################

def main():
  #RunTestsR4();

  searchRadius = 20;

  area = GetPointsAroundZero(searchRadius);

  n = int(input().rstrip());

  exits = {};

  for i in range(n):
    s = input().rstrip().split();
    ex = ( int(s[0]), int(s[1]) );
    exits[ex] = [ i + 1, 0 ];

  m = int(input().rstrip());

  stops = [ None ] * m;

  for i in range(m):
    s = input().rstrip().split();
    stop = ( int(s[0]), int(s[1]) );
    stops[i] = stop;

  maxStops = 0;
  exInd    = 0;

  #
  # O(n*m)
  #
  for exKey, exValue in exits.items():
    for st in stops:
      if IsPointInside(exKey, st, area):
        exValue[1] += 1;
        if exValue[1] > maxStops:
          maxStops = exValue[1];
          exInd    = exValue[0];

  print(exInd);

################################################################################

if __name__ == "__main__":
  main();
