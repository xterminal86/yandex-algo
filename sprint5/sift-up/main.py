#!/usr/bin/python3

#
# Формат ввода
# Элементы кучи —– целые числа, лежащие в диапазоне от −10^9 до 10^9.
# Все элементы кучи уникальны. Передаваемый в функцию индекс лежит в диапазоне
# от 1 до размера передаваемого массива. В куче содержится от 1 до 10^5
# элементов.
#
# Инструкцию по работе с Make вы можете найти в конце этого урока
#

import math;
import sys;

from io import StringIO

################################################################################

def PrintHeap(tree, total_width=80, fill=' '):
  output = StringIO();
  last_row = -1;
  for i, n in enumerate(tree):
    if i:
      row = int(math.floor(math.log(i+1, 2)));
    else:
      row = 0;
    if row != last_row:
      output.write('\n');
    columns = 2**row;
    col_width = int(math.floor((total_width * 1.0) / columns));
    output.write(str(n).center(col_width, fill));
    last_row = row;
  print (output.getvalue());
  print ('-' * total_width);

################################################################################

def sift_up(heap, idx) -> int:
  if (idx == 1):
    return idx;

  parentIndex = idx // 2;

  if (heap[idx] > heap[parentIndex]):
    heap[parentIndex], heap[idx] = heap[idx], heap[parentIndex];
    return sift_up(heap, parentIndex);
  return idx;

################################################################################

def main():
  n = int(input().rstrip());

  ar = list( map(int, sys.stdin.readline().rstrip().split()) );

  ar.insert(0, -1);

  PrintHeap(ar[1:]);

  toAdd = int(input().rstrip());

  for i in range(toAdd):
    line = list( map(int, sys.stdin.readline().rstrip().split()) );
    print(line);
    ar[ line[0] ] += line[1];
    print("Before:");
    PrintHeap(ar[1:]);
    newInd = sift_up(ar, line[0]);
    print("After:");
    PrintHeap(ar[1:]);
    print(f"sift up index = { newInd }");

################################################################################

if __name__ == '__main__':
  main();
