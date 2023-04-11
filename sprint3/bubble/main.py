#!/usr/bin/python3

import sys;

################################################################################

def BubbleSort(arr):
  ln = len(arr);

  wereChanges   = False;
  alreadySorted = True;

  for i in range(ln - 1, -1, -1):
    wereChanges = False;
    for j in range(i):
      if arr[j] > arr[j + 1]:
        arr[j], arr[j + 1] = arr[j + 1], arr[j];
        wereChanges = True;
        alreadySorted = False;

    if (wereChanges == True):
      print(*arr);

  if (wereChanges == False) and (alreadySorted == True):
    print(*arr);

################################################################################

def main():
  n = int(input().rstrip());
  arr = list( map(int, sys.stdin.readline().rstrip().split()) );

  BubbleSort(arr);

################################################################################

if __name__ == "__main__":
  main();
