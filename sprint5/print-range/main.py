#!/usr/bin/python3

import sys;

class Node:
  def __init__(self, left=None, right=None, value=0):
    self.right = right
    self.left  = left
    self.value = value

  def __repr__(self):
    l = None if (self.left  == None) else hex(id(self.left)).upper().replace('X', 'x');
    r = None if (self.right == None) else hex(id(self.right)).upper().replace('X', 'x');

    return f"< value = { self.value }, left = { l }, right = { r } >";

################################################################################

def PrintTreeIntl(node, level):
  if node != None:
    PrintTreeIntl(node.right, level + 1);
    print(' ' * 2 * level + '-> ' + str(node.value))
    PrintTreeIntl(node.left, level + 1);

################################################################################

def PrintTree(node):
  PrintTreeIntl(node, 0);
  print("="*80);

################################################################################

def Traverse(node, l, r):
  if node != None:
    if (node.value >= l):
      Traverse(node.left, l, r);
    if (node.value >= l) and (node.value <= r):
      print(node.value);
    if (node.value <= r):
      Traverse(node.right, l, r);

################################################################################

def print_range(node, l, r):
  Traverse(node, l, r);

################################################################################

def main():
  n = int(input().rstrip());

  nodes = [ None ] * (n + 1);

  later = [];

  for i in range(n):
    line = list( map(int, sys.stdin.readline().rstrip().split()) );

    ind   = line[0];
    val   = line[1];
    left  = line[2];
    right = line[3];

    if (left == -1) and (right == -1):
      nodes[ind] = Node(None, None, val);
    else:
      later.append([ ind, val, left, right ]);

  while len(later) != 0:
    item = later.pop();

    ind = item[0];
    val = item[1];
    left  = None if (item[2] == -1) else nodes[ item[2] ];
    right = None if (item[3] == -1) else nodes[ item[3] ];

    nodes[ind] = Node(left, right, val);

  PrintTree(nodes[1]);

  rangeAr = [0, 0];

  rangeAr[0] = int(input().rstrip());
  rangeAr[1] = int(input().rstrip());

  print_range(nodes[1], rangeAr[0], rangeAr[1]);

################################################################################

if __name__ == '__main__':
  main();
