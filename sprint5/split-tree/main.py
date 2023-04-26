#!/usr/bin/python3

import sys;

from typing import Tuple

class Node:
  def __init__(self, left=None, right=None, value=0, size=0):
    self.right = right;
    self.left  = left;
    self.value = value;
    self.size  = size;

  # ----------------------------------------------------------------------------

  def __repr__(self):
    l = None if (self.left == None) else self.left.value;
    r = None if (self.right == None) else self.right.value;

    s = (
      f"<v = { self.value } "
      f"l = { l } "
      f"r = { r } "
      f"s = { self.size }>"
    );

    return s;

################################################################################

def split(root, k) -> Tuple[Node, Node]:
  pass;

'''
def test():
  node1 = Node(None, None, 3, 1)
  node2 = Node(None, node1, 2, 2)
  node3 = Node(None, None, 8, 1)
  node4 = Node(None, None, 11, 1)
  node5 = Node(node3, node4, 10, 3)
  node6 = Node(node2, node5, 5, 6)
  left, right = split(node6, 4)
  assert(left.size == 4)
  assert(right.size == 2)
'''

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

  print(nodes);

################################################################################

if __name__ == '__main__':
  main();
