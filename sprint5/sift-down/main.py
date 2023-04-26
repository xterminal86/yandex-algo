#!/usr/bin/python3

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

def sift_down(heap, idx) -> int:
  left  = 2 * idx;
  right = 2 * idx + 1;

  ln = len(heap) - 1;

  # нет дочерних узлов
  if (left > ln):
    return idx;

  # right <= heap.size проверяет, что есть оба дочерних узла
  if (right <= ln) and (heap[left] < heap[right]):
    indLargest = right;
  else:
    indLargest = left;

  if (heap[idx] < heap[indLargest]):
    heap[idx], heap[indLargest] = heap[indLargest], heap[idx];
    return sift_down(heap, indLargest);
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
    ar[ line[0] ] -= line[1];
    print("Before:");
    PrintHeap(ar[1:]);
    newInd = sift_down(ar, line[0]);
    print("After:");
    PrintHeap(ar[1:]);
    print(f"sift down index = { newInd }");

################################################################################

if __name__ == '__main__':
  main();
