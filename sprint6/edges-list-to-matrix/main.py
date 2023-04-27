#!/usr/bin/python3

################################################################################

def main():
  line = input().rstrip().split();
  v = int(line[0]);
  e = int(line[1]);

  matrix = [];

  for i in range(v):
    matrix.append([0] * v);

  for i in range(e):
    line = input().rstrip().split();
    from_ = int(line[0]);
    to    = int(line[1]);

    x = from_ - 1;
    y = to - 1;

    matrix[x][y] = 1;

  for line in matrix:
    print(*line);

################################################################################

if __name__ == "__main__":
  main();
