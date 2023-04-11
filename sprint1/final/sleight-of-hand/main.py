#!/usr/bin/python3

import sys;

Fingers = 0;

################################################################################

def GetScore(matrix, t):

  buttonsPressed = 0;

  score = 0;
  
  for x in range(4):
    for y in range(4):
      if matrix[x][y] != "." and int(matrix[x][y]) == t:
        buttonsPressed += 1;

      if (buttonsPressed > Fingers):
        return 0;

  if (buttonsPressed != 0):
    score = 1;
  
  return score;        

################################################################################

def main():
  global Fingers;
  
  Fingers = int(input().rstrip()) * 2;

  matrix = [];

  ind = 0;
  
  for i in range(4):
    line = sys.stdin.readline().rstrip();

    matrix.append([]);
    
    for c in line:
      matrix[ind].append(c);

    ind += 1;

  score = 0;
  
  for t in range(10):
    score += GetScore(matrix, t);

  print(score);

################################################################################

if __name__ == "__main__":
  main();
  
