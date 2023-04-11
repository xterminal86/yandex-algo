#!/usr/bin/python3

def merge(arr, left, mid, right):
  return sorted(arr);

################################################################################

def merge_sort(arr, left, right):
  toSort = arr[left:right];
  toSort[:] = sorted(toSort);

  ind = 0;
  for i in range(left, right):
    arr[i] = toSort[ind];
    ind += 1;

################################################################################

def main():
  a = [ 1, 4, 9, 2, 10, 11 ];
  b = merge(a, 0, 3, 6);
  expected = [ 1, 2, 4, 9, 10, 11 ];
  assert b == expected;
  c = [ 1, 4, 2, 10, 1, 2 ];
  merge_sort(c, 0, 6);
  expected = [ 1, 1, 2, 2, 4, 10 ];
  assert c == expected;
  d = [ 4, 5, 3, 0, 1, 2 ];
  expected = [ 4, 5, 0, 3, 1, 2 ];
  merge_sort(d, 2, 4);
  assert d == expected;
  e = [ 49, 67, 66, 73, -85, -76, 59, 17, 65, 85, -16, -16, 35, 70 ];
  expected = [ -85, -76, -16, -16, 17, 35, 49, 59, 65, 66, 67, 70, 73, 85 ];
  merge_sort(e, 0, 14);
  assert e == expected;

################################################################################

if __name__ == "__main__":
  main();