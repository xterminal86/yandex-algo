#!/usr/bin/python3

#
# Формат ввода
# В первой строке задано n — количество строк матрицы. Во второй — количество
# столбцов m. Числа m и n не превосходят 1000. В следующих n строках задана
# матрица. Элементы матрицы — целые числа, по модулю не превосходящие 1000.
# В последних двух строках записаны координаты элемента, соседей которого нужно
# найти. Индексация начинается с нуля.
#
# Формат вывода
# Напечатайте нужные числа в возрастающем порядке через пробел.
#

import sys;

Rows = 0;
Cols = 0;

def FindNeighbours(matrix, x, y):
  lx = x - 1;
  ly = y - 1;
  hx = x + 1;
  hy = y + 1;

  res = [];

  if (lx >= 0):
    res.append(matrix[lx][y]);

  if (hx < Rows):
    res.append(matrix[hx][y]);

  if (ly >= 0):
    res.append(matrix[x][ly]);

  if (hy < Cols):
    res.append(matrix[x][hy]);

  res = sorted(res);

  output = "";

  for item in res:
    output += f"{ item } ";

  if len(output) != 0:
    output = output[:-1];

  print(output);

################################################################################

def main():
  global Rows;
  global Cols;

  Rows = int(input().rstrip());
  Cols = int(input().rstrip());

  matrix = [];

  for i in range(Rows):
    line = list(map(int, (sys.stdin.readline().rstrip()).split()));
    matrix.append(line);

  x = int(input().rstrip());
  y = int(input().rstrip());

  FindNeighbours(matrix, x, y);

################################################################################

if __name__ == "__main__":
  main();
