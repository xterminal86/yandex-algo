#!/usr/bin/python3

#
# Формат ввода
# В первой строке задано число n — количество строк матрицы.
# Во второй строке задано m — число столбцов, m и n не превосходят 1000.
# В следующих n строках задана матрица. Числа в ней не превосходят по модулю
# 1000.
#
# Формат вывода
# Напечатайте транспонированную матрицу в том же формате, который задан во
# входных данных. Каждая строка матрицы выводится на отдельной строке, элементы
# разделяются пробелами.
#

import sys;

def PrintMatrix(matrix):
  text = "";

  rows = len(matrix);
  cols = len(matrix[0]);

  for x in range(rows):
    for y in range(cols):
      text += f"{ matrix[x][y] }";

      if (y != cols - 1):
        text += " ";

    if (x != rows - 1):
      text += "\n";

  print(text);

################################################################################

def main():
  rows = int(input().rstrip());
  cols = int(input().rstrip());

  if (rows == 0) and (cols == 0):
    return;
  
  matrix = [];

  for x in range(rows):
    line = list( map(int, sys.stdin.readline().rstrip().split()) );
    matrix.append(line);

  res = [];
  
  for i in range(cols):
    res.append([0] * rows);
  
  for x in range(rows):
    for y in range(cols):
      res[y][x] = matrix[x][y];
      
  PrintMatrix(res);

################################################################################

if __name__ == "__main__":
  main();
