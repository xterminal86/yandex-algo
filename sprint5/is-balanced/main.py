#!/usr/bin/python3

import sys;

class Node:
  def __init__(self, value, left=None, right=None):
    self.value = value;
    self.right = right;
    self.left  = left;

  # --------------------------------------------------------------------------

  def __repr__(self):
    l = None if (self.left  == None) else self.left.value;
    r = None if (self.right == None) else self.right.value;

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

def GetHeight(node):
  if (node == None):
    return 0;

  return 1 + max( GetHeight(node.left), GetHeight(node.right) );

################################################################################

def IsBalanced(node):
  if (node == None):
    return True;

  return IsBalanced(node.left) and \
         IsBalanced(node.right) and \
         abs( GetHeight(node.left) - GetHeight(node.right) ) <= 1;

################################################################################

def solution(root) -> bool:
  return IsBalanced(root);

################################################################################

def main():
  n = int(input().rstrip());

  nodes = [ None ] * n;

  later = [];

  for i in range(n):
    line = sys.stdin.readline().rstrip().split();
    ind = int(line[0]);
    val = int(line[1]);
    left  = line[2];
    right = line[3];

    if (left == "None") and (right == "None"):
      nodes[ind] = Node(val, None, None);
    else:
      later.append([ ind, val, left, right ]);

  while len(later) != 0:
    item = later.pop();

    ind = item[0];
    val = item[1];
    left  = None if (item[2] == "None") else nodes[int(item[2])];
    right = None if (item[3] == "None") else nodes[int(item[3])];

    nodes[ind] = Node(val, left, right);

  PrintTree(nodes[0]);

  res = solution(nodes[0]);

  print(res);

################################################################################

if __name__ == '__main__':
  main();